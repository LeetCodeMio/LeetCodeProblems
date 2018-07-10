class Solution :
	def rotateString(self, A, B) :
		if len(A) != len(B) : return False
		if A == B == '' : return True
		for a in range(len(A)) :
			if A[a] != B[0] : continue
			if all(A[(a+b) % len(A)] == B[b]
				for b in range(len(B))) : return True
		return False