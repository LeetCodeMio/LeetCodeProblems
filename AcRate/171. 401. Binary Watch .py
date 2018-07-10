from itertools import combinations as cb
class Solution :
	def readBinaryWatch(self, num) :
		t = [8,4,2,1,32,16,8,4,2,1]
		ret = []
		for i in cb(range(10), num) :
			h,m = 0,0
			for j in i :
				if j < 4 : h += t[j]
				else : m += t[j]
			if h >= 12 or m >= 60 : continue
			ret.append(str(h) + ':' + str(m).zfill(2))
		return ret