# 非递归
class Solution :
	def inorderTraversal(self, root) :
		if not root : return []
		ret = []
		stack = [[root, True]]
		while stack :
			while stack[-1][1] and stack[-1][0].left :
				stack.append([stack[-1][0].left, True])
			tmp = stack.pop()
			ret.append(tmp[0].val)
			if stack : stack[-1][1] = False
			if tmp[0].right : stack.append([tmp[0].right, True])
		return ret