#!/usr/bin/python3

import re
from zipfile import ZipFile, ZipInfo

def get_filename(id):
    return 

id = 90052
channelzip = ZipFile('channel.zip', 'r') 
data = None
for i in range(4000):
    tmp = channelzip.getinfo('{}.txt'.format(id)).comment
    if data == None:
        data = tmp
    else:
        data += tmp
    

    line = open('channel/{}.txt'.format(id), 'r').readlines()
    #print(line)
    m = re.search('Next nothing is (\d+)', line[0])
    if m is None:
        break
    id = m.group(1)

print(data)
