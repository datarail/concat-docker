#!/usr/bin/env python

'''
Application that concatenates files listed in /input/concat_config.yml.

Optionally, converts the output file to all-uppercase if a given environment
variable ("UPPERCASE") is set.

Outputs to /output/concatenated.txt.
'''

import os
import ruamel.yaml as yaml

# Check for the environment variable to convert output to all caps
try:
    convert_to_upper = os.environ['UPPERCASE'].upper() == 'TRUE'
except Exception:
    convert_to_upper = False

# Read an expected configuration file
with open('/config/concat.yml') as c:
    config = yaml.safe_load(c)

# Concatenate the files into a single string
output = ''
for file in config['inputs']:
    with open('/input/' + file, 'r') as f:
        output += f.read()

# Convert to all caps if that environment variable requested it
if convert_to_upper:
    output = output.upper()

# Write concatenated string out to a file
with open('/output/concatenated.txt', 'w') as f:
    f.write(output)
