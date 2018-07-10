class Solution(object) :
	def findComplement(self, num) :
		ret = ''
		for i in bin(num)[2:] : ret += '0' if i == '1' else '1'
		return int(ret, 2) # 第二个参数表示ret的进制