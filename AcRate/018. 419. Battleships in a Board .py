# 只读地扫描一次board且空间复杂度O(1)的解法
class Solution(object) :
	def countBattleships(self, board) :
		ans = 0
		for r in range(len(board)) :
			for c in range(len(board[0])) :
				if board[r][c] != 'X' : continue
				if r != 0 and board[r-1][c] != '.' : continue
				if c != 0 and board[r][c-1] != '.' : continue
				ans += 1
		return ans