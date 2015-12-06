# -*-coding: utf8 -*-

import requests
import re
from sys import argv
import os
import time
import subprocess


if len(argv) != 3:
	print 'Uso: python getemall.py path/to/webpage.html|url search_regexp'
	exit()
if argv[1].startswith('http'):
	html = requests.get(argv[1]).content
else: 
	html = open(argv[1]).read()
print argv[2]

found = re.finditer(argv[2], html)
if found:
	if not os.path.exists('getemall-descargas/'):
		os.mkdir('getemall-descargas/')
	os.chdir('getemall-descargas/')
	fecha = time.strftime("%H:%M:%S %d-%m-%Y")
	print fecha
	os.makedirs(fecha)
	os.chdir(fecha)
	for item in found:
		G = open(item.group(2), 'w')
		print item.group(2)
		G.write(requests.get(item.group(1)).content)
else: 
	print 'No se encontró nada. Revisa la regexp o el html'