# 动态规划
# 先遍历找出长度为3的slice的起始下标和公差
# 长度为4的slice必然是长度为3的slice再添加一个等差元素得到
# 如此反复 得到所有长度的slice 返回计数
class Solution(object) :
	def numberOfArithmeticSlices(self, A) :
		ans = 0
		arithmetic = [] # 元素为 [slice的起始下标,公差]
		for i in range(len(A)-2) : # 找出长度为3的slice
			if A[i] + A[i+2] == A[i+1] * 2 :
				arithmetic.append([i, A[i+1] - A[i]])
				ans += 1
		for l in range(3, len(A)) : # 找出长度为l+1的slice
			tmp = []
			while len(arithmetic) :
				i, d = arithmetic.pop()
				if i + l >= len(A) : continue
				if A[i+l] - A[i+l-1] != d : continue
				tmp.append([i, d])
				ans += 1
			arithmetic = tmp
		return ans