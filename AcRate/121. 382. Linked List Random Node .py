from random import randint
class Solution :
	def __init__(self, head) :
		node = head
		l = 1
		while node.next :
			l += 1
			node = node.next
		self.head = head
		self.l = l
	def getRandom(self) :
		step = randint(0, self.l-1)
		node = self.head
		while step :
			step -= 1
			node = node.next
		return node.val