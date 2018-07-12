# f[a][b] =def= 区间[a,b]内的回文子串最大长度
# f[a][b] = f[a+1][b-1] + 2 if s[a] == s[b]
# f[a][b] = max(f[a+1][b], f[a][b-1]) if s[a] != s[b]
# f[a][a] = 1, f[a][a+1] = 2 if s[a] == s[a+1] else 1
# 求 f[0][len(s)-1]
class Solution : # 动态规划
	def longestPalindromeSubseq(self, s) :
		if not s : return 0 # 角落
		if s == s[::-1] : return len(s) # 加速
		f = [[None for a in s] for b in s]
		for a in range(len(s)) : f[a][a] = 1
		for a in range(len(s) - 1) :
			f[a][a+1] = 2 if s[a] == s[a+1] else 1
		for l in range(2, len(s)) :
			for a,b in zip(range(len(s)), range(l, len(s))) :
				f[a][b] = (f[a+1][b-1] + 2 if s[a] == s[b]
					else max(f[a+1][b], f[a][b-1]))
		return f[0][len(s) - 1]
