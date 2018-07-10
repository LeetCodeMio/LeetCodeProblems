class Solution :
	def exclusiveTime(self, n, logs) :
		ret = [0] * n
		stack = [] # [[id,exe_time,recent_start_time],...]
		for log in logs :
			i, flag, t = log.split(':')
			i,t = int(i), int(t)
			if flag == 'start' :
				if stack : stack[-1][1] += t - stack[-1][2]
				stack.append([i, 0, t])
			else :
				t += 1
				li, lt, ls = stack.pop()
				ret[li] += lt + t - ls
				if stack : stack[-1][2] = t
		return ret