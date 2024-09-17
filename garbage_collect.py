#!/usr/bin/env python3 

# Memory Management in Python 
# use the gc.collect() method to manually trigger the garbage collector. 
# This can be useful in situations where you want to free up memory as quickly as possible.

import gc

# check the configured thresholds of your garbage collector 
print(gc.get_threshold()) # (700, 10, 10)

# check the number of objects in each of your generations
print(gc.get_count())
# In this example, we have 430 objects in our youngest generation, one object in the next generation, and one object in the oldest generation.

# Python creates a number of objects by default before you even start executing your program. 
# You can trigger a manual garbage collection process by using the gc.collect() method:
print('---')
print('Trigger a manual garbage collection process:')
print(gc.get_count())
print(gc.collect()) 
print(gc.get_count()) 

# Running a garbage collection process cleans up a huge amount of objects—there are 577 objects 
# in the first generation and three more in the older generations.

# You can alter the thresholds for triggering garbage collection by using the 
# set_threshold() method in the gc module:
print('---') 
print('Alter the thresholds for triggering garbage collection:')
print(gc.get_threshold()) 
gc.set_threshold(1000, 15, 15)
print(gc.get_threshold()) 



# class myObj():
#     def __init__(self, num) -> None:
#         self.num = num
#     def power(self):
#         return self.num**3 


# for i in range(10000):
#     print(i)
#     j = myObj(i)
#     j.power()
#     # assuming count reference is not zero but still
#     # object won't remain usable after the iteration

#     if (i%100):
#         gc.collect()