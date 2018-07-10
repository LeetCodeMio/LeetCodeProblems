class Solution(object) :
	def fizzBuzz(self, n) :
		ret = [str(i) for i in range(n+1)]
		for i in range(0, n+1, 3) : ret[i] = 'Fizz'
		for i in range(0, n+1, 5) :
			ret[i] = 'FizzBuzz' if ret[i] == 'Fizz' else 'Buzz'
		return ret[1:]