#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:47:05 2020

@author: Winnie
"""
'''
8.5 Open the file mbox-short.txt and read it line by line. When you find a line
that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the
line (i.e. the entire address of the person who sent the message). Then print
out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt
'''

fname = input("Enter file name: \n")
fn = open(fname)

count = 0

for line in fn:
    if not line.startswith("From"): continue
    line = line.split()
    count += 1
    print(line[1])
    
print("There were", count, "lines in the file with From as the first word")