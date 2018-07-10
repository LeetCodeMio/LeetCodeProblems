# a/b/c/d/e/... = a * 1/b * 1/c * 1/d * 1/e * ...
# 添加括号可以将若干 1/k 翻正为 k
# 对于正整数 必有 k >= 1/k
# 所以要尽可能多地翻正
# 易知 1/b 不可能翻正
# 于是存在唯一的加括号方法把 1/b 之后的全部翻正
# 就是 a/(b/c/d/e/...)
class Solution(object) :
	def optimalDivision(self, nums) :
		nums = [str(i) for i in nums]
		if len(nums) > 2 :
			nums[1] = '(' + nums[1]
			nums[-1] += ')'
		return '/'.join(nums)