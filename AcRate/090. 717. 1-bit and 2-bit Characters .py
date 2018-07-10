class Solution :
	def isOneBitCharacter(self, bits) :
		i = 0
		while i < len(bits) :
			ret = bits[i]
			i += 2 if ret else 1
		return not ret