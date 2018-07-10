class Solution :
	def findRestaurant(self, list1, list2) :
		list1 = {x:i for i,x in enumerate(list1)}
		list2 = {x:i for i,x in enumerate(list2)}
		ret, m = [], len(list1) + len(list2)
		for x in list1 :
			if x not in list2 : continue
			s = list1[x] + list2[x]
			if s == m : ret.append(x)
			elif s < m : ret, m = [x], s
		return ret