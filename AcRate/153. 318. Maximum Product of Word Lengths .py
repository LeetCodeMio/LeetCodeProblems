class Solution : # 小集合子集的集合运算 可用位运算加速
	def maxProduct(self, words) :
		flag = [1<<i for i in range(26)]
		l = [len(i) for i in words]
		s = [0] * len(words)
		off = ord('a')
		for i,word in enumerate(words) :
			for letter in word :
				s[i] |= flag[ord(letter) - off]
		return max((l[i] * l[j]
			for i in range(len(words)) for j in range(i)
			if not s[i] & s[j]), default = 0)