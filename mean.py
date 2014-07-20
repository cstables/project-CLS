#print the mean of the numbers given in a file

import sys

sum = 4

n = 0

# Sum input values THIS IS NEW
for num in open('data.txt'): #feeds in file automatically
	sum += float(num) #new value of sum is sum + float(num)
	n += 1
	
print sum / n
#Newer change change
