# The number of 0's is equal to the number of 1's.
# 0和1的数量相等
# Every prefix of the binary string has at least as many 1's as 0's.
# 任何前缀中 1的数量 >= 0的数量
# 分治 括号山
# 对括号山进行递归处理
# 在递归体中对已经递归处理好的子括号山按字典序降序排列
class Solution :
	def makeLargestSpecial(self, S) :
		def f(s) :
			if len(s) == 2 : return s
			ret = []
			level = 0
			start = 1
			for i in range(1, len(s) - 1) :
				level += 1 if s[i] == '1' else -1
				if level == 0 :
					ret.append(f(s[start : i+1]))
					start = i+1
			return '1' + ''.join(sorted(ret, reverse = True)) + '0'
		return f('1' + S + '0')[1:-1]