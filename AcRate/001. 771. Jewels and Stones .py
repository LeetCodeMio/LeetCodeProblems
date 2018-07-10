class Solution(object):
	def numJewelsInStones(self, J, S):
		return sum([S.count(i) for i in J])