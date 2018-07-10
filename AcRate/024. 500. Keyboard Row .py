class Solution(object) :
	def findWords(self, words) :
		s1 = set('qwertyuiopQWERTYUIOP')
		s2 = set('asdfghjklASDFGHJKL')
		s3 = set('zxcvbnmZXCVBNM')
		return [i for i in words
			if set(i).issubset(s1)
			or set(i).issubset(s2)
			or set(i).issubset(s3)]