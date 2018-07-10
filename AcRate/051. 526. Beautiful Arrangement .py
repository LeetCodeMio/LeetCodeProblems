# 深度优先搜索
class Solution(object) :
	def count(self, places, elements) :
		if not elements : return 1
		ret = 0
		element = elements.pop()
		for place in places :
			if place % element and element % place : continue
			places.remove(place)
			ret += self.count(places.copy(), elements.copy())
			places.add(place)
		return ret
	def countArrangement(self, N) :
		places = set(range(1, N+1))
		elements = list(range(1, N+1))
		return self.count(places, elements)