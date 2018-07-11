from collections import Counter
class Solution : # 其实括号表达式计算都可以用栈来做 尽量别用递归吧
	def countOfAtoms(self, formula) :
		def f(form) :
			ret = Counter()
			if form[0] != '(' :
				end = len(form)
				for i in reversed(range(len(form))) :
					if not form[i].isupper() : continue
					atom = form[i:end]
					end = i
					num = ''.join(j for j in atom if j.isdigit())
					if num :
						atom = atom[:-len(num)]
						num = int(num)
					else : num = 1
					ret[atom] = num
				return ret
			coe = form[form.rfind(')') + 1:]
			form = form[1:form.rfind(')')]
			end = len(form)
			bracket = 0
			for i in reversed(range(len(form))) :
				if form[i] == ')' : bracket += 1; continue
				if form[i] == '(' : bracket -= 1
				if bracket : continue
				if form[i] == '(' or form[i].isupper() :
					ret.update(f(form[i:end]))
					end = i
			if coe :
				coe = int(coe)
				for i in ret : ret[i] *= coe
			return ret
		return ''.join(k + str(v) if v > 1 else k
			for k,v in sorted(f('(' + formula + ')').items()))
