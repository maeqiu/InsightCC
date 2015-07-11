'''
median_unique.py
Purpose: Calculate the median number of unique words per tweet
Method: Use a 1-d array to store the appearance frequency of each number of unique words.
        The number of unique words is corresponding to the index of this 1-d array
        Compute the median based on the appearance frequency.
Output: the median number of unique words to a text file
Created on Jul 6, 2015
@author: maeq
'''
import sys
import numpy as np

#get the input & output file names
input_file=sys.argv[1]
output_file=sys.argv[2]

#set an initial size, then initialize the frequency array
SIZE=50
freq=np.zeros((SIZE))
 
fout=open(output_file,"w")
with open(input_file,"r") as fin:
    for line in fin:
        #get the number of unique words in each tweet
        i=len(set(line.split()))
        
        #increase array size if necessary
        while i>=freq.shape[0]:
            freq=np.concatenate([freq,np.zeros(SIZE)])
            
        #count the frequency of each number of unique words    
        freq[i]+=1
        n=sum(freq)         #sum 
        c=np.cumsum(freq)   #cumulative sum
        
        #compute median based on the frequency
        #when even number of elements, the median is the average of values at the (n/2) & (n/2+1) positions.
        if n%2==0:
            k1=np.where(c>=n/2)[0][0]
            k2=np.where(c>=(n/2+1))[0][0]
            m=(k1+k2)/2.0
        else:        #when odd number of elements, the median is the value at the (n+1)/2 position
            m=1.0*np.where(c>=(n+1)/2)[0][0]
         
        #output to a text file    
        fout.write("%.2f\n" % m)   
fout.close()
