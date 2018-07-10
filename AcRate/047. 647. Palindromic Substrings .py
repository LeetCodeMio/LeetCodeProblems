# 动态规划
class Solution(object) :
	def countSubstrings(self, s) :
		odd = list(range(len(s))) # 长度为1的回文串中心坐标
		ans = len(odd)
		for l in range(1, (len(s)+1) // 2) :
			_odd = [] # 长度为l+1+l的回文串中心坐标
			for i in odd :
				if i-l < 0 or i+l >= len(s) : continue
				if s[i-l] == s[i+l] :
					_odd.append(i)
					ans += 1
			if _odd == [] : break
			odd = _odd
		even = [i for i in range(len(s)-1) if s[i] == s[i+1]]
		# 长度为2的回文串中心坐标
		ans += len(even)
		for l in range(1, len(s) // 2) :
			_even = [] # 长度为l+2+l的回文串中心坐标
			for i in even :
				if i-l < 0 or i+1+l >= len(s) : continue
				if s[i-l] == s[i+1+l] :
					_even.append(i)
					ans += 1
			if _even == [] : break
			even = _even
		return ans