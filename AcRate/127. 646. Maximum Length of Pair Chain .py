# 先将pairs按second元素从小到大排序
# 首先 第一个pair使用pairs[0]肯定能构造出最优解
# 因为任给一个最优解 将它的第一个pair替换为pairs[0]仍然是最优解
# 将pairs[0]选为第一个pair后
# 在剩下的可合法链接的pairs中 使用second最小的一定能构造出最优解
# 因为假设选择了别的pair构造出了最优解
# 将它替换为second最小的pair仍然是最优解
from operator import itemgetter as ig
class Solution :
	def findLongestChain(self, pairs) :
		pairs.sort(key = ig(1))
		ret = 0
		p = pairs[0][0] - 1
		for a,b in pairs :
			if a > p :
				p = b
				ret += 1
		return ret