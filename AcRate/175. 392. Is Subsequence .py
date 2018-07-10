class Solution : # 双指针
	def isSubsequence(self, s, t) :
		j = -1
		for i in s :
			j = t.find(i, j+1)
			if j == -1 : return False
		return True

# Follow up :
# 用26个数组分别储存26个字母在t中出现的位置 升序排列
# 对s做判断时 先查s[1]首次出现位置i1
# 再查s[2]的首次出现位置i2 但要求i2>i1 用二分查找
# 如此往复 看能不能将s的元素都查到