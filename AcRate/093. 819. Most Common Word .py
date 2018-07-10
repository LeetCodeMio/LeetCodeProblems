from collections import Counter
class Solution :
	def mostCommonWord(self, paragraph, banned) :
		paragraph = ''.join(i.lower() for i in paragraph if i not in "!?',;.")
		banned = set(banned)
		for i,_ in Counter(paragraph.split()).most_common() :
			if i not in banned : return i