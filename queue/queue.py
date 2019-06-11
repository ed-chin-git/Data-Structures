class Node:
    '''
          Node Class
    '''
    def __init__(self, item=None):
        self.next = None
        self.prev = None
        self.item = item


class Queue:
    '''
      Queue Class
    '''
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        #  as per guided practice - single linked_list
        self.head = None
        self.tail = None

    def enqueue(self, item):
        no_de = Node(item)
        hold = self.head
        if hold is not None:
            hold.prev = no_de
        no_de.next = hold
        no_de.prev = None
        self.head = no_de
        if hold is None:
            self.tail = self.head
        self.size += 1

    def dequeue(self):
        if self.tail is None:
            return None
        no_de = self.tail
        if no_de.prev is None:
            self.head = None
            self.tail = None
        else:
            self.tail = no_de.prev
        self.size -= 1
        return no_de.item

    def len(self):
        return self.size