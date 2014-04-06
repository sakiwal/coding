#!/usr/bin/env python

import sys

# Find number provided at command prompt
# then convert to an integer
n = sys.argv[1]
n = int(n)

second time lucky

# Figured out strange algorithm; results in 100x
# speedup
result = n/2 * (n+1)
print "XXSum", result


# calculate the sum from 1 to n

result = 0
for i in xrange(n+1):
	#print i, result
	result = i + result
print "XSum:", result

result = 0
for i in range(n+1):
	#print i, result
	result = i + result
print "Sum:", result


