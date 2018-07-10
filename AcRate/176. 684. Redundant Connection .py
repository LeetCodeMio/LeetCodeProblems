from collections import defaultdict
class Solution : # 寻找环 返回环中key最大的边 深度优先搜索
	def findRedundantConnection(self, edges) :
		graph = defaultdict(dict)
		for k,(a,b) in enumerate(edges) :
			graph[a][b], graph[b][a] = k,k
		trace = {'now':1, 1:(None, iter(graph[1]))}
		while True :
			node = trace['now']
			pnode, nnode = trace[node]
			try : nnode = next(nnode)
			except :
				del(trace[node])
				trace['now'] = pnode
				continue
			if nnode == pnode : continue
			if nnode in trace : break
			trace[nnode] = (node, iter(graph[nnode]))
			trace['now'] = nnode
		ret = [graph[node][nnode], (node,nnode)]
		while node != nnode :
			pnode = trace[node][0]
			ret = max(ret, [graph[node][pnode], (node,pnode)])
			node = pnode
		return sorted(ret[1])