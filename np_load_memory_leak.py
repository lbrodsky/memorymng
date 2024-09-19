import numpy as np
import gc

# here come the overflow:
for i in range(10000):
    data = np.load('tmp.npz')
    data.close()  # avoid the "too many files are open" error

d = dict()
for o in gc.get_objects():
    name = type(o).__name__
    if name not in d:
        d[name] = 1
    else:
        d[name] += 1

items = d.items()
items.sort(key=lambda x:x[1])
for key, value in items:
    print(key, value) 
