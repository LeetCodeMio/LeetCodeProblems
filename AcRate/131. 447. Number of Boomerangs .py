# 优化
class Solution :
	def numberOfBoomerangs(self, points) :
		dis = [{} for _ in range(len(points))]
		# dis[i] = {d:points中到points[i]的距离为d的点数}
		for a,(ax,ay) in enumerate(points) :
			for b,(bx,by) in enumerate(points[:a]) :
				d = (ax-bx)**2 + (ay-by)**2
				dis[a][d] = dis[a].setdefault(d, 0) + 1
				dis[b][d] = dis[b].setdefault(d, 0) + 1
		return sum(n*(n-1) for dic in dis for n in dic.values())