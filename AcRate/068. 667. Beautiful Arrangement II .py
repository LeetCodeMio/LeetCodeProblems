class Solution :
	def constructArray(self, n, k) :
		ret = [0] * n
		for i in range(k) : ret[i] = n - i // 2 if i % 2 else i // 2 + 1
		for i in range(k, n) : ret[i] = ret[i-1] + 1 if k % 2 else ret[i-1] - 1
		return ret