from collections import Counter
from math import ceil
class Solution :
	def numRabbits(self, answers) :
		return sum(ceil(v / (k+1)) * (k+1)
			for k,v in Counter(answers).items())