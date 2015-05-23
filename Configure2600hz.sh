#!/bin/bash
set -x #echo on
python 2600hzConfigurationGenerator.py
cp -f configuration/config.ini /etc/kazoo/config.ini
cp -f configuration/config.js /var/www/html/kazoo-ui/config/config.js
cp -f configuration/dispatcher /etc/kazoo/kamailio/dbtext/dispatcher
cp -f configuration/haproxy.cfg /etc/kazoo/haproxy/haproxy.cfg
cp -f configuration/kazoo.conf.xml /etc/kazoo/freeswitch/autoload_configs/kazoo.conf.xml
cp -f configuration/local.cfg /etc/kazoo/kamailio/local.cfg
cp -f configuration/vm.args /etc/kazoo/bigcouch/vm.args
