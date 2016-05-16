#!/usr/bin/env python
import csv



with open('simple.txt', 'r') as myfile:
	 data=myfile.read().replace('\n', '')

'''
def ngrams(input, n):
	input = input.split()
	output = []
	print len(input)
	for i in range(len(input)-n+1):
		output.append(input[i:i+n])
		
	print (output)
		#return output 
ngrams(data, 2) 
'''

def ngrams(input, n):
	input = input.split(' ')
	output = {}
	for i in range(len(input)-n+1):
	  	g = ' '.join(input[i:i+n])
	  	output.setdefault(g, 0)
	  	output[g] += 1
	print (output)
ngrams(data, 2)

'''
def ngrams(input, n):
	input = input.split()
	output = []
	print len(input)
	for i in range(len(input)-n+1):
		output.append(input[i:i+n])
	print (output)
		#return output 
ngrams("ram bahadur hari bahadur", 2) 

'''

