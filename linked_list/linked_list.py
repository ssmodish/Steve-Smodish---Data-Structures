class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # wrap input value in new node
        new_node = Node(value)
        # check if we have anything in our linked list
        # if not
        if not self.head:
            # set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # we do
        else:
            # set the new node as the list's last node's next node
            self.tail.set_next(new_node)
            # set the list's tail as the new node
            self.tail = new_node

    def remove_head(self):
        # is the list empty? (is self.head == None?)
        if not self.head:
            return None
        # if it isn't , see if we only have one element (is self.head.next == None?
        #   and is self.head == self.tail
        if self.head.get_next() is None:
            # get a new reference to the current head node
            head = self.head
            # set self.head to None
            self.head = None
            # set self.tail to None
            self.tail = None
            # return value of old head element
            return head.value
        # if there is more than one element
        else:
            # get a new reference to the current head node
            head = self.head
            # set self.head to current head's next node
            self.head = self.head.get_next()
            # return value of old head element
            return head.value

    def contains(self, value):
        # check to see if list is empty
        if not self.head:
            # return none
            return None
        # init `current_node` variable to keep track of where we are in the list
        current_node = self.head
        # check while `current_node` is a valid node
        while current_node:
            # check if current node.value == input value
            if current_node.get_value() == value:
                # return True
                return True
            # update `current_node` to `current_node.next`
            current_node = current_node.get_next()
        # we checked the whole list and did not find value
        # return false
        return False


