# Compilation Notes
These compilation notes describe things that I learned when I had to compile everything from source, since 2600hz 
currently does not provide binaries for CentOS 7, which I had to use for driver compatibility reasons.

## Kamailio
### Required Modules for Compilation
The following modules are required by the Kazoo scripts for Kamailio:
- ctl
- kex
- tm
- tmx
- sl
- rr
- maxfwd
- siputils
- sanity
- textops
- textopsx
- htable
- pv
- xlog
- mi_fifo
- uac
- uac_redirect
- db_text
- kazoo
