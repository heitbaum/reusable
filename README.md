# reusable
Prebuilt host tools used by LibreELEC, one release per tool.

| tool  | built from (`BUILD_REUSABLE`) | release tag                     | archive |
|-------|-------------------------------|---------------------------------|---------|
| cargo | `cargo:host` (with rust:host) | `cargo-<OS_VERSION>-<rust>`     | `cargo-reusable-<OS_VERSION>-<rust>-<host>-<TARGET_NAME>-<hash>.tar.xz` |
| mesa  | `mesa:host`                   | `mesa-<OS_VERSION>-<mesa>`      | `mesa-reusable-<OS_VERSION>-<mesa>-<host>-<hash>.tar.xz` |
| cmake | `cmake:host`                  | `cmake-<OS_VERSION>-<cmake>`    | `cmake-reusable-<OS_VERSION>-<cmake>-<host>-<hash>.tar.xz` |
| gettext | `gettext:host`             | `gettext-<OS_VERSION>-<gettext>` | `gettext-reusable-<OS_VERSION>-<gettext>-<host>-<hash>.tar.xz` |
| or1k  | `gcc-or1k:host` (with binutils-or1k:host) | `or1k-<OS_VERSION>-<gcc>` | `or1k-reusable-<OS_VERSION>-<gcc>-<host>-<hash>.tar.xz` |
| llvm  | `llvm:host`                   | `llvm-<OS_VERSION>-<llvm>`      | `llvm-reusable-<OS_VERSION>-<llvm>-<host>-<TARGET_ARCH>-<hash>.tar.xz` |
| m4 | `m4:host` | `m4-<OS_VERSION>-<m4 version>` | `m4-reusable-<OS_VERSION>-<version>-<host>-<hash>.tar.xz` |
| bison | `bison:host` | `bison-<OS_VERSION>-<bison version>` | `bison-reusable-<OS_VERSION>-<version>-<host>-<hash>.tar.xz` |
| flex | `flex:host` | `flex-<OS_VERSION>-<flex version>` | `flex-reusable-<OS_VERSION>-<version>-<host>-<hash>.tar.xz` |
| ccache | `ccache:host` | `ccache-<OS_VERSION>-<ccache version>` | `ccache-reusable-<OS_VERSION>-<version>-<host>-<hash>.tar.xz` |
| heimdal | `heimdal:host` | `heimdal-<OS_VERSION>-<heimdal version>` | `heimdal-reusable-<OS_VERSION>-<version>-<host>-<hash>.tar.xz` |
| flatbuffers | `flatbuffers:host` | `flatbuffers-<OS_VERSION>-<flatbuffers version>` | `flatbuffers-reusable-<OS_VERSION>-<version>-<host>-<hash>.tar.xz` |
| pcre2 | `pcre2:host` | `pcre2-<OS_VERSION>-<pcre2 version>` | `pcre2-reusable-<OS_VERSION>-<version>-<host>-<hash>.tar.xz` |
| libjpeg-turbo | `libjpeg-turbo:host` | `libjpeg-turbo-<OS_VERSION>-<libjpeg-turbo version>` | `libjpeg-turbo-reusable-<OS_VERSION>-<version>-<host>-<hash>.tar.xz` |

`<hash>` is taken from the tool's `package.mk`, so a recipe change in
LibreELEC.tv names a different archive and an old one is never used. A
`MANIFEST` in each archive records the versions it was built with. Archives
that would otherwise carry the toolchain path (gettext, or1k, llvm) list the files that
LibreELEC.tv fills the path back into in `RELOCATE`, so every archive unpacks
into any toolchain.

LibreELEC.tv owns the naming: the workflow asks the tree for each archive's URL
and name, takes the release tag from the URL and skips archives that are
already published. `tools.json` lists the tools and the hosts and targets each
is built for.

LibreELEC.tv fetches from `REUSABLE_URL` (`distributions/LibreELEC/options`)
with `USE_REUSABLE="preferred"` (or `"yes"`).
