class Solution :
	def getImportance(self, employees, ID0) :
		info = {} # id:[importance,subordinates]
		for i in employees :
			info[i.id] = [i.importance, i.subordinates]
		stack = [ID0]
		ans = 0
		while stack :
			importance, subordinates = info[stack.pop()]
			ans += importance
			stack += subordinates
		return ans