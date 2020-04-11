# -*- coding: utf-8 -*-
"""
Queue
===

 Queue (FIFO) first-in firt-out
+===========================================================================+
|   method        |    discription                                          |
|_________________|_________________________________________________________|
|   enqueue,put   | Adding element in queuq                                 |
|___________________________________________________________________________|
|   dequeue       | Removing element(first element) form queue              |
|___________________________________________________________________________|
|   isfull        | Check queue is full or not. return value--> True,False  |
|___________________________________________________________________________|
|   isempty       | Check queue is empty or not. return value--> True,False |
|___________________________________________________________________________|
|   front         | get front element of queue                              |
|___________________________________________________________________________|
|   reare         | get front element of queue                              |
|___________________________________________________________________________|
|   front_index   | get front element index in queue                        |
|___________________________________________________________________________|
|   reare_index   | get reare element index in queue                        |
|___________________________________________________________________________|
|   element       | get queue in reurn                                      |
|___________________________________________________________________________|
|   count         | get total element count in queue                        |
|___________________________________________________________________________|
|   index         | get index element in queue                              |
|___________________________________________________________________________|
|   clear         | clear or remove all element from queue                  |
|___________________________________________________________________________|
"""

################################ imports ##############################
from typing import overload
from enum import Enum 

QueueType = Enum('Static','Dynamic')

"""
Queue
"""
import queue 

class Queue(object):
    """ Queue  """
    def __init__(self,queue=[],maxsize=10):
        """ 
        __queue : list will hold all element
        __type :  QueueType enum var 
        __front : front index of queue
        __rear : reare index of queue
        """
        assert type(queue)==list,"queue should be type of  list"
        self.__queue: list = []
        self.__front: int = 0
        self.__rear: int = 0
        self.__maxsize: int = maxsize
    
    def __call__(self,*args):
        return self.enqueue(*args)
    
    def enqueue(self,*args):
        for i in args:
            self.__queue.append(i)
            self.__rear+=1
        return self.__queue
            
    
    def put(self,*args):
        return self.enqueue(*args)

    def dequeue(self,count=1):
        for i in range(count):
            self.__queue[self.__front]=None
            self.__front+=1

    def pop(self,count=1):
        return self.dequeue(count)
    
    def front(self):
        return self.__queue[self.__front]
    
    def reare(self):
        return self.__queue[self.__rear]

    def __str__(self):
        return self.__queue

"""
Enum for queue type
+============================================+
|   type    |  discription                   |
|___________|________________________________|
|           | front and reare both will move |
|  Dynamic  | accourding to opration         |
|___________|________________________________|
|           | front will remain zero and     |
|   Static  | move accourding to opration    |
|___________|________________________________|

"""
    