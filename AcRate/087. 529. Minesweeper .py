class Solution :
	def updateBoard(self, board, click) :
		x, y = click
		if board[x][y] == 'M' :
			board[x][y] = 'X'
			return board
		board[x][y] = 'B'
		dxs = [0,0,1,-1,1,1,-1,-1]
		dys = [1,-1,0,0,1,-1,1,-1]
		connects = lambda x,y : ([x+dx, y+dy]
			for dx,dy in zip(dxs,dys)
			if 0 <= x+dx < len(board)
			and 0 <= y+dy < len(board[0])
			and board[x+dx][y+dy] in 'ME')
		stack = [click]
		while stack :
			x, y = stack.pop()
			M_num = sum(board[nx][ny] == 'M'
				for nx,ny in connects(x,y))
			if M_num : board[x][y] = str(M_num)
			else :
				for nx,ny in connects(x, y) :
					board[nx][ny] = 'B'
					stack.append([nx,ny])
		return board