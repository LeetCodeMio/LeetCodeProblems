# 小数字的位置不会影响大数字的相对位置
# 所以要先确定大数字的相对位置
# 对于相同大小的数字 先确定k小者的相对位置
from operator import itemgetter as ig
class Solution(object) :
	def reconstructQueue(self, people) :
		people.sort(key= ig(1))
		people.sort(key= ig(0), reverse= True)
		ret = []
		for i in people : ret.insert(i[1], i)
		return ret