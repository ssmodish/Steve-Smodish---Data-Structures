import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

try:
    sys.path.remove(str(parent))
except ValueError:
    pass

from linked_list.linked_list import LinkedList
from linked_list.linked_list import Node


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        queue = LinkedList()
        self.storage = queue

    def enqueue(self, item):
        # add item to one end of self.storage
        self.storage.add_to_tail(item)
        # add one to self.size
        self.size += 1

    def dequeue(self):
        # do nothing if there are there no items in the queue
        if self.size == 0:
            return
        # subtract one from self.size
        self.size -= 1
        # remove an item from the opposite end of self.storage
        return self.storage.remove_head()

    def len(self):
        # return self.size
        return self.size



