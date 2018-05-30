#Using Python 3

class Node:
    """
    My node class for each node in the linked list.
    Each node has a value and a next node.
    """
    def __init__(self, value=None, next=None):
        """
        Initialises a node with a value and a next node which is set to None.
        """
        self.value = value
        self.next = next

    def get_node_value(self):
        """
        Returns the value of a node.
        """
        return self.value

    def get_next_node(self):
        """
        Returns the next node.
        """
        return self.next

    def set_next(self, new):
        """
        Sets next node of a node to new.
        """
        self.next = new



class LinkedList:
    """
    My class for a singly linked list.
    Each list has a head.
    Nodes can be inserted by using the insert method after initialising a linked list.
    """

    def __init__(self, head=None):
        """
        Initialises an empty linked list object with head set to None and length set to 0.
        """
        self.head = head
        self.length = 0

    def insert(self, value):
        """
        Inserts a node into the linked listself.
        Sets next node of new node to the head of the list.
        Sets the new node to the head of the list.
        Adds 1 to the length of the list.
        """
        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node
        self.length += 1

    def get_length(self):
        """
        Gets the length of the list.
        """
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.get_next_node()
        return count

    def find_kth_to_last(self, k):
        """
        Finds the kth to last element of the linked list.
        """
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
