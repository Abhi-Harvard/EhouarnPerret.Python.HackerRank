"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
	# e.g. A > B > C > D
	if head:
		current = head				# current = A
		next = current.next 		# next = A.next = B
		current.next = None			# A > None
		while next:					
			tmp = next.next			# tmp = B.next = C
			next.next = current		# B.next = current = A
			head = current = next 	# head = current = B
			next = tmp				# next = tmp = C
	return head

def Stack_Reverse(head):
	# e.g. A > B > C > D
	if head:
		stack = [head]
		while stack[-1].next:
			node = stack[-1]
			stack.append(node.next)
		# stack = [D, C, B, A]
		head = stack.pop()	# head = D
		current = head		# current = head = D
		while stack:
			node = stack.pop()	#
			current.next = node
			current = current.next
		current.next = None
	return head

def Recursive_Reverse(head):
	if not head:
		return head
	else:
		head = Recursive_Reverse(head.next)
		head.next
	return head