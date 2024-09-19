#!/usr/local/bin/python3

# import garbage collector interface
import gc 
import numpy as np 


for i in range(1000):
    data = np.load('tmp.npz')
    # process data
    del data 
    gc.collect()

print('end')

