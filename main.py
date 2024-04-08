# How to Get the length of a Queue in Python

from collections import deque
import queue

deq = deque(['a', 'b', 'c'])

# ✅ Get the length of a deque object
print(len(deq))  # 👉️ 3


q = queue.Queue()

for item in range(15):
    q.put(item)

# ✅ Get the length of a queue object
print('size of queue: ', q.qsize()) # 👉️ 15