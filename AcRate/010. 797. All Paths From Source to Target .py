class Solution(object) :
	def allPathsSourceTarget(self, graph) :
		target = len(graph) - 1
		able = [True] * len(graph)
		# 发现node无法到达target后 able[node]==False 剪枝
		ans = []
		def find_way(node0, way) :
			if node0 == target :
				ans.append(way)
				return True
			tmp = [find_way(node, way + [node])
				for node in graph[node0] if able[node]]
			if any(tmp) : return True
			able[node0] = False
			return False
		find_way(0, [0])
		return ans