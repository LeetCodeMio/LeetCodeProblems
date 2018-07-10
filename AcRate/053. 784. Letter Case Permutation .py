# 深度优先搜索
class Solution(object) :
	def search(self, S, prev, i) :
		if i == len(S) :
			self.ans.append(prev)
			return
		if S[i].isdigit() : self.search(S, prev+S[i], i+1)
		else :
			self.search(S, prev+S[i].lower(), i+1)
			self.search(S, prev+S[i].upper(), i+1)
	def letterCasePermutation(self, S) :
		self.ans = []
		self.search(S, '', 0)
		return self.ans