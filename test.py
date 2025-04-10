#test
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

print(node1.data)

from collections import deque
queue = deque()
queue.append(1)  # Enqueue
queue.append(2)
print(queue.popleft())  # Dequeue, returns 1
