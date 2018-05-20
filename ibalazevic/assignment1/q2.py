class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def find_kth_to_last(head, k):
	p1 = head
	p2 = head
	i = 0
	if not head:
		return None
	while(p1):
		p1 = p1.next
		if i > k:
			p2 = p2.next
		i += 1
	return p2.data
