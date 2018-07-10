class Solution :
	def minimumDeleteSum(self, A, B) :
		ret = 0 # 最长公共子序列串ascii和
		l = [0] * len(B) # 以ab作为AB结尾 的最长公共子序列ascii和
		tmp_l = l.copy()
		for a in range(len(A)) :
			for b in range(len(B)) :
				if A[a] != B[b] : tmp_l[b] = max(l[b], tmp_l[b-1]) if b else l[b]
				else : tmp_l[b] = l[b-1] + ord(B[b]) if b else ord(B[b])
				ret = max(ret, tmp_l[b])
			l, tmp_l = tmp_l, l
		return sum(ord(a) for a in A) + sum(ord(b) for b in B) - ret*2