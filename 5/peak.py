#!/usr/bin/python3

import pickle,sys

f = open('banner.p', 'rb')
listoflist = pickle.load(f)
for l in listoflist:
    for t in l:
        print(t[0] * t[1], end="")
    print()
