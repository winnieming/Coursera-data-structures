#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:44:33 2020

@author: Winnie
"""
'''
8.4 Open the file romeo.txt and read it line by line. For each line, split the
line into a list of words using the split() method. The program should build a
list of words. For each word on each line check to see if the word is already
in the list and if not append it to the list. When the program completes,
sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.pythonlearn.com/code/romeo.txt
'''

fname = input("Enter file name\n")
fh = open(fname)

lst = list()

for line in fh:
    for word in line.split():
        if not word in lst:
            lst.append(word)
lst.sort()
print(lst)