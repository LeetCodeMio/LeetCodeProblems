# 将nums2放入优先队列
# 放入元素i前将比i小的取出
# 并将其Next Greater Number记为i
import queue
class Solution(object) :
	def nextGreaterElement(self, findNums, nums) :
		ret = {}
		pq = queue.PriorityQueue()
		for i in nums :
			pq.put(i)
			while pq.queue[0] < i :
				ret.update({pq.get(): i})
		while not pq.empty() :
			ret.update({pq.get(): -1})
		return [ret[i] for i in findNums]