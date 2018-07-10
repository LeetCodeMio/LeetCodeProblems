class MagicDictionary :
	def buildDict(self, words) :
		self.words = {}
		for i in words :
			self.words.setdefault(len(i), []).append(i)
	def search(self, word) :
		if len(word) not in self.words : return False
		for i in self.words[len(word)] :
			num = 0
			for index,char in enumerate(word) :
				if i[index] != char : num += 1
				if num == 2 : break
			if num == 1 : return True
		return False