class Solution :
	def checkRecord(self, s) :
		A = s.find('A')
		if A != -1 and s[A+1:].find('A') != -1 : return False
		return not('LLL' in s)