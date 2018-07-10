class Solution :
	def floodFill(self, image, x, y, new) :
		old = image[x][y]
		if old == new : return image
		image[x][y] = new
		stack = [(x,y)]
		dxs = [0,0,1,-1]
		dys = [1,-1,0,0]
		while stack :
			x0,y0 = stack.pop()
			for dx,dy in zip(dxs,dys) :
				x, y = x0+dx, y0+dy
				if not(0 <= x < len(image)) : continue
				if not(0 <= y < len(image[0])) : continue
				if image[x][y] != old : continue
				image[x][y] = new
				stack.append((x,y))
		return image