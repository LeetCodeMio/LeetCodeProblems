from math import gcd
class Solution : # 数学公式
	def mirrorReflection(self, p, q) :
		lcm = p*q // gcd(p,q)
		return (lcm//p) % 2 if (lcm//q) % 2 else 2