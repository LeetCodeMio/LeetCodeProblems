# 排列组合数学题
# 有m-1个白球和n-1个黑球 排成一排
# 一共有C_(m-1+n-1)^(m-1)中排法
class Solution :
    def uniquePaths(self, m, n) :
    	a = min(m,n) - 1
    	b = m+n-2
    	ret = 1
    	for i in range(a) : ret *= b - i
    	for i in range(a) : ret //= a - i
    	return ret
