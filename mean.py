import sys

sum = 0
n = 0

# Sum input values
for num in sys.stdin:
	sum += float(num) #new value of sum is sum + float(num)
	n += 1
	
print sum / n

