'''
words_tweeted.py
Purpose: Calculates the total number of times each word has been tweeted
Method: Use a dictionary, each word as key and count as value
Output: the total count for each word in ASCII order to a text file
Created on Jul 6, 2015
@author: maeq
'''
import sys
from collections import defaultdict

#get the input & output file names
input_file=sys.argv[1]
output_file=sys.argv[2]

#define a dictionary
word_count = defaultdict(int)

#count each word using the dictionary
with open(input_file,"r") as fin:
    for line in fin:
        for word in line.split():
            word_count[word]+=1

#output the result to a text file in ASCII order
with open(output_file,"w") as fout:
    for key in sorted(word_count):           
        fout.write("%s %s\n" % (key, word_count[key]))
