class Solution :
	def findDiagonalOrder(self, matrix) :
		if not matrix : return []
		M, N = len(matrix), len(matrix[0])
		ret = []
		state = 1
		i,j = 0,0
		while True :
			ret.append(matrix[i][j])
			if i == M-1 and j == N-1 : break
			if 0 <= i-state < M and 0 <= j+state < N :
				i,j = i-state, j+state
			else :
				if state == 1 :
					if j == N-1 : i += 1
					else : j += 1
				else :
					if i == M-1 : j += 1
					else : i += 1
				state *= -1
		return ret