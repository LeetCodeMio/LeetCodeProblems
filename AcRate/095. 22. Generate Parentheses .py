# 遍历合法的出栈方式
class Solution :
	def generateParenthesis(self, n) :
		ret = [('', 0)]
		for i in range(n*2) :
			tmp = []
			for bra,depth in ret :
				if depth : tmp.append((bra + ')', depth-1))
				if depth < n*2-i : tmp.append((bra + '(', depth+1))
			ret = tmp
		return [bra for bra,depth in ret]