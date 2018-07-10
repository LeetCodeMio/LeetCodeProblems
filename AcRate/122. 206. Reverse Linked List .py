class Solution :
	def reverseList(self, head) :
		if not head : return head
		node = head
		prev = None
		while True :
			tmp = node.next
			node.next = prev
			prev = node
			if tmp : node = tmp
			else : break
		return node