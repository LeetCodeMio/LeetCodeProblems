# 模拟下雨 用并查集表示水坑
# 格点由低到高进入并查集 起终点进入同一水坑即可
class Solution :
	def swimInWater(self, grid) :
		N = len(grid)
		connect = lambda i,j : ((i+di, j+dj)
			for di,dj in zip([1,-1,0,0], [0,0,1,-1])
			if 0 <= i+di < N and 0 <= j+dj < N)
		uset = {}
		def find(node) :
			root = node
			while uset[root] != root :
				root = uset[root]
			while uset[node] != root :
				uset[node], node = root, uset[node]
			return root
		def join(a,b) : uset[find(a)] = find(b)
		grid = sorted((grid[i][j], (i,j))
			for i in range(N) for j in range(N))
		s,e = (0,0), (N-1, N-1)
		for t, node in grid :
			uset[node] = node
			for nnode in connect(*node) :
				if nnode in uset : join(nnode, node)
			if s in uset and e in uset and find(s) == find(e) :
				return t