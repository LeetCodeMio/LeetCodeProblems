# ret = x1 * x2 * ...
# x->i*(x-i) if 1<i<=x-i and i*(x-i)>=x
# 1,2,3 can't break
# 4 -> 2*2 yes
# 5 -> 2*3 yes
# 6 -> 2*4~2*2*2`no 3*3`yes
# 7 -> 2*5~2*2*3`yes 3*4~3*2*2`yes
# 8 -> 2*6~2*3*3`yes 3*5~3*2*3`yes 4*4~2*2*2*2`no
# 2*(x-2)>=x <=> x>=4    3*(x-3)>=x <=> x>=4.5
# x must break to a*b if x >= 4
# a and b must break if >= 4 ...
# untill x -> 2*2*...*3*3*...
# because 2*2*2<3*3 the num of 2 in product must < 2
class Solution :
	def integerBreak(self, n) :
		if n == 2 : return 1
		if n == 3 : return 2
		if n % 3 == 0 : return 3**(n//3) # 没有2
		elif n % 3 == 2 : return 3**(n//3) * 2 # 1个2
		return 3**(n//3 - 1) * 4 # 2个2