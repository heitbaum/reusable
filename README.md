# reusable
Prebuilt host tools used by LibreELEC, one release per tool.

Every archive is named in the same way, by `reusable_names` in LibreELEC.tv:

- release tag: `<tool>-<OS_VERSION>-<version>`
- archive: `<tool>-reusable-<OS_VERSION>-<version>-<host>[-<variant>]-<hash>.tar.xz`

| tool          | built from (`BUILD_REUSABLE`)              | variant         |
|---------------|--------------------------------------------|-----------------|
| binutils      | `binutils:host`                            | `<TARGET_NAME>` |
| bison         | `bison:host`                               |                 |
| cargo         | `cargo:host` (with rust:host)              | `<TARGET_NAME>` |
| ccache        | `ccache:host`                              |                 |
| cmake         | `cmake:host`                               |                 |
| flatbuffers   | `flatbuffers:host`                         |                 |
| flex          | `flex:host`                                |                 |
| gcc-bootstrap | `gcc:bootstrap`                            | `<TARGET_NAME>` |
| gettext       | `gettext:host`                             |                 |
| heimdal       | `heimdal:host`                             |                 |
| libjpeg-turbo | `libjpeg-turbo:host`                       |                 |
| llvm          | `llvm:host`                                | `<TARGET_ARCH>` |
| m4            | `m4:host`                                  |                 |
| mesa          | `mesa:host`                                |                 |
| or1k          | `gcc-or1k:host` (with binutils-or1k:host)  |                 |
| pcre2         | `pcre2:host`                               |                 |

`<host>` is the build host (x86_64 or aarch64). A tool built for each target
carries the target as its variant, at the granularity its build depends on.
`<hash>` covers the recipes the tool is built from and, where it matters, its
configure options, so a recipe change in LibreELEC.tv names a different
archive and an old one is never used. A `MANIFEST` in each archive records the
versions it was built with. Archives that would otherwise carry the toolchain
path list the files LibreELEC.tv fills the path back into in `RELOCATE`, so
every archive unpacks into any toolchain.

LibreELEC.tv owns the naming: the workflow asks the tree for each archive's URL
and name, takes the release tag from the URL and skips archives that are
already published. `tools.json` lists the tools and the hosts and targets each
is built for.

LibreELEC.tv fetches from `REUSABLE_URL` (`distributions/LibreELEC/options`)
with `USE_REUSABLE="preferred"` (or `"yes"`).
