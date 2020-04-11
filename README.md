
# <img src='https://hackr.io/tutorials/learn-data-structures-algorithms/logo/logo-data-structures-algorithms?ver=1550834269' height='50' width='50'> <a style="font-size:50px" >Data Structure</a>

### **1.** `Queue` (FIFO) first-in firt-out

#### `I` **BaseQueue**
`BaseQueue` simple queue which support only very basic methods of queue data structure

Start with `BaseQueue`
```python
from ds import BaseQueue

# maxsize is optional in BaseQueue
# if maxsize is not given than queue will be dynamic
# end never full

# static or fixed size 
base_queue = BaseQueue(maxsize=2)

# dynamic size
base_queue = BaseQueue()
```

enqueue element in queue
```python

base_queue = BaseQueue(maxsize=2)
base_queue.enqueue(10) # enqueue first element 
base_queue.enqueue(20) # enqueue sescond enqueue 
print(base_queue())  # printing all enqueue
```
    [10,20]
```python
base_queue.enqueue(30) #will raise error as an queuq size is only two and third element can't be pushed
```
    AssertionError: Queue is full

dequeue element in queue
```python
base_queue.dequeue()
base_queue.dequeue()
print(base_queue())
```
    []
```python
base_queue.base_queue() #will raise error as an queue size is only two and third element can't be pushed
```
  AssertionError: Queue is empty

example
```python
from ds import BaseQueue

base_queue = BaseQueue(maxsize=2)
base_queue.enqueue(10) # enqueue first element 
base_queue.enqueue(20) # enqueue sescond enqueue 
print(base_queue())
base_queue.dequeue()
base_queue.dequeue()
print(base_queue())

```
