class Solution(object) :
	def count(self, root) :
		if not root : return 0
		num = root.val + self.count(root.left) + self.count(root.right)
		if num in self.ans : self.ans[num] += 1
		else : self.ans[num] = 1
		return num
	def findFrequentTreeSum(self, root) :
		self.ans = {} # 子树和:频率
		self.count(root)
		print(self.ans)
		ret = []
		max_freq = 0
		for num, freq in self.ans.items() :
			if freq > max_freq : ret, max_freq = [num], freq
			elif freq == max_freq : ret.append(num)
		return ret