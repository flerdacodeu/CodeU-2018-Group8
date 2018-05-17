class Node():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList():
    def __init__(self, a=None):
        self.first = None
        if a is None:
            return
        self.first = Node(a[0])
        now = self.first
        for value in a[1:]:
            now.next = Node(value)
            now = now.next

    def find_kth_to_last(self, k=0):
        len = 0
        now = self.first
        while now is not None:
            len += 1
            now = now.next
        assert(k < len)
        now = self.first
        for _ in range(len - k - 1):
            now = now.next
        return now.value


a = list(map(int, input().split()))
linked_list = SinglyLinkedList(a)
k = int(input())
print(linked_list.find_kth_to_last(k))