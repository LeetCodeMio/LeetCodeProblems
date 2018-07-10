class Solution :
	def escapeGhosts(self, ghosts, target) :
		tx, ty = target
		l = abs(tx) + abs(ty)
		for gx, gy in ghosts :
			if abs(gx - tx) + abs(gy - ty) <= l :
				return False
		return True