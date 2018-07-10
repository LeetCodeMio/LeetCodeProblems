class Solution	:
	def findPoisonedDuration(self, t, d) :
		if not t : return 0
		return d + sum(min(d, t[i+1] - t[i]) for i in range(len(t)-1))