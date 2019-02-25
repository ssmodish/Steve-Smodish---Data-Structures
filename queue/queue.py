import LinkedList from linked_list

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = new LinkedList

  def enqueue(self, item):
    # add item to one end of self.storage
    # add one to self.size
    pass
  
  def dequeue(self):
    # remove an item from the opposite end of self.storage
    # subtract one from self.size
    pass

  def len(self):
    # return self.size
    pass
