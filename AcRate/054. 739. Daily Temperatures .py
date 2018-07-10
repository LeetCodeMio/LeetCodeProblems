# 从后往前扫描有奇效
class Solution(object) :
	def dailyTemperatures(self, t) :
		ans = [0] * len(t)
		stack = [] # 从顶到底为当前扫描位置到末尾的严格单增子序列坐标
		for date in range(len(t)).__reversed__() :
			while len(stack) and t[date] >= t[stack[-1]] : stack.pop()
			if len(stack) : ans[date] = stack[-1] - date
			stack.append(date)
		return ans