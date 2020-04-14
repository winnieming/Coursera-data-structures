#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:10:40 2020

@author: Winnie
"""


'''
10.2 Write a program to read through the mbox-short.txt and figure out
the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then
splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below.
'''

fname = open("mbox-short.txt")
counts = dict()

for line in fname:
    if not line.startswith("From"): continue
    words = line.split()
    if words[0] == 'From':
        time = words[5].split(':')
        hr = time[0]
        counts[hr] = counts.get(hr, 0) + 1
    
print(sorted([(k, v) for k, v in counts.items()]))