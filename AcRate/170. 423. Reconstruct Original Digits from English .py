# zore z
# two w
# four u
# six x
# eight g
# one-o
# three-t
# five-f
# seven-s
# nine~i
from collections import Counter
class Solution :
	def originalDigits(self, s) :
		s = Counter(s)
		n = [0] * 10
		n[0] = s['z']
		n[2] = s['w']
		n[4] = s['u']
		n[6] = s['x']
		n[8] = s['g']
		n[1] = s['o'] - n[0] - n[2] - n[4]
		n[3] = s['t'] - n[2] - n[8]
		n[5] = s['f'] - n[4]
		n[7] = s['s'] - n[6]
		n[9] = s['i'] - n[6] - n[8] - n[5]
		return ''.join(str(i) * n[i] for i in range(10))