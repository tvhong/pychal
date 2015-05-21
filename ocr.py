#!/usr/bin/python2.7

import os

str = open('ocr.html', 'r').read()

a = {}
for c in str:
    if a.has_key(c):
        a[c] += 1
    else:
        print c
        a[c] = 1
print a
