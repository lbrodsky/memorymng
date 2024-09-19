#!/usr/bin/env python3 

# https://stackoverflow.com/questions/9244397/memory-overflow-when-using-numpy-load-in-a-loop
# Looping over npz files load causes memory overflow (depending on the file list length).
# None of the following seems to help: 
# 1. Deleting the variable which stores the data in the file.
# 2. Using mmap.
# 3. calling gc.collect() (garbage collection).


import numpy as np

# generate a file for the demo
# X = np.random.randn(1000,1000)
# np.savez('tmp.npz',X=X)


# here come the overflow:
for i in range(1000000):
    data = np.load('tmp.npz')
    del data.f 
    data.close()  # avoid the "too many files are open" error

print('done')