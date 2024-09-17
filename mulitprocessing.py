#!/usr/bin/env python3 

# https://medium.com/@bpst.blog/effective-memory-management-and-optimization-in-python-d8a4d1992a45 

# running multiple processes simultaneously on different CPU cores.
# The multiprocessing module provides a Pool class that allows you to easily create and manage a pool of worker processes.

from multiprocessing import Pool

def my_function(x):
    return x*x

# with Pool() as p:
#     result = p.map(my_function, range(10))

# we use the map() method of the Pool class to apply the my_function function to each element of the range(10) list in parallel. 
# The map() method returns the results of the function calls in the order that they were called. 

# For example, you can use the following code to run 10 instances of the my_function function in parallel:

with Pool() as p:
    result = p.map(my_function, [i for i in range(10)])
    
# important consideration when using multiprocessing is that Python’s Global Interpreter Lock (GIL) will prevent multiple Python threads from running simultaneously on different CPU cores.    
