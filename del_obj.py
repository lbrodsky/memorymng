#!/usr/bin/env python3 

# Memory Management in Python 

class SomeObject(): 
    def __init__(self) -> None:
        pass
    def run(self): 
        print('This is my object') 


my_object = SomeObject()
# Do something with my_object
my_object.run()

# manually manage your objects using the del keyword.
del my_object

try:
    my_object.run()
except:
    print('Object was aready removed.')