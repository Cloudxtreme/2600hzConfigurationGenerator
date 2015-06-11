# Compilation Notes
These compilation notes describe things that I learned when I had to compile everything from source, since 2600hz 
currently does not provide binaries for CentOS 7, which I had to use for driver compatibility reasons.

## Kamailio
### Required Modules for Compilation
The following additional modules are required as of Kamailio 3.4 and Kazoo 3.20. You actually don't need all of them if you 
don't use some of the roles that are disabled by default. Also note that you need to include the DB of your choice if you plan 
on using sqlops
- kazoo
- presence
- presence_dialoginfo
- presence_mwi
- presence_xml
- sqlops
- tls
- websocket

### Regenerating dbtext
If you receive errors, you need to regenerate the text databases. This happened to me when I upgraded to Kamailio 3.4 but was 
still using Kazoo 3.20 configs. This website goes into detail:
http://nil.uniza.sk/sip/kamailio/kamailio-31-text-file-database-dbtext

## FreeSwitch
### Required Modules for Compilation
- formats/mod_shout
- event_handlers/mod_erlang_event

### A Note on Erlang Installation Order
If Erlang is installed after the FreeSwitch build process starts, the Erland header files won't be found. At this point, 
it is best to start over (delete FreeSwitch and redownload it).
