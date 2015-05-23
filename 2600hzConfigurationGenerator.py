#!/usr/bin/env python
from jinja2 import Environment, FileSystemLoader
from os import listdir, urandom
from uuid import uuid4

TEMPLATES_FOLDER = 'templates'
OUTPUT_FOLDER = 'configuration'

IP = '192.168.1.239'
FQDN = 'citatest.local'
BIG_COUCH_COOKIE = uuid4().hex
WHISTLE_COOKIE = uuid4().hex
FREESWITCH_COOKIE = uuid4().hex

print('2600hz Configuration Generator')

env = Environment(loader=FileSystemLoader(TEMPLATES_FOLDER))

template_files = listdir(TEMPLATES_FOLDER)

for template_file in template_files:
	template = env.get_template(template_file)
	
	rendered_template = template.render(ip=IP, fqdn=FQDN, big_couch_cookie=BIG_COUCH_COOKIE, 
		whistle_cookie=WHISTLE_COOKIE, freeswitch_cookie=FREESWITCH_COOKIE)
	
	with open(OUTPUT_FOLDER + '/' + template_file, 'w') as rendered_template_file:
		rendered_template_file.write(rendered_template)
	
	print('Rendered ' + template_file)
