# reusable
Prebuilt host tools used by LibreELEC, one release per tool.

| tool  | built from (`BUILD_REUSABLE`) | release tag                     | archive |
|-------|-------------------------------|---------------------------------|---------|
| cargo | `cargo:host` (with rust:host) | `cargo-<OS_VERSION>-<rust>`     | `cargo-reusable-<OS_VERSION>-<rust>-<host>-<TARGET_NAME>-<hash>.tar.xz` |
| mesa  | `mesa:host`                   | `mesa-<OS_VERSION>-<mesa>`      | `mesa-reusable-<OS_VERSION>-<mesa>-<host>-<hash>.tar.xz` |

`<hash>` is taken from the tool's `package.mk`, so a recipe change in
LibreELEC.tv names a different archive and an old one is never used. A
`MANIFEST` in each archive records the versions it was built with.

LibreELEC.tv owns the naming: the workflow asks the tree for each archive's URL
and name, takes the release tag from the URL and skips archives that are
already published. `tools.json` lists the tools and the hosts and targets each
is built for.

LibreELEC.tv fetches from `REUSABLE_URL` (`distributions/LibreELEC/options`)
with `USE_REUSABLE="preferred"` (or `"yes"`).
