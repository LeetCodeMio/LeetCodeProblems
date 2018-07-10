# 设立k个篮子，分别放入1~k个球
# 放入一个新球，要求篮中球数必须保持严格单增，且最后一个篮子不超过9个球
# 将所有可能得到的结果存入哈希表
# 按照相同的要求继续放球，直至球的总数为n
class Solution :
	def combinationSum3(self, k, n) :
		if n < (k+1)*k//2 : return []
		ret = set()
		ret.add(tuple(range(1, 1+k)))
		for _ in range(n - (k+1)*k//2) :
			tmp = set()
			for i in ret :
				i = list(i)
				for j in range(k-1) :
					if i[j]+1 < i[j+1] :
						i[j] += 1
						tmp.add(tuple(i))
						i[j] -= 1
				i[k-1] += 1
				if i[k-1] <= 9 : tmp.add(tuple(i))
			ret = tmp
		return [list(i) for i in ret]