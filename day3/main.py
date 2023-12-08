inp = [[char for char in x.rstrip() ]for x in open('input.txt', 'r')]

def part1(): 
	nums = '1234567890'
	def findAndReplace(x, y):
		num = ''
		off = 0
		startIdx = 0
		endIdx = 0

		if inp[y][x] in nums:

			try:
				while inp[y][x + off] in nums:
					off -= 1
			except IndexError:
				pass

			startIdx = x + off + 1
			off = 0

			try:
				while inp[y][x + off] in nums:
					off += 1
			except IndexError:
				pass

			endIdx = x + off - 1
			for _x in range(startIdx, endIdx+1):
				num += inp[y][_x]
				inp[y][_x] = '.'

		return int(num)

	n = 0
	for idy, row in enumerate(inp):
		for idx, char in enumerate(row):
			if char not in '1234567890.':
				try:
					if inp[idy-1][idx-1] in nums:
						n += findAndReplace(idx-1, idy-1)
				except IndexError:
					pass

				try:
					if inp[idy-1][idx] in nums:
						n += findAndReplace(idx, idy-1)
				except IndexError:
					pass

				try:
					if inp[idy-1][idx+1] in nums:
						n += findAndReplace(idx+1, idy-1)
				except IndexError:
					pass

				try:
					if inp[idy][idx-1] in nums:
						n += findAndReplace(idx-1, idy)
				except IndexError:
					pass

				try:
					if inp[idy][idx+1] in nums:
						n += findAndReplace(idx+1, idy)
				except IndexError:
					pass

				try:
					if inp[idy+1][idx-1] in nums:
						n += findAndReplace(idx-1, idy+1)
				except IndexError:
					pass

				try:
					if inp[idy+1][idx] in nums:
						n += findAndReplace(idx, idy+1)
				except IndexError:
					pass

				try:
					if inp[idy+1][idx+1] in nums:
						n += findAndReplace(idx+1, idy+1)
				except IndexError:
					pass
	return n


def part2(): # starting with copy of part1
	nums = '1234567890'
	def findAndReplace(x, y):
		num = ''
		off = 0
		startIdx = 0
		endIdx = 0

		if inp[y][x] in nums:

			try:
				while inp[y][x + off] in nums:
					off -= 1
			except IndexError:
				pass

			startIdx = x + off + 1
			off = 0

			try:
				while inp[y][x + off] in nums:
					off += 1
			except IndexError:
				pass

			endIdx = x + off - 1
			for _x in range(startIdx, endIdx+1):
				num += inp[y][_x]
				inp[y][_x] = '.'

			return int(num)

	n = 0
	for idy, row in enumerate(inp):
		for idx, char in enumerate(row):
			if char == '*':
				adjacent = []
				try:
					if inp[idy-1][idx-1] in nums:
						adjacent.append(findAndReplace(idx-1, idy-1))
				except IndexError:
					pass

				try:
					if inp[idy-1][idx] in nums:
						adjacent.append(findAndReplace(idx, idy-1))
				except IndexError:
					pass

				try:
					if inp[idy-1][idx+1] in nums:
						adjacent.append(findAndReplace(idx+1, idy-1))
				except IndexError:
					pass

				try:
					if inp[idy][idx-1] in nums:
						adjacent.append(findAndReplace(idx-1, idy))
				except IndexError:
					pass

				try:
					if inp[idy][idx+1] in nums:
						adjacent.append(findAndReplace(idx+1, idy))
				except IndexError:
					pass

				try:
					if inp[idy+1][idx-1] in nums:
						adjacent.append(findAndReplace(idx-1, idy+1))
				except IndexError:
					pass

				try:
					if inp[idy+1][idx] in nums:
						adjacent.append(findAndReplace(idx, idy+1))
				except IndexError:
					pass

				try:
					if inp[idy+1][idx+1] in nums:
						adjacent.append(findAndReplace(idx+1, idy+1))
				except IndexError:
					pass

				if len(adjacent) == 2:
					n += (adjacent[0] * adjacent[1])
	return n

# Input is modified by function. input must be reset before finding awnser to part2
print(f"awnser part 1: {part1()}")

inp = [[char for char in x.rstrip() ]for x in open('input.txt', 'r')]
print(f"awnser part 2: {part2()}")
