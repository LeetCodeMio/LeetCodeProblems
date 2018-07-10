class Solution :
	def findTilt(self, root) :
		def tilt(node) :
			if not node : return 0, 0
			lsum, ltilt = tilt(node.left)
			rsum, rtilt = tilt(node.right)
			nsum = lsum + rsum + node.val
			ntilt = ltilt + rtilt + abs(lsum - rsum)
			return nsum, ntilt
		return tilt(root)[1]