# 广度优先遍历
class Solution(object) :
	def largestValues(self, root) :
		queue = [root] if root else []
		ret = []
		while len(queue) :
			ret.append(max(n.val for n in queue))
			tmp = [n.left for n in queue if n.left]
			queue = tmp + [n.right for n in queue if n.right]
		return ret