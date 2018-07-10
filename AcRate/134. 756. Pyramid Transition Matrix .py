# 深度优先搜索
from itertools import product
class Solution :
	def pyramidTransition(self, bottom, allowed) :
		triples = {}
		for a,b,c in allowed :
			triples.setdefault((a,b), set()).add(c)
		stack = [bottom]
		while stack :
			line = stack.pop()
			if len(line) == 1 : return True
			if not all((line[i], line[i+1]) in triples
				for i in range(len(line)-1)) : continue
			stack.extend(product(*(triples[(line[i], line[i+1])]
				for i in range(len(line)-1))))
		return False