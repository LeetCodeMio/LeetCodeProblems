# 从左至右扫描座位，若某人A与其配偶B不相邻，则将A右侧的人与B交换
class Solution :
	def minSwapsCouples(self, person_on) :
		seat_of = [0] * len(person_on)
		for seat,person in enumerate(person_on) :
			seat_of[person] = seat
		def swap(a, i, j) :
			a[i], a[j] = a[j], a[i]
		count = 0
		for seat,person in enumerate(person_on) :
			if seat % 2 : continue
			next_person = person_on[seat+1]
			couple = person-1 if person % 2 else person+1
			if next_person == couple  : continue
			swap(person_on, seat+1, seat_of[couple])
			swap(seat_of, next_person, couple)
			count += 1
		return count