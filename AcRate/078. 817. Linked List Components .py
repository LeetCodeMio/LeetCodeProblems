class Solution :
	def numComponents(self, head, G) :
		G = set(G)
		ret = 0
		while head :
			if head.val in G :
				ret += 1
				while head and head.val in G :
					head = head.next
			else : head = head.next
		return ret