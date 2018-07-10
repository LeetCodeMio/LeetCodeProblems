# 并查集
# 将一种字母出现的首位置到尾位置合并
# 将具有交叠的并查集合并
class Solution(object) :
	def partitionLabels(self, S) :
		vis = {} # 字母 : 第一次出现的位置
		bcj = [i for i in range(len(S))] # 并查集
		for i in range(len(S)) :
			if S[i] in vis :
				tmp = bcj[vis[S[i]]]
				j = i
				while bcj[j] != tmp :
					bcj[j] = tmp
					j -= 1
			else : vis[S[i]] = i
		ans, c, last = [], 0, bcj[0]
		for i in bcj :
			if i != last :
				ans += [c]
				c = 0
				last = i
			c += 1
		ans += [c]
		return ans