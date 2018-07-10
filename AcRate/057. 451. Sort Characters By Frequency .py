from collections import Counter as ct
from operator import itemgetter as ig
class Solution(object) :
	def frequencySort(self, s) :
		s = sorted(ct(s).items(), key = ig(1),  reverse = True)
		return ''.join(k*v for k,v in s)