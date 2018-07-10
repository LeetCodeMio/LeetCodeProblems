# 并查集
class Solution :
	def findCircleNum(self, M) :
		ran = range(len(M))
		uset = [i for i in ran]
		def root(i) :
			stack = []
			while uset[i] != i :
				stack.append(i)
				i = uset[i]
			for j in stack : uset[j] = i
			return i
		for i in ran :
			for j in ran :
				if M[i][j] : uset[root(j)] = root(i)
		for i in ran : uset[i] = root(i)
		return len(set(uset))