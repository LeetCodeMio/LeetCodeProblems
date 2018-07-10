class Solution(object) :
	def subdomainVisits(self, cpdomains) :
		ans = {}
		for cpdomain in cpdomains :
			count, address = cpdomain.split(' ')
			addresses = [address]
			addresses += [address[i+1:]
				for i in range(len(address))
				if address[i] == '.']
			for i in addresses :
				if i in ans : ans[i] += int(count)
				else : ans[i] = int(count)
		return [str(v) + ' ' + k for k, v in ans.items()]