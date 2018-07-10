class Solution(object) :
	def findDuplicate(self, paths) :
		ans = {} # 文件内容:文件路径
		for i in paths :
			tmp = i.split(' ')
			path = tmp[0]
			for j in range(1, len(tmp)) :
				file_name, content = tmp[j].split('(')
				file_path = path + '/' + file_name
				content = content[:-1]
				if content in ans : ans[content].append(file_path)
				else : ans[content] = [file_path]
		return [i for i in ans.values() if len(i) > 1]