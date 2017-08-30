#!/usr/bin/env python

import random

nums = range(0,100,10)

key = 70

#whole list should be searched 
lo = 0
hi = len(nums)

#main loop keep going until we find it
while lo < hi:
    mididx = (lo+hi)/2    
    mid = nums[mididx]
    print "checking in the range [%d, %d], mididx [%d]=%d" % (lo, hi, mididx, mid)
    
    if (mid == key):
        print "you found %d" % (key)
        break
    elif (mid < key):
        lo = mididx + 1    
    else:
        hi = mididx