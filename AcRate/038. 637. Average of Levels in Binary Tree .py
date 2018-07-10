class Solution(object) :
	def __init__(self) :
		self.ret = [] # 各层节点和
		self.num = [] # 各层节点数
	def calc(self, root, h) :
		if h >= len(self.ret) :
			self.ret.append(0)
			self.num.append(0)
		self.ret[h] += root.val
		self.num[h] += 1
		if root.left : self.calc(root.left, h+1)
		if root.right : self.calc(root.right, h+1)
	def averageOfLevels(self, root) :
		self.calc(root, 0)
		return [self.ret[i] / self.num[i]
			for i in range(len(self.ret))]