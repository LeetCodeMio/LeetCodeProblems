# 储存26个字母在s中出现的位置 升序排列
# 对d中的word做判断时 先查word[1]首次出现位置i1
# 再查word[2]的首次出现位置i2 但要求i2>i1 用二分查找
# 如此往复 看能不能将word的元素都查到
from bisect import bisect
from collections import defaultdict
class Solution : # 二分查找优化
	def findLongestWord(self, s, d) :
		ret = (0, '')
		appear = defaultdict(list)
		for i,x in enumerate(s) :
			appear[x].append(i)
		for word in d :
			bound = -1
			for c in word :
				if c not in appear : break
				pos = appear[c]
				find = bisect(pos, bound)
				if find == len(pos) : break
				bound = pos[find]
			else : ret = min(ret, (-len(word), word))
		return ret[1]
