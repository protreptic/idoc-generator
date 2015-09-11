#!/usr/bin/python
from collections import defaultdict

__author__ = 'peterbukhal'

import xml.etree.ElementTree as ET
import os
import uuid
import argparse

output_directory = 'output'

def generate_idoc():
    tree = ET.parse(template_file)
    root = tree.getroot()

    for bolnr_tag in root.iter('BOLNR'):
        bolnr_tag.text = str(uuid.uuid4().int)[0:10]

    for xabln_tag in root.iter('XABLN'):
        xabln_tag.text = str(uuid.uuid4().int)[0:10]

    for sscc_tag in root.iter('SSCC'):
        sscc_tag.text = str(uuid.uuid4().int)[0:18]

    tree.write(output_directory + str('/idoc-' + str(uuid.uuid4()) + '.xml').upper())

parser = argparse.ArgumentParser(prog='idoc-generator')
parser.add_argument("--output",
                    type=str, help="A full path to output folder for idocs")
parser.add_argument("--template",
                    type=str, help="A full path to an IDOC template file")
parser.add_argument("--gen-number",
                    type=int, help="Number IDOCs to be generated")
parser.add_argument("--clean",
                    type=bool,
                    help="")

args = parser.parse_args()

print args.output;

output_directory = args.output
clean_directory = args.clean
template_file = args.template
gen_number = args.gen_number

if (not os.path.isdir(output_directory)):
    os.mkdir(output_directory)

if (clean_directory):
    for idoc in os.listdir(output_directory):
        os.remove(output_directory + '/' + idoc)

for idoc_number in range(0, gen_number): generate_idoc()
