class Solution :
	def imageSmoother(self, M) :
		dxs = [0,1,-1,0,0,1,-1,1,-1]
		dys = [0,0,0,1,-1,1,1,-1,-1]
		X,Y = len(M), len(M[0])
		sample = lambda x,y : [(x+dx, y+dy)
			for dx,dy in zip(dxs,dys)
			if 0 <= x+dx < X and 0 <= y+dy < Y]
		ret = [[0 for y in range(Y)] for x in range(X)]
		for x in range(X) :
			for y in range(Y) :
				s = sample(x,y)
				ret[x][y] = sum(M[nx][ny] for nx,ny in s) // len(s)
		return ret