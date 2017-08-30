#!/usr/bin/env python

# random.randint(a,b) gives random numbers out with a and be being low and high values

import random
#r = random.randint(1,100)
#print r

nums = []

#xrange gives range of numbers
for i in xrange(10):
   # print i
    r = random.randint(1,100)
    print "the %dth number is %d" % (i,r)
    nums.append(r)
    
print nums

nums.sort ()
print nums

key = 42

#next to lines are equal to for i,v in enumerate(nums):
for i in xrange(len(nums)):
    v = nums[i]
    print "the %dth number is %d" % (i,v)
    if (v == key) :
        print "Found it at the %dth position" %(i)