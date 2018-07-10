class Solution :
	def tree2str(self, t) :
		def f(t) :
			if not t : return ''
			ret = '(' + str(t.val) + f(t.left)
			if not t.left and t.right : ret += '()'
			return ret + f(t.right) + ')'
		return f(t)[1:-1]