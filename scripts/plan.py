#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-only

"""Plan the reusable builds.

For every selected tool in tools.json ask LibreELEC.tv for the archive URL, take
the release tag from it, create the release when it does not exist yet, and
print the GitHub Actions matrix of the builds to run. LibreELEC.tv owns the
naming, so nothing here spells out a tag or an archive name.
"""

import argparse
import json
import os
import subprocess
import sys


def resolve(tree, build, package, variable):
    """Return a package variable as LibreELEC.tv resolves it for one build."""
    env = dict(os.environ, PROJECT=build["project"], ARCH=build["arch"], DEVICE=build["device"])
    script = f'. config/options {package} >/dev/null 2>&1; echo "${{{variable}}}"'
    out = subprocess.run(["bash", "-c", script], cwd=tree, env=env, capture_output=True, text=True)
    return out.stdout.strip()


def release_exists(repo, tag):
    return subprocess.run(["gh", "release", "view", tag, "--repo", repo],
                          capture_output=True, text=True).returncode == 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tools", required=True, help="tools.json")
    parser.add_argument("--tree", required=True, help="LibreELEC.tv checkout")
    parser.add_argument("--repo", required=True, help="owner/name of this repository")
    parser.add_argument("--tool", default="all")
    parser.add_argument("--host", default="all")
    parser.add_argument("--notes", required=True, help="release notes file")
    parser.add_argument("--dry-run", action="store_true", help="do not create releases")
    args = parser.parse_args()

    tools = json.load(open(args.tools))
    base = f"https://github.com/{args.repo}/releases/download/"
    matrix = []

    for name, tool in tools.items():
        if args.tool not in ("all", name):
            continue
        builds = [b for b in tool["builds"] if args.host in ("all", b["host"])]
        if not builds:
            continue

        url = resolve(args.tree, builds[0], tool["package"], "PKG_REUSABLE_URL")
        if not url.startswith(base):
            sys.exit(f"{name}: {tool['package']} gives '{url}', expected a URL under {base}")
        tag = url[len(base):].split("/")[0]
        print(f"{name}: release {tag}", file=sys.stderr)

        if not args.dry_run and not release_exists(args.repo, tag):
            os.makedirs(name, exist_ok=True)
            log = f"{name}/build-log.txt"
            with open(log, "w") as f:
                head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=args.tree,
                                      capture_output=True, text=True).stdout.strip()
                f.write(f"{tool['description']} - LibreELEC.tv {head}\n")
                plan = subprocess.run(["tools/viewplan", tool["build"]], cwd=args.tree,
                                      capture_output=True, text=True)
                f.write(plan.stdout)
            subprocess.run(["gh", "release", "create", tag, "--repo", args.repo, "--prerelease",
                            "--title", f"reusable {tool['description']} - {tag}",
                            "--notes-file", args.notes, log], check=True, stdout=sys.stderr)

        for b in builds:
            matrix.append(dict(b, tool=name, package=tool["package"], build=tool["build"], tag=tag))

    # stdout is the GITHUB_OUTPUT file, so only the matrix goes there
    print("matrix=" + json.dumps({"include": matrix}))


if __name__ == "__main__":
    main()
