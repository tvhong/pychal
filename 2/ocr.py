#!/usr/bin/python3

import os

str = open('ocr.html', 'r').read()

a = {}
for c in str:
    a.setdefault(c, 0)
    if (a[c] == 0):
        print(c)
    a[c] += 1
print(a)
