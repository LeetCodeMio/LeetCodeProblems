# def L[a][b] = 字符串A[:a]和B[:b]的最长公共子序列长度
# if A[a] == B[b] : L[a][b] = L[a-1][b-1] + 1
# if A[a] != B[b] : L[a][b] = max(L[a-1][b], L[a][b-1])
# with L[0][b] == L[a][0] == 0
class Solution : # 最长公共子序列 动态规划
	def minDistance(self, A, B) :
		L = [0] * (len(B) + 1)
		Ltmp = L.copy()
		for a,Aa in enumerate(A, 1) :
			for b,Bb in enumerate(B, 1) :
				Ltmp[b] = L[b-1] + 1 if Aa == Bb else max(L[b], Ltmp[b-1])
			L, Ltmp = Ltmp, L
		return len(A) + len(B) - L[len(B)] * 2