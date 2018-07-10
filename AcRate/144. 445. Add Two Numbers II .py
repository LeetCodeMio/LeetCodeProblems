class Solution :
	def addTwoNumbers(self, l1, l2) :
		def toInt(l) :
			ret = 0
			node = l
			while node :
				ret = ret*10 + node.val
				node = node.next
			return ret
		ret = ListNode(None)
		node = ret
		for i in str(toInt(l1) + toInt(l2)) :
			if node.val is not None :
				node.next = ListNode(None)
				node = node.next
			node.val = int(i)
		return ret