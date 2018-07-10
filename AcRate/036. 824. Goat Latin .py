class Solution(object) :
	def toGoatLatin(self, S) :
		S = S.split(' ')
		vowel = set('aeiouAEIOU')
		for i in range(len(S)) :
			if S[i][0] not in vowel : S[i] = S[i][1:] + S[i][0]
			S[i] += 'maa' + 'a'*i
		return ' '.join(S)