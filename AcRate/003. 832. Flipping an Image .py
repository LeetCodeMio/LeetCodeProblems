class Solution(object) :
	def flipAndInvertImage(self, A) :
		return [[int(not j) for j in i.__reversed__()] for i in A]