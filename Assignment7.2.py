# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and
compute the average of those values and produce an output as shown below. Do
not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
'''

fname = input("Enter file name\n")
fh = open(fname)
count = 0
sum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence"):
        continue
    count += 1   
    pos = line.find('0')
    sum += float(line[pos:])
    average = sum / count
print ("Average spam confidence: ", average)