class Solution(object) :
	def islandPerimeter(self, grid) :
		I, J = len(grid), len(grid[0])
		def border(i, j) :
			ret = 4
			if i != 0 and grid[i-1][j] : ret -= 1
			if i+1 != I and grid[i+1][j] : ret -= 1
			if j != 0 and grid[i][j-1] : ret -= 1
			if j+1 != J and grid[i][j+1] : ret -= 1
			return ret
		return sum(border(i, j)
			for i in range(I)
			for j in range(J)
			if grid[i][j])