Name:           kamailio
Version:        4.3.0
Release:        1%{?dist}
Summary:        Open Source SIP Server

License:        GPLv2
URL:            http://www.kamailio.org
Source0:        http://www.kamailio.org/pub/kamailio/latest/src/kamailio-%{version}_src.tar.gz

BuildRequires:  rabbitmq-server
Requires:       rabbitmq-server

%description
Kamailio SIP Server for use with 2600hz Kazoo

%prep
%setup -q


%build
make cfg prefix=/usr cfg_prefix=$RPM_BUILD_ROOT basedir=$RPM_BUILD_ROOT \
	cfg_target=/%{_sysconfdir}/kamailio/ modules_dirs="modules" \
	include_modules="kazoo \
		presence \
		presence_dialoginfo \
		presence_mwi \
		presence_xml \
		sqlops \
		tls \
		websocket"
make all

%install
rm -rf $RPM_BUILD_ROOT
make install


%files
%config(noreplace) %{_sysconfdir}/kamailio/dictionary.kamailio
%config(noreplace) %{_sysconfdir}/kamailio/kamailio-advanced.cfg
%config(noreplace) %{_sysconfdir}/kamailio/kamailio-basic.cfg
%exclude %{_sysconfdir}/kamailio/kamailio-selfsigned.key
%exclude %{_sysconfdir}/kamailio/kamailio-selfsigned.pem
%config(noreplace) %{_sysconfdir}/kamailio/kamailio.cfg
%config(noreplace) %{_sysconfdir}/kamailio/kamctlrc
%config(noreplace) %{_sysconfdir}/kamailio/tls.cfg
%{_libdir}/kamailio/kamctl/dbtextdb/dbtextdb.py
%{_libdir}/kamailio/kamctl/dbtextdb/dbtextdb.pyc
%{_libdir}/kamailio/kamctl/dbtextdb/dbtextdb.pyo
%{_libdir}/kamailio/kamctl/kamctl.base
%{_libdir}/kamailio/kamctl/kamctl.ctlbase
%{_libdir}/kamailio/kamctl/kamctl.dbtext
%{_libdir}/kamailio/kamctl/kamctl.fifo
%{_libdir}/kamailio/kamctl/kamctl.ser
%{_libdir}/kamailio/kamctl/kamctl.ser_mi
%{_libdir}/kamailio/kamctl/kamctl.sqlbase
%{_libdir}/kamailio/kamctl/kamctl.unixsock
%{_libdir}/kamailio/kamctl/kamdbctl.base
%{_libdir}/kamailio/kamctl/kamdbctl.dbtext
%{_libdir}/kamailio/libbinrpc.so
%{_libdir}/kamailio/libbinrpc.so.0
%{_libdir}/kamailio/libbinrpc.so.0.1
%{_libdir}/kamailio/libkcore.so
%{_libdir}/kamailio/libkcore.so.1
%{_libdir}/kamailio/libkcore.so.1.0
%{_libdir}/kamailio/libkmi.so
%{_libdir}/kamailio/libkmi.so.1
%{_libdir}/kamailio/libkmi.so.1.0
%{_libdir}/kamailio/libprint.so
%{_libdir}/kamailio/libprint.so.1
%{_libdir}/kamailio/libprint.so.1.2
%{_libdir}/kamailio/libsrdb1.so
%{_libdir}/kamailio/libsrdb1.so.1
%{_libdir}/kamailio/libsrdb1.so.1.0
%{_libdir}/kamailio/libsrdb2.so
%{_libdir}/kamailio/libsrdb2.so.1
%{_libdir}/kamailio/libsrdb2.so.1.0
%{_libdir}/kamailio/libsrutils.so
%{_libdir}/kamailio/libsrutils.so.1
%{_libdir}/kamailio/libsrutils.so.1.0
%{_libdir}/kamailio/libtrie.so
%{_libdir}/kamailio/libtrie.so.1
%{_libdir}/kamailio/libtrie.so.1.0
%{_libdir}/kamailio/modules/acc.so
%{_libdir}/kamailio/modules/alias_db.so
%{_libdir}/kamailio/modules/async.so
%{_libdir}/kamailio/modules/auth.so
%{_libdir}/kamailio/modules/auth_db.so
%{_libdir}/kamailio/modules/auth_diameter.so
%{_libdir}/kamailio/modules/auth_xkeys.so
%{_libdir}/kamailio/modules/avp.so
%{_libdir}/kamailio/modules/avpops.so
%{_libdir}/kamailio/modules/benchmark.so
%{_libdir}/kamailio/modules/blst.so
%{_libdir}/kamailio/modules/call_control.so
%{_libdir}/kamailio/modules/cfg_db.so
%{_libdir}/kamailio/modules/cfg_rpc.so
%{_libdir}/kamailio/modules/cfgutils.so
%{_libdir}/kamailio/modules/corex.so
%{_libdir}/kamailio/modules/counters.so
%{_libdir}/kamailio/modules/ctl.so
%{_libdir}/kamailio/modules/db2_ops.so
%{_libdir}/kamailio/modules/db_cluster.so
%{_libdir}/kamailio/modules/db_flatstore.so
%{_libdir}/kamailio/modules/db_text.so
%{_libdir}/kamailio/modules/debugger.so
%{_libdir}/kamailio/modules/dialog.so
%{_libdir}/kamailio/modules/dispatcher.so
%{_libdir}/kamailio/modules/diversion.so
%{_libdir}/kamailio/modules/dmq.so
%{_libdir}/kamailio/modules/dmq_usrloc.so
%{_libdir}/kamailio/modules/domain.so
%{_libdir}/kamailio/modules/domainpolicy.so
%{_libdir}/kamailio/modules/drouting.so
%{_libdir}/kamailio/modules/enum.so
%{_libdir}/kamailio/modules/exec.so
%{_libdir}/kamailio/modules/group.so
%{_libdir}/kamailio/modules/htable.so
%{_libdir}/kamailio/modules/imc.so
%{_libdir}/kamailio/modules/ipops.so
%{_libdir}/kamailio/modules/jsonrpc-s.so
%{_libdir}/kamailio/modules/kazoo.so
%{_libdir}/kamailio/modules/kex.so
%{_libdir}/kamailio/modules/malloc_test.so
%{_libdir}/kamailio/modules/mangler.so
%{_libdir}/kamailio/modules/matrix.so
%{_libdir}/kamailio/modules/maxfwd.so
%{_libdir}/kamailio/modules/mediaproxy.so
%{_libdir}/kamailio/modules/mi_datagram.so
%{_libdir}/kamailio/modules/mi_fifo.so
%{_libdir}/kamailio/modules/mi_rpc.so
%{_libdir}/kamailio/modules/mohqueue.so
%{_libdir}/kamailio/modules/mqueue.so
%{_libdir}/kamailio/modules/msilo.so
%{_libdir}/kamailio/modules/msrp.so
%{_libdir}/kamailio/modules/mtree.so
%{_libdir}/kamailio/modules/nat_traversal.so
%{_libdir}/kamailio/modules/nathelper.so
%{_libdir}/kamailio/modules/nosip.so
%{_libdir}/kamailio/modules/p_usrloc.so
%{_libdir}/kamailio/modules/path.so
%{_libdir}/kamailio/modules/pdb.so
%{_libdir}/kamailio/modules/pdt.so
%{_libdir}/kamailio/modules/permissions.so
%{_libdir}/kamailio/modules/pike.so
%{_libdir}/kamailio/modules/pipelimit.so
%{_libdir}/kamailio/modules/prefix_route.so
%{_libdir}/kamailio/modules/presence.so
%{_libdir}/kamailio/modules/presence_dialoginfo.so
%{_libdir}/kamailio/modules/presence_mwi.so
%{_libdir}/kamailio/modules/presence_xml.so
%{_libdir}/kamailio/modules/print.so
%{_libdir}/kamailio/modules/print_lib.so
%{_libdir}/kamailio/modules/pv.so
%{_libdir}/kamailio/modules/qos.so
%{_libdir}/kamailio/modules/ratelimit.so
%{_libdir}/kamailio/modules/registrar.so
%{_libdir}/kamailio/modules/rr.so
%{_libdir}/kamailio/modules/rtimer.so
%{_libdir}/kamailio/modules/rtjson.so
%{_libdir}/kamailio/modules/rtpengine.so
%{_libdir}/kamailio/modules/rtpproxy.so
%{_libdir}/kamailio/modules/sanity.so
%{_libdir}/kamailio/modules/sca.so
%{_libdir}/kamailio/modules/sdpops.so
%{_libdir}/kamailio/modules/seas.so
%{_libdir}/kamailio/modules/sipcapture.so
%{_libdir}/kamailio/modules/sipt.so
%{_libdir}/kamailio/modules/siptrace.so
%{_libdir}/kamailio/modules/siputils.so
%{_libdir}/kamailio/modules/sl.so
%{_libdir}/kamailio/modules/sms.so
%{_libdir}/kamailio/modules/speeddial.so
%{_libdir}/kamailio/modules/sqlops.so
%{_libdir}/kamailio/modules/sst.so
%{_libdir}/kamailio/modules/statistics.so
%{_libdir}/kamailio/modules/statsd.so
%{_libdir}/kamailio/modules/stun.so
%{_libdir}/kamailio/modules/tcpops.so
%{_libdir}/kamailio/modules/textops.so
%{_libdir}/kamailio/modules/textopsx.so
%{_libdir}/kamailio/modules/timer.so
%{_libdir}/kamailio/modules/tls.so
%{_libdir}/kamailio/modules/tm.so
%{_libdir}/kamailio/modules/tmrec.so
%{_libdir}/kamailio/modules/tmx.so
%{_libdir}/kamailio/modules/topoh.so
%{_libdir}/kamailio/modules/tsilo.so
%{_libdir}/kamailio/modules/uac.so
%{_libdir}/kamailio/modules/uac_redirect.so
%{_libdir}/kamailio/modules/uid_auth_db.so
%{_libdir}/kamailio/modules/uid_avp_db.so
%{_libdir}/kamailio/modules/uid_domain.so
%{_libdir}/kamailio/modules/uid_gflags.so
%{_libdir}/kamailio/modules/uid_uri_db.so
%{_libdir}/kamailio/modules/uri_db.so
%{_libdir}/kamailio/modules/userblacklist.so
%{_libdir}/kamailio/modules/usrloc.so
%{_libdir}/kamailio/modules/websocket.so
%{_libdir}/kamailio/modules/xhttp.so
%{_libdir}/kamailio/modules/xhttp_rpc.so
%{_libdir}/kamailio/modules/xlog.so
%{_libdir}/kamailio/modules/xprint.so
%{_sbindir}/kamailio
%{_sbindir}/kamcmd
%{_sbindir}/kamctl
%{_sbindir}/kamdbctl
%doc %{_docdir}/kamailio/AUTHORS
%doc %{_docdir}/kamailio/INSTALL
%doc %{_docdir}/kamailio/NEWS
%doc %{_docdir}/kamailio/README
%doc %{_docdir}/kamailio/README-MODULES
%doc %{_docdir}/kamailio/modules/README.acc
%doc %{_docdir}/kamailio/modules/README.alias_db
%doc %{_docdir}/kamailio/modules/README.async
%doc %{_docdir}/kamailio/modules/README.auth
%doc %{_docdir}/kamailio/modules/README.auth_db
%doc %{_docdir}/kamailio/modules/README.auth_diameter
%doc %{_docdir}/kamailio/modules/README.auth_xkeys
%doc %{_docdir}/kamailio/modules/README.avp
%doc %{_docdir}/kamailio/modules/README.avpops
%doc %{_docdir}/kamailio/modules/README.benchmark
%doc %{_docdir}/kamailio/modules/README.blst
%doc %{_docdir}/kamailio/modules/README.call_control
%doc %{_docdir}/kamailio/modules/README.cfg_db
%doc %{_docdir}/kamailio/modules/README.cfg_rpc
%doc %{_docdir}/kamailio/modules/README.cfgutils
%doc %{_docdir}/kamailio/modules/README.corex
%doc %{_docdir}/kamailio/modules/README.counters
%doc %{_docdir}/kamailio/modules/README.ctl
%doc %{_docdir}/kamailio/modules/README.db2_ops
%doc %{_docdir}/kamailio/modules/README.db_cluster
%doc %{_docdir}/kamailio/modules/README.db_flatstore
%doc %{_docdir}/kamailio/modules/README.db_text
%doc %{_docdir}/kamailio/modules/README.debugger
%doc %{_docdir}/kamailio/modules/README.dialog
%doc %{_docdir}/kamailio/modules/README.dispatcher
%doc %{_docdir}/kamailio/modules/README.diversion
%doc %{_docdir}/kamailio/modules/README.dmq
%doc %{_docdir}/kamailio/modules/README.dmq_usrloc
%doc %{_docdir}/kamailio/modules/README.domain
%doc %{_docdir}/kamailio/modules/README.domainpolicy
%doc %{_docdir}/kamailio/modules/README.drouting
%doc %{_docdir}/kamailio/modules/README.enum
%doc %{_docdir}/kamailio/modules/README.exec
%doc %{_docdir}/kamailio/modules/README.group
%doc %{_docdir}/kamailio/modules/README.htable
%doc %{_docdir}/kamailio/modules/README.imc
%doc %{_docdir}/kamailio/modules/README.ipops
%doc %{_docdir}/kamailio/modules/README.jsonrpc-s
%doc %{_docdir}/kamailio/modules/README.kazoo
%doc %{_docdir}/kamailio/modules/README.kex
%doc %{_docdir}/kamailio/modules/README.malloc_test
%doc %{_docdir}/kamailio/modules/README.mangler
%doc %{_docdir}/kamailio/modules/README.matrix
%doc %{_docdir}/kamailio/modules/README.maxfwd
%doc %{_docdir}/kamailio/modules/README.mediaproxy
%doc %{_docdir}/kamailio/modules/README.mi_datagram
%doc %{_docdir}/kamailio/modules/README.mi_fifo
%doc %{_docdir}/kamailio/modules/README.mi_rpc
%doc %{_docdir}/kamailio/modules/README.mohqueue
%doc %{_docdir}/kamailio/modules/README.mqueue
%doc %{_docdir}/kamailio/modules/README.msilo
%doc %{_docdir}/kamailio/modules/README.msrp
%doc %{_docdir}/kamailio/modules/README.mtree
%doc %{_docdir}/kamailio/modules/README.nat_traversal
%doc %{_docdir}/kamailio/modules/README.nathelper
%doc %{_docdir}/kamailio/modules/README.nosip
%doc %{_docdir}/kamailio/modules/README.p_usrloc
%doc %{_docdir}/kamailio/modules/README.path
%doc %{_docdir}/kamailio/modules/README.pdb
%doc %{_docdir}/kamailio/modules/README.pdt
%doc %{_docdir}/kamailio/modules/README.permissions
%doc %{_docdir}/kamailio/modules/README.pike
%doc %{_docdir}/kamailio/modules/README.pipelimit
%doc %{_docdir}/kamailio/modules/README.prefix_route
%doc %{_docdir}/kamailio/modules/README.presence
%doc %{_docdir}/kamailio/modules/README.presence_dialoginfo
%doc %{_docdir}/kamailio/modules/README.presence_mwi
%doc %{_docdir}/kamailio/modules/README.presence_xml
%doc %{_docdir}/kamailio/modules/README.print
%doc %{_docdir}/kamailio/modules/README.print_lib
%doc %{_docdir}/kamailio/modules/README.pv
%doc %{_docdir}/kamailio/modules/README.qos
%doc %{_docdir}/kamailio/modules/README.ratelimit
%doc %{_docdir}/kamailio/modules/README.registrar
%doc %{_docdir}/kamailio/modules/README.rr
%doc %{_docdir}/kamailio/modules/README.rtimer
%doc %{_docdir}/kamailio/modules/README.rtjson
%doc %{_docdir}/kamailio/modules/README.rtpengine
%doc %{_docdir}/kamailio/modules/README.rtpproxy
%doc %{_docdir}/kamailio/modules/README.sanity
%doc %{_docdir}/kamailio/modules/README.sca
%doc %{_docdir}/kamailio/modules/README.sdpops
%doc %{_docdir}/kamailio/modules/README.seas
%doc %{_docdir}/kamailio/modules/README.sipcapture
%doc %{_docdir}/kamailio/modules/README.sipt
%doc %{_docdir}/kamailio/modules/README.siptrace
%doc %{_docdir}/kamailio/modules/README.siputils
%doc %{_docdir}/kamailio/modules/README.sl
%doc %{_docdir}/kamailio/modules/README.sms
%doc %{_docdir}/kamailio/modules/README.speeddial
%doc %{_docdir}/kamailio/modules/README.sqlops
%doc %{_docdir}/kamailio/modules/README.sst
%doc %{_docdir}/kamailio/modules/README.statistics
%doc %{_docdir}/kamailio/modules/README.statsd
%doc %{_docdir}/kamailio/modules/README.stun
%doc %{_docdir}/kamailio/modules/README.tcpops
%doc %{_docdir}/kamailio/modules/README.textops
%doc %{_docdir}/kamailio/modules/README.textopsx
%doc %{_docdir}/kamailio/modules/README.timer
%doc %{_docdir}/kamailio/modules/README.tls
%doc %{_docdir}/kamailio/modules/README.tm
%doc %{_docdir}/kamailio/modules/README.tmrec
%doc %{_docdir}/kamailio/modules/README.tmx
%doc %{_docdir}/kamailio/modules/README.topoh
%doc %{_docdir}/kamailio/modules/README.tsilo
%doc %{_docdir}/kamailio/modules/README.uac
%doc %{_docdir}/kamailio/modules/README.uac_redirect
%doc %{_docdir}/kamailio/modules/README.uid_auth_db
%doc %{_docdir}/kamailio/modules/README.uid_avp_db
%doc %{_docdir}/kamailio/modules/README.uid_domain
%doc %{_docdir}/kamailio/modules/README.uid_gflags
%doc %{_docdir}/kamailio/modules/README.uid_uri_db
%doc %{_docdir}/kamailio/modules/README.uri_db
%doc %{_docdir}/kamailio/modules/README.userblacklist
%doc %{_docdir}/kamailio/modules/README.usrloc
%doc %{_docdir}/kamailio/modules/README.websocket
%doc %{_docdir}/kamailio/modules/README.xhttp
%doc %{_docdir}/kamailio/modules/README.xhttp_rpc
%doc %{_docdir}/kamailio/modules/README.xlog
%doc %{_docdir}/kamailio/modules/README.xprint
%{_datarootdir}/kamailio/dbtext/kamailio/acc
%{_datarootdir}/kamailio/dbtext/kamailio/acc_cdrs
%{_datarootdir}/kamailio/dbtext/kamailio/active_watchers
%{_datarootdir}/kamailio/dbtext/kamailio/address
%{_datarootdir}/kamailio/dbtext/kamailio/aliases
%{_datarootdir}/kamailio/dbtext/kamailio/carrier_name
%{_datarootdir}/kamailio/dbtext/kamailio/carrierfailureroute
%{_datarootdir}/kamailio/dbtext/kamailio/carrierroute
%{_datarootdir}/kamailio/dbtext/kamailio/cpl
%{_datarootdir}/kamailio/dbtext/kamailio/dbaliases
%{_datarootdir}/kamailio/dbtext/kamailio/dialog
%{_datarootdir}/kamailio/dbtext/kamailio/dialog_vars
%{_datarootdir}/kamailio/dbtext/kamailio/dialplan
%{_datarootdir}/kamailio/dbtext/kamailio/dispatcher
%{_datarootdir}/kamailio/dbtext/kamailio/domain
%{_datarootdir}/kamailio/dbtext/kamailio/domain_attrs
%{_datarootdir}/kamailio/dbtext/kamailio/domain_name
%{_datarootdir}/kamailio/dbtext/kamailio/domainpolicy
%{_datarootdir}/kamailio/dbtext/kamailio/dr_gateways
%{_datarootdir}/kamailio/dbtext/kamailio/dr_groups
%{_datarootdir}/kamailio/dbtext/kamailio/dr_gw_lists
%{_datarootdir}/kamailio/dbtext/kamailio/dr_rules
%{_datarootdir}/kamailio/dbtext/kamailio/globalblacklist
%{_datarootdir}/kamailio/dbtext/kamailio/grp
%{_datarootdir}/kamailio/dbtext/kamailio/htable
%{_datarootdir}/kamailio/dbtext/kamailio/imc_members
%{_datarootdir}/kamailio/dbtext/kamailio/imc_rooms
%{_datarootdir}/kamailio/dbtext/kamailio/lcr_gw
%{_datarootdir}/kamailio/dbtext/kamailio/lcr_rule
%{_datarootdir}/kamailio/dbtext/kamailio/lcr_rule_target
%{_datarootdir}/kamailio/dbtext/kamailio/location
%{_datarootdir}/kamailio/dbtext/kamailio/location_attrs
%{_datarootdir}/kamailio/dbtext/kamailio/matrix
%{_datarootdir}/kamailio/dbtext/kamailio/missed_calls
%{_datarootdir}/kamailio/dbtext/kamailio/mohqcalls
%{_datarootdir}/kamailio/dbtext/kamailio/mohqueues
%{_datarootdir}/kamailio/dbtext/kamailio/mtree
%{_datarootdir}/kamailio/dbtext/kamailio/mtrees
%{_datarootdir}/kamailio/dbtext/kamailio/pdt
%{_datarootdir}/kamailio/dbtext/kamailio/pl_pipes
%{_datarootdir}/kamailio/dbtext/kamailio/presentity
%{_datarootdir}/kamailio/dbtext/kamailio/pua
%{_datarootdir}/kamailio/dbtext/kamailio/purplemap
%{_datarootdir}/kamailio/dbtext/kamailio/re_grp
%{_datarootdir}/kamailio/dbtext/kamailio/rls_presentity
%{_datarootdir}/kamailio/dbtext/kamailio/rls_watchers
%{_datarootdir}/kamailio/dbtext/kamailio/rtpproxy
%{_datarootdir}/kamailio/dbtext/kamailio/sca_subscriptions
%{_datarootdir}/kamailio/dbtext/kamailio/silo
%{_datarootdir}/kamailio/dbtext/kamailio/sip_trace
%{_datarootdir}/kamailio/dbtext/kamailio/speed_dial
%{_datarootdir}/kamailio/dbtext/kamailio/subscriber
%{_datarootdir}/kamailio/dbtext/kamailio/trusted
%{_datarootdir}/kamailio/dbtext/kamailio/uacreg
%{_datarootdir}/kamailio/dbtext/kamailio/uid_credentials
%{_datarootdir}/kamailio/dbtext/kamailio/uid_domain
%{_datarootdir}/kamailio/dbtext/kamailio/uid_domain_attrs
%{_datarootdir}/kamailio/dbtext/kamailio/uid_global_attrs
%{_datarootdir}/kamailio/dbtext/kamailio/uid_uri
%{_datarootdir}/kamailio/dbtext/kamailio/uid_uri_attrs
%{_datarootdir}/kamailio/dbtext/kamailio/uid_user_attrs
%{_datarootdir}/kamailio/dbtext/kamailio/uri
%{_datarootdir}/kamailio/dbtext/kamailio/userblacklist
%{_datarootdir}/kamailio/dbtext/kamailio/usr_preferences
%{_datarootdir}/kamailio/dbtext/kamailio/version
%{_datarootdir}/kamailio/dbtext/kamailio/watchers
%{_datarootdir}/kamailio/dbtext/kamailio/xcap
%{_mandir}/man5/kamailio.cfg.5.gz
%{_mandir}/man8/kamailio.8.gz
%{_mandir}/man8/kamcmd.8.gz
%{_mandir}/man8/kamctl.8.gz
%{_mandir}/man8/kamdbctl.8.gz


%changelog
* Tue Jun 16 2015 Thomas Newman <tnewman1@ltu.edu>
  - Initial
