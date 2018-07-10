class Solution :
	def findTheDifference(self, s, t) :
		ret = {}
		for i in t :
			if i in ret : ret[i] += 1
			else : ret[i] = 1
		for i in s :
			ret[i] -= 1
			if not ret[i] : del(ret[i])
		return ret.popitem()[0]