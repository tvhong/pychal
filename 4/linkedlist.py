#!/usr/bin/python2.7

import urllib.request, re

#id = '12345'
#id = '8022'
id = '63579'
for i in range(400):
    line = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + id).readline().decode('utf-8')
    print(line)
    id = re.search('the next nothing is (\d+)', line).group(1)
