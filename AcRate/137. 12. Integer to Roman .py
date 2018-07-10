class Solution :
	def intToRoman(self, num) :
		pattern = {'0':'', '1':'a', '2':'aa', '3':'aaa', '4':'ab',
			'5':'b', '6':'ba', '7':'baa', '8':'baaa', '9':'ac'}
		code = ['IVX', 'XLC', 'CDM', 'M__']
		ret = []
		for i,x in enumerate(reversed(str(num))) :
			tmp = pattern[x]
			for p,r in zip('abc', code[i]) :
				tmp = tmp.replace(p, r)
			ret.append(tmp)
		return ''.join(reversed(ret))