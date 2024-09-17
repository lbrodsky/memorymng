#!/usr/bin/env python3 

# Multithreading is a technique for running multiple threads simultaneously within a single process. 
# This can be useful for improving the performance of I/O-bound tasks, such as network communication or disk access.

# The threading module provides a Thread class that allows you to easily create and manage threads. 

from threading import Thread

def my_function():
    print("Hello from thread!")

thread = Thread(target=my_function)
thread.start()

# In this example, the my_function function will be executed in a separate thread. 
# You can also use the join() method to wait for a thread to complete before continuing with the main program. 
