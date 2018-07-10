class Solution(object) :
	def maxAreaOfIsland(self, grid) :
		d = [[1,0],[-1,0],[0,1],[0,-1]]
		I, J = len(grid), len(grid[0])
		ans = 0
		for i in range(I) :
			for j in range(J) :
				if not grid[i][j] : continue
				stack = [[i,j]]
				grid[i][j] = 0
				area = 1
				while stack :
					x, y = stack.pop()
					for dx, dy in d :
						nx, ny = x+dx, y+dy
						if nx < 0 or nx >= I : continue
						if ny < 0 or ny >= J : continue
						if not grid[nx][ny] : continue
						stack.append([nx,ny])
						grid[nx][ny] = 0
						area += 1
				ans = max(ans, area)
		return ans