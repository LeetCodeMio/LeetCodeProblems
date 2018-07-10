class Solution : # 双指针
	def magicalString(self, n) :
		S = [None] * (n+5) # 1:True 2:False
		S[0], S[1] = True, False
		flag = False
		a,b = 1,1
		while b < n :
			if S[a] :
				S[b] = flag
				b += 1
			else :
				S[b], S[b+1] = flag, flag
				b += 2
			flag = not flag
			a += 1
		return sum(S[:n])