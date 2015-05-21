#!/usr/bin/python2.7

import urllib, re

id = '63579'
for i in range(400):
    line = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + id).readline()
    print line
    id = re.search('the next nothing is (\d+)', line).group(1)
