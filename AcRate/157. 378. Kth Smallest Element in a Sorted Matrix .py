import heapq as hp
class Solution : # 归并排序
	def kthSmallest(self, matrix, k) :
		heap = [(matrix[i][0], i, 0) for i in range(len(matrix))]
		hp.heapify(heap)
		for _ in range(k-1) :
			num, i,j = hp.heappop(heap)
			if j+1 < len(matrix[0]) :
				hp.heappush(heap, (matrix[i][j+1], i, j+1))
		return heap[0][0]