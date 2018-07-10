class Solution :
	def splitListToParts(self, root, k) :
		node = root
		l = 0
		while node :
			l += 1
			node = node.next
		a, b = l // k, l % k
		ret = [None] * k
		def split(node, n) :
			for j in range(n-1) :
				if node : node = node.next
				else : return node
			if node :
				tmp = node.next
				node.next = None
				return tmp
		node = root
		for i in range(b) :
			ret[i] = node
			node =  split(node, a+1)
		for i in range(b, k) :
			ret[i] = node
			node = split(node, a)
		return ret