#Using Python 3

class Node:
    """
    My node class for each node in the linked list.
    Each node has a value and a next node.
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_node_value(self):
        return self.value

    def get_next_node(self):
        return self.next

    def set_next(self, new):
        self.next = new



class LinkedList:
    """
    My class for a singly linked list.
    Each list has a head.
    Nodes can be inserted.
    """

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node

    def get_length(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.get_next_node()
        return count

    def find_kth_to_last(self, k):
        curr = self.head
        count = 0
        length = self.get_length()
        while curr:
            count += 1
            if (length - k) == count:
                return curr.get_node_value()
            else:
                curr = curr.get_next_node()

        return None


#My Testing
#l = LinkedList()
#l.insert(5)
#l.insert(6)
#print (l.get_length())
#print(l.find_kth_to_last(0))
