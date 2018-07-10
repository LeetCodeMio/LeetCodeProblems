class Solution(object) :
	def shortestToChar(self, S, C) :
		ans = [0] * len(S)
		last = S.find(C)
		# 第一个C前的ans
		for i in range(last) : ans[i] = last - i
		# 只考虑左近邻C时的ans
		for i in range(last, len(S)) :
			if S[i] == C : last = i
			ans[i] = i - last
		# 再考虑上右近邻C时的ans
		for i in range(last).__reversed__() :
			if S[i] == C : last = i
			ans[i] = min(ans[i], last - i)
		return ans