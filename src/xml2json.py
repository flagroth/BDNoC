#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:49:25 2017

@author: javier
"""

import xmltodict, json

xml_file='data/xml/sample.xml'
file=open(xml_file,'r')
json_file='data/json/sample.json'
output=open(json_file,'w')


# WARNING!! Esta línea bloquea el PC. 
o = xmltodict.parse(file.read())
output.write(json.dumps(o))
file.close()
output.close()

