# 用有序的{时间节点:该节点之后的book数}来保存日程表即可

# SortedDict是更优的解法 不过不是Python标准库
# from sortedcontainers import SortedDict
# class MyCalendarThree :
# 	def __init__(self) :
# 		self.k = 0 # 最大book数
# 		self.dic = SortedDict() # 时间节点:该节点之后的book数
# 	def book(self, start, end) :
# 		def insert(time) :
# 			if time in self.dic : return
# 			index = self.dic.bisect(time)
# 			self.dic[time] = self.dic.values()[index-1] if index else 0
# 		insert(start)
# 		insert(end)
# 		for key in self.dic.irange(start, end, (True,False)) :
# 			self.dic[key] += 1
# 			self.k = max(self.k, self.dic[key])
# 		return self.k

from bisect import bisect_left
class MyCalendarThree :
	def __init__(self) :
		self.k = 0 # 最大book数
		self.time = []
		self.books = []
	def book(self, start, end) :
		def insert(time) :
			index = bisect_left(self.time, time)
			if index < len(self.time) and self.time[index] == time : return index
			self.time.insert(index, time)
			self.books.insert(index, self.books[index-1] if index else 0)
			return index
		s = insert(start)
		e = insert(end)
		for i in range(s, e) :
			self.books[i] += 1
			self.k = max(self.books[i], self.k)
		return self.k