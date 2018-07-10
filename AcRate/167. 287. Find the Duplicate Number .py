# 循环索引 追及trick
# 指针p从0出发 按p=num[p]前进 必然进入循环 循环入口坐标就是重复的数
# 指针p1按p1=num[p1]前进 指针p2按p2=num[num[p2]]前进
# p1将以O(n)进入循环 此时p2也在循环中
# 接下来p2将在p1重新到达循环入口前追上p1 O(n)
# 设进入此时p1走了L步 那么p2走了2*L步
# 设进入循环需要L0步 循环有c步
# 那么有 2*L - L0 == L - L0 + n*c 其中n为某个整数
# <=> L == n*c
# 如果p1再走L0步 L + L0 == L0 + n*c 它将到达循环入口 O(n)
# 可以让p2在追上p1后 回到0 然后p1 p2都采取p=num[p]前进
# 那么它们将在前进L0步后在循环入口相遇
class Solution :
	def findDuplicate(self, num) :
		p1,p2 = num[0], num[num[0]]
		while p1 != p2 : p1,p2 = num[p1], num[num[p2]]
		p2 = 0
		while p1 != p2 : p1,p2 = num[p1], num[p2]
		return p1