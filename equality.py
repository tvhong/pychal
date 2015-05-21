#!/usr/bin/python2.7

import re

str = open('equality.html', 'r').read()
print re.findall('[^A-Z][A-Z]{3,3}([a-z])[A-Z]{3,3}[^A-Z]', str)
