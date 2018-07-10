# 先对节点排序
from operator import attrgetter as ag
class Solution :
	def convertBST(self, root) :
		if not root : return root
		nodes = []
		stack = [root]
		while stack :
			nodes.append(stack.pop())
			if nodes[-1].left : stack.append(nodes[-1].left)
			if nodes[-1].right : stack.append(nodes[-1].right)
		nodes.sort(key = ag('val'), reverse = True)
		for i in range(1, len(nodes)) :
			nodes[i].val += nodes[i-1].val
		return root