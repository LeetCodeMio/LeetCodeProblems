from fractions import Fraction
class Solution :
	def fractionAddition(self, exp) :
		exp = exp.replace('+', ' +')
		exp = exp.replace('-', ' -')
		ret = sum(map(Fraction, exp.split()))
		return str(ret.numerator) + '/' + str(ret.denominator)