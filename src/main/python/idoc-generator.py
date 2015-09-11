#!/usr/bin/python

__author__ = 'peterbukhal'

import xml.etree.ElementTree as ET
import os

output_directory = 'output'

if (not os.path.isdir(output_directory)):
    os.mkdir(output_directory)

def generate_idoc(idoc_num, bolnr_num, xabln_num, sscc_num):
    tree = ET.parse('../resources/delivery_template.xml')
    root = tree.getroot()

    for bolnr in root.iter('BOLNR'):
        bolnr.text = str(bolnr_num)

    for xabln in root.iter('XABLN'):
        xabln.text = str(xabln_num)

    for sscc in root.iter('SSCC'):
        sscc.text = str(sscc_num)

    print ('bolnr: ' + str(bolnr_num) + ' xabln: ' + str(xabln_num) + ' sscc: ' + str(sscc_num) + ' -> ' + output_directory + '/idoc' + str(idoc_num) + '.xml')

    tree.write(output_directory + '/idoc' + str(idoc_number) + '.xml')

bolnr = 121662240
xabln = 123522790
sscc = 789613220008442413

for idoc_number in range(1, 21):
    bolnr += 1
    xabln += 1
    sscc += 1

    generate_idoc(idoc_number, bolnr, xabln, sscc)

