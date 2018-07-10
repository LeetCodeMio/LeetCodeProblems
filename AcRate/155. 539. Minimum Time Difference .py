class Solution :
	def findMinDifference(self, timePoints) :
		time = []
		for i in timePoints :
			h,m = map(int, i.split(':'))
			time.append(h*60 + m)
		time.sort()
		ret = min(time[i+1] - time[i] for i in range(len(time) - 1))
		return min(ret, time[0] + 24*60 - time[-1])