"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        # wrap input value in new node
        current_node = ListNode(value)
        # check to see if we have anything in the list already.
        # if not
        if self.head is None:
            # set both the head and tail to the new node
            self.head = current_node
            self.tail = current_node
        # if we do
        else:
            # set the lists head as the new node's next
            current_node.next = self.head
            # set the new node as the lists head's prev
            self.head.prev = current_node
            # set the new node as the lists head
            self.head = current_node

    def remove_from_head(self):
        # make sure we have items in the list
        if self.head is None:
            # if we don't return None
            return None
        # if we do, see if we have only one element
        elif self.head == self.tail:
            # get the value of head
            current_node = self.head
            # set head and tail to None
            self.head = None
            self.tail = None
            # return value of former head
            return current_node.value
        # if there's more than one element
        else:
            # get a new reference to the current head node
            current_node = self.head
            # set current_node.next's prev node to None
            current_node.next.prev = None
            # set self.head to the current head's next node
            self.head = current_node.next
            # return value of the former head
            return current_node.value

    def add_to_tail(self, value):
        # wrap input value in new node
        current_node = ListNode(value)
        # check to see if we have anything in the list already.
        # if not
        if self.tail == None:
            # set both the head and tail to the new node
            self.head = current_node
            self.tail = current_node
            # if we do
        else:
            # set the lists tail as the new node's prev
            current_node.prev = self.tail
            # set the new node as the lists tails's next
            self.tail.next = current_node
            # set the new node as the lists tail
            self.tail = current_node

    def remove_from_tail(self):
        # make sure we have items in the list
        if self.head is None:
            # if we don't return None
            return None
        # if we do, see if we have only one element
        elif self.head == self.tail:
            # get the value of tail
            current_node = self.tail
            # set head and tail to None
            self.head = None
            self.tail = None
            # return value of former tail
            return current_node.value
        # if there's more than one element
        else:
            # get a new reference to the current tail node
            current_node = self.tail
            # set self.tail to the current tail's prev node
            self.tail = current_node.prev
            # set self.tail's next node to None
            self.tail.next = None
            # return reference to the former tail
            return current_node.value

    def move_to_front(self, node):
        # make sure there is more than one item in the list
        if self.head != self.tail:
            # if there is set a reference to the selected node
            current_node = node
            # if that node isn't the head or tail
            if node != self.head and node != self.tail:
                # set the next node's prev to the current node's prev
                current_node.next.prev = current_node.prev
                # set the prev node's next as the current node's next
                current_node.prev.next = current_node.next
                # set the referenced node as the current heads prev
                self.head.prev = current_node
                # set the referenced nodes next as the current head
                current_node.next = self.head
                # set the referenced nodes prev to None
                current_node.prev = None
                # set self.head as the referenced node
                self.head = current_node
            # else if it is the tail
            elif node == self.tail:
                # set the previous node's next to None
                current_node.prev.next = None
                # set the tail to the previous node
                self.tail = current_node.prev
                # set the current node's next as the head and prev to none
                current_node.next = self.head
                current_node.prev = None
                # set the head's prev to the current node
                self.head.prev = current_node
                # set the head to the current node
                self.head = current_node
            # otherwise it's already the head

    def move_to_end(self, node):
        # make sure there is more than one item in the list
        if self.tail != self.head:
            # if there is set a reference to the selected node
            current_node = node
            # check to see if current node is not the head
            if node != self.head and node != self.tail:
                # set the next node's prev to the current node's prev
                current_node.next.prev = current_node.prev
                # set the prev node's next as the current node's next
                current_node.prev.next = current_node.next
                # set the referenced node as the current tails next
                self.tail.next = current_node
                # set the referenced nodes prev as the current tail
                current_node.prev = self.tail
                # set the referenced nodes next to None
                current_node.next = None
                # set self.tail as the referenced node
                self.tail = current_node
            elif node == self.head:
                # set the next node's prev to none
                current_node.next.prev = None
                # set the head to the next node
                self.head = current_node.next
                # set the current node's prev to the tail and next to none
                current_node.prev = self.tail
                current_node.next = None
                # set the tail's next to the current node
                self.tail.next = current_node
                # set the tail as the current node
                self.tail = current_node


    def delete(self, node):
        # make sure there are more than one items in our list
        if self.head == self.tail:
            self.head = None
            self.tail = None
            node.delete()
        else:
            # make a reference to the selected node
            current_node = node
            # check to see if the selected node is the head or tail
            # if it is the head
            if current_node == self.head:
                # set self.head to the next node
                self.head = current_node.next
                # set current_node.next's prev to None
                self.head.prev = None
            # if it is the tail
            elif current_node == self.tail:
                # set self.tail to the prev node
                self.tail = current_node.prev
                # set self.tail's next to None
                self.tail.next = None
            # if it isn't the head or tail
            else:
                # set the next nodes prev to the current nodes prev
                current_node.next.prev = current_node.prev
                # set prev nodes next to the current nodes next
                current_node.prev.next = current_node.next
            # delete the node
            current_node.delete()


    def get_max(self):
            # make sure there are items in the list
            if self.head:
                # set max_value to the value of self.head
                max_val = self.head.value
                # set a node at the top of the list
                current_node = self.head
                # while we are not at the end of the list
                while current_node != self.tail:
                    # move to the next node
                    current_node = current_node.next
                    # compare the value of the current node to max_value
                    if current_node.value > max_val:
                        # if the node's value is greater, set max_value to that value
                        max_val = current_node.value

                # return max_value
                return max_val
            return 0
