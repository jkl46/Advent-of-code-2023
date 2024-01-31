import sys
from math import ceil

def getInput():
	return [[c for c in line.rstrip()] for line in open("input.txt", "r")]

def part1():
	inp = getInput()
	for idy in range(len(inp)):
		for idx in range(len(inp[0])):
			c = inp[idy][idx]
			if c == 'O':
				thisY = idy
				while inp[thisY - 1][idx] == '.' and thisY - 1 >= 0:
					thisY -= 1
				inp[idy][idx] = '.'
				inp[thisY][idx] = 'O'
				
	return sum([(len(inp)-idy) for idy, row in enumerate(inp) for c in row if c == 'O'])

def part2(): # Starting with copy of part 1.
	inp = getInput()

	rowHistory = []
	resultHistory = []
	cycles = 1_000_000_000

	for i in range(cycles):
		for _ in range(4):
			for idy in range(len(inp)):
				for idx in range(len(inp[0])):
					c = inp[idy][idx]
					if c == 'O':
						thisY = idy
						while inp[thisY - 1][idx] == '.' and thisY - 1 >= 0:
							thisY -= 1
						inp[idy][idx] = '.'
						inp[thisY][idx] = 'O'

			h = hash(''.join([str(c) for b in inp for c in b]))	
			if h in rowHistory:
				s = rowHistory.index(h)
				e = len(rowHistory)
				diff = e - s
				return resultHistory[ceil((((cycles*4-s)%diff)+s)/4)-1]

			rowHistory.append(h)

			inp = [[*row][::-1] for row in zip(*inp)]

		resultHistory.append(sum([(len(inp)-idy) for idy, row in enumerate(inp) for c in row if c == 'O']))

print(f"awnser to part 1: {part1()}")
print(f"awnser to part 2: {part2()}")
