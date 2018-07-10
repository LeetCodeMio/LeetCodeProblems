# 深度优先搜索
# 优先返回更深的节点
# 同等深度情况下优先返回左边的节点
class Solution(object) :
	def find(self, root, depth) :
		f = lambda n : self.find(n, depth+1)
		if root.left and root.right :
			l, dl = f(root.left)
			r, dr = f(root.right)
			if dl >= dr : return l, dl
			return r, dr
		if root.left : return f(root.left)
		if root.right : return f(root.right)
		return root.val, depth
	def findBottomLeftValue(self, root) :
		return self.find(root, 0)[0]