class Solution : # t=O(n) m=O(1) inplace
	def oddEvenList(self, head) :
		if not (head and head.next) : return head
		oddhead, oddtail = head, head
		evenhead, eventail = head.next, head.next
		while True :
			if not eventail.next : break
			oddtail.next = eventail.next
			oddtail = oddtail.next
			if not oddtail.next : break
			eventail.next = oddtail.next
			eventail = eventail.next
		oddtail.next = evenhead
		eventail.next = None
		return oddhead