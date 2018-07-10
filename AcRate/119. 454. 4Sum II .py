# 先分别计算A+B和C+D可能得到的结果及方法数
from collections import Counter as ct
class Solution :
	def fourSumCount(self, A, B, C, D) :
		AB = ct(a+b for a in A for b in B)
		CD = ct(c+d for c in C for d in D)
		return sum(AB[i] * CD[-i] for i in AB if -i in CD)