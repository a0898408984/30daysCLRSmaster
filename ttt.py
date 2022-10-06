import queue

q = queue.Queue()
q.put('3')
print(q.qsize())
q.put('2')
print(q.qsize())
q.put('1')
