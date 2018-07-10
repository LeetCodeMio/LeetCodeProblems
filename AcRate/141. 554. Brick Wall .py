from collections import Counter
class Solution :
	def leastBricks(self, wall) :
		for row in wall :
			for i in range(1, len(row)) :
				row[i] += row[i-1]
		c = Counter(i for row in wall for i in row).most_common(2)
		return len(wall) - (c[1][1] if len(c) > 1 else 0)