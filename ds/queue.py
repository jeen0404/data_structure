# -*- coding: utf-8 -*-
"""
Queue
===
 Queue (FIFO) first-in firt-out
+===========================================================================+
|   method        |    discription                                          |
|_________________|_________________________________________________________|
|   enqueue,push  | Adding element in queuq                                 |
|___________________________________________________________________________|
|   dequeue,pop   | Removing element(first element) form queue              |
|___________________________________________________________________________|
|   isfull        | Check queue is full or not. return value--> True,False  |
|___________________________________________________________________________|
|   isempty       | Check queue is empty or not. return value--> True,False |
|___________________________________________________________________________|
|   head          | get head element of queue                               |
|___________________________________________________________________________|
|   tail          | get head element of queue                               |
|___________________________________________________________________________|
|   head_index    | get head element index in queue                         |
|___________________________________________________________________________|
|   tail_index    | get tail element index in queue                         |
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
"""
Queue
"""


class BaseQueue(object):
    def __init__(self, maxsize=None):
        """
        _queue : list will hold all element
        __type :  QueueType enum var
        tail : tail index of queue
        """
        self._queue: list = []
        self.tail: int = 0
        self._maxsize: int = maxsize

    def __call__(self):
        return self._queue

    def enqueue(self, item):
        assert self.tail != self._maxsize, 'Queue is full'
        self._queue.append(item)
        self.tail += 1
        return self._queue

    def dequeue(self, count=1):
        assert self.tail != 0, 'Queue is empty'
        self.tail -= 1
        return self._queue.pop(0)


class Queue(BaseQueue):
    """ Queue  """
    def __init__(self, maxsize=None):
        super().__init__(maxsize=maxsize)

    def __call__(self):
        return self._queue

    def put(self, *args):
        return self.enqueue(*args)

    def pop(self, count=1):
        assert type(count) == int, 'numper of element to pop should be int'
        for i in range(count):
            self.dequeue
        return self.dequeue(count)

    def push(self, *args):
        if len(args) > 0:
            if type(args[0]) == list:
                [self.enqueue(i) for i in args[0]]
            else:
                [self.enqueue(i) for i in args]
        return self._queue

    def head(self):
        return self._queue[0]

    def tail(self):
        assert self.tail != 0, 'Queue is empty'
        return self._queue[self.tail - 1]

    def tail_index(self):
        return self.tail
    
    def len(self):
        return len(self._queue)

    def __str__(self,item):
        return self._queue.index(item)

    def __str__(self):
        return self._queue

    def __add__(self, queuq):
        [self.enqueue(i) for i in queuq()]
        return self._queue
