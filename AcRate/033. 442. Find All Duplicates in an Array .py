# 空间O(0) 时间O(n)
class Solution(object) :
	def findDuplicates(self, nums) :
		ret = []
		for i in range(len(nums)) :
			# 规定nums[i]只能是i+1或者-1
			while nums[i] != i+1 :
				if nums[i] == -1 : break
				# 尝试把nums[i]放到应在的位置nums[i]-1
				# 准备将其与目标位置的元素交换
				j = nums[i] - 1
				a, b, = nums[i], nums[j]
				# 如果和目标位置的元素一样
				# 说明该元素出现了两次
				# 更新ret并将nums[i]置为-1
				if a == b :
					ret += [nums[i]]
					nums[i] = -1
					break
				# 否则执行交换
				nums[i], nums[j] = b, a
		return ret