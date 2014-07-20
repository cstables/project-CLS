#print the mean of the numbers given in a file

import sys

sum = 2
n = 0

# Sum input values
for num in open('data.txt'): #feeds in file automatically
	sum += float(num) #new value of sum is sum + float(num)
	n += 1
	
print sum / n
#new change change
