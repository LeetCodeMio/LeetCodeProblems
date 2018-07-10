import numpy as np
# 随机6位编码，判重，存入字典
class Codec :
	def __init__(self) :
		self.dic = '0123456789qwertyuiopasdfghjklzxcvbnm'
		self.dic_len = len(self.dic)
		self.shortUrl_len = 6
		self.data = {}
	def encode(self, longUrl) :
		while True :
			code = np.random.randint(0, self.dic_len, [self.shortUrl_len])
			code = ''.join([self.dic[i] for i in code])
			code = 'http://tinyurl.com/' + code
			if code not in self.data : break
		self.data.update({code: longUrl})
		return code
	def decode(self, shortUrl) :
		return self.data[shortUrl]