class Solution : # 动态规划
	def diffWaysToCompute(self, string) :
		dic = {'+':int.__add__, '-':int.__sub__, '*':int.__mul__}
		num, op, start = [], [], 0
		for i,x in enumerate(string) :
			if x in dic :
				num.append(int(string[start:i]))
				start = i+1
				op.append(dic[x])
		num.append(int(string[start:]))
		res = {(i,i):[x] for i,x in enumerate(num)}
		for j in range(1, len(num)) :
			for i in reversed(range(j)) :
				res[(i,j)] = [op[i+l](a,b) for l in range(j-i)
					for a in res[(i, i+l)] for b in res[(i+l+1, j)]]
		return res[(0, len(num)-1)]