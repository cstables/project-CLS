#print the mean of the numbers given in a file

import sys

sum = 0
n = 0

# Sum input values
for num in open('data.txt'):
	sum += float(num) #new value of sum is sum + float(num)
	n += 1
	
print sum / n

