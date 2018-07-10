from collections import deque
class Solution : # 广度优先搜索 哈希判重
	def slidingPuzzle(self, board) :
		board = [j for i in board for j in i]
		connect = [[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]
		final = (1,2,3,4,5,0)
		vis = set(tuple(board))
		queue = deque([(board, board.index(0), 0)])
		while queue :
			board, start, step = queue.popleft()
			if tuple(board) == final : return step
			for end in connect[start] :
				new = board.copy()
				new[start], new[end] = new[end], new[start]
				if tuple(new) in vis : continue
				vis.add(tuple(new))
				queue.append((new, end, step+1))
		return -1