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
        # check to see if we have anything in the list already.
        # if not
            # set both the head and tail to the new node
        # if we do
            # set the lists head as the new node's next
            # set the new node as the lists head's prev
            # set the new node as the lists head
        pass

    def remove_from_head(self):
        # make sure we have items in the list
            # if we don't return None
        # if we do, see if we have only one element
            # if that is the case
                # get the value of head
                # set head and tail to None
                # return value of head
        # if there's more than one element
            # get a new reference to the current head node
            # set self.head to the current head's next node
            # set self.head's prev node to None
            # return reference to the former head
        pass

    def add_to_tail(self, value):
        # wrap input value in new node
        # check to see if we have anything in the list already.
        # if not
            # set both the head and tail to the new node
        # if we do
            # set the lists tail as the new node's prev
            # set the new node as the lists tails's next
            # set the new node as the lists tail
        pass

    def remove_from_tail(self):
        # make sure we have items in the list
            # if we don't return None
        # if we do, see if we have only one element
            # if that is the case
                # get the value of tail
                # set head and tail to None
                # return value of tail
        # if there's more than one element
            # get a new reference to the current tail node
            # set self.tail to the current tail's prev node
            # set self.tail's next node to None
            # return reference to the former tail
        pass

    def move_to_front(self, node):
        # make sure there is more than one item in the list
        # if there is set a reference to the selected node
        # set the next node's prev to the current node's prev
        # set the prev node's next as the current node's next

        # Would it suffice to copy the value and add to head?
        # Assuming it wouldn't

        # set the referenced node as the current heads prev
        # set the referenced nodes next as the current head
        # set the referenced nodes prev to None
        # set self.head as the referenced node
        pass

    def move_to_end(self, node):
        # make sure there is more than one item in the list
        # if there is set a reference to the selected node
        # set the next node's prev to the current node's prev
        # set the prev node's next as the current node's next

        # Would it suffice to copy the value and add to tail?
        # Assuming it wouldn't

        # set the referenced node as the current tails next
        # set the referenced nodes prev as the current tail
        # set the referenced nodes next to None
        # set self.tail as the referenced node
        pass

    def delete(self, node):
        # make a reference to the selected node
        # check to see if the selected node is the head or tail
        # if it is the head
            # set self.head to the next node
            # set self.head's prev to None
            # return selected.value
        # if it is the tail
            # set self.tail to the prev node
            # set self.tail's next to None
            # return selected value
        #
        pass

    def get_max(self):
        # make sure there are items in the list
        # set a max_value variable to track and compare the values
        # while we are not at the end of the list
        # compare the value of the current node to max_value
        # if the node's value is greater, set max_value to that value
        # return max_value
        pass
