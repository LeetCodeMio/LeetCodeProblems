class Solution : # 逆向动态规划
	def rob(self, root) :
		vis = {}
		def money(node, take) :
			if not node : return 0
			key = (id(node), take)
			if key in vis : return vis[key]
			ret = node.val if take else 0
			for child in (node.left, node.right) :
				tmp = money(child, False)
				if not take : tmp = max(tmp, money(child, True))
				ret += tmp
			vis[key] = ret
			return ret
		return max(money(root, True), money(root, False))