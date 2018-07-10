class Solution : # 逆向动态规划
	def shoppingOffers(self, price, special, needs) :
		useful = []
		for *offer, sprice in special :
			if sum(i*j for i,j in zip(price,offer)) > sprice :
				useful.append((offer, sprice))
		vis = {}
		def cost(needs) :
			if tuple(needs) in vis : return vis[tuple(needs)]
			ret = float('inf')
			for offer, sprice in useful :
				new = [i-j for i,j in zip(needs,offer)]
				if any(i<0 for i in new) : continue
				ret = min(ret, cost(new) + sprice)
			if ret == float('inf') :
				ret = sum(i*j for i,j in zip(price,needs))
			vis[tuple(needs)] = ret
			return ret
		return cost(needs)