"""other filled started to get to filled"""
from collections import deque
# queues (FIFO = First In First Out)
# the import of deque helps with preformance (example large lists)
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)

queue.popleft() #special deque method
print(queue)
if not queue:
    print('empty')


# tuples can not be modified so use them when you dont want data to get change
point = (1, 2, 3)

