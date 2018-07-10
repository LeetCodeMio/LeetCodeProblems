# 将roots保存为前缀树
# 当rootA是rootB的前缀时，只在树中保留rootA
class Solution :
	def replaceWords(self, roots, sentence) :
		dic = {}
		for root in roots :
			node = dic
			for i in root :
				node = node.setdefault(i, {})
				if 'end' in node : break
			node.clear()
			node['end'] = True
		sentence = sentence.split()
		for index,word in enumerate(sentence) :
			node = dic
			for i,x in enumerate(word) :
				if x in node : node = node[x]
				else : break
				if 'end' in node :
					sentence[index] = word[:i+1]
					break
		return ' '.join(sentence)