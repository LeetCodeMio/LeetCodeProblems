class Solution :
	def largeGroupPositions(self, S) :
		ret = []
		last = 0
		for i in range(1, len(S)+1) : # 注意边界case
			if i == len(S) or S[i] != S[last] :
				if i - last >= 3 : ret.append([last, i-1])
				last = i
		return ret