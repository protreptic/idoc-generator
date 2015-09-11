#!/usr/bin/python

__author__ = 'peterbukhal'

import xml.etree.ElementTree as ET
import os
import uuid

output_directory = 'output'

if (not os.path.isdir(output_directory)):
    os.mkdir(output_directory)

def generate_idoc(idoc_num):
    tree = ET.parse('../resources/delivery_template.xml')
    root = tree.getroot()

    for bolnr_tag in root.iter('BOLNR'):
        bolnr_tag.text = str(uuid.uuid4().int)[0:10]

    for xabln_tag in root.iter('XABLN'):
        xabln_tag.text = str(uuid.uuid4().int)[0:10]

    for sscc_tag in root.iter('SSCC'):
        sscc_tag.text = str(uuid.uuid4().int)[0:18]

    tree.write(output_directory + '/idoc' + str(idoc_num) + '.xml')

for idoc_number in range(1, 101):
    generate_idoc(idoc_number)

