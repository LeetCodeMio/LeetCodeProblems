class Solution :
	def backspaceCompare(self, S, T) :
		def edit(s) :
			ret = []
			for i in s :
				if i == '#' :
					if ret : ret.pop()
					continue
				ret.append(i)
			return ret
		return edit(S) == edit(T)