# 回溯搜索
class Solution :
	def totalNQueens(self, n) :
		vis = [[None] * n for _ in range(n)]
		def flip(i0, j0, a, b) :
			for d,i in enumerate(range(i0+1, n), 1) :
				for j in (j0-d, j0, j0+d) :
					if 0 <= j < n and vis[i][j] == a :
						vis[i][j] = b
		stack = [0]
		ret = 0
		while True :
			i, j = len(stack)-1, stack[-1]
			if i == n :
				ret += 1
				j = n
			if j == n :
				stack.pop()
				if not stack : return ret
				flip(i-1, stack[-1], i-1, None)
				stack[-1] += 1
				continue
			if vis[i][j] is not None :
				stack[-1] += 1
				continue
			flip(i, j, None, i)
			stack.append(0)