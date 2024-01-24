import sys
from itertools import combinations
inp = [[char for char in line.rstrip()] for line in open("input.txt", "r")]

def part1():
	rowExpand = []
	colExpand = []
	galaxyCoords = []
	totalSum = 0

	# Find empty rows
	for idx, row in enumerate(inp):
		if '#' not in row:
			rowExpand.append(idx)

	# Find empty collumns
	for col in range(len(inp[0])):
		if '#' not in [inp[y][col] for y in range(len(inp))]:
			colExpand.append(col)

	# Find galaxies
	for idx in range(len(inp[0])):
		for idy in range(len(inp)):
			if inp[idy][idx] == '#':
				galaxyCoords.append((idx, idy))

	while len(galaxyCoords)	> 1:
		cGalaxy = galaxyCoords.pop(0)

		for galaxy in galaxyCoords:
			totalSum += max(cGalaxy[0], galaxy[0]) - min(cGalaxy[0], galaxy[0])
			totalSum += max(cGalaxy[1], galaxy[1]) - min(cGalaxy[1], galaxy[1])

			for x in range(min(cGalaxy[0], galaxy[0]), max(cGalaxy[0], galaxy[0])):
				if x in colExpand:
					totalSum += 1

			for y in range(min(cGalaxy[1], galaxy[1]), max(cGalaxy[1], galaxy[1])):
				if y in rowExpand:
					totalSum += 1


	return totalSum



def part2():
	rowExpand = []
	colExpand = []
	galaxyCoords = []
	totalSum = 0

	# Find empty rows
	for idx, row in enumerate(inp):
		if '#' not in row:
			rowExpand.append(idx)

	# Find empty collumns
	for col in range(len(inp[0])):
		if '#' not in [inp[y][col] for y in range(len(inp))]:
			colExpand.append(col)

	# Find galaxies
	for idx in range(len(inp[0])):
		for idy in range(len(inp)):
			if inp[idy][idx] == '#':
				galaxyCoords.append((idx, idy))

	while len(galaxyCoords)	> 1:
		cGalaxy = galaxyCoords.pop(0)

		for galaxy in galaxyCoords:
			totalSum += max(cGalaxy[0], galaxy[0]) - min(cGalaxy[0], galaxy[0])
			totalSum += max(cGalaxy[1], galaxy[1]) - min(cGalaxy[1], galaxy[1])

			for x in range(min(cGalaxy[0], galaxy[0]), max(cGalaxy[0], galaxy[0])):
				if x in colExpand:
					totalSum += 999999

			for y in range(min(cGalaxy[1], galaxy[1]), max(cGalaxy[1], galaxy[1])):
				if y in rowExpand:
					totalSum += 999999

	return totalSum

print(f"awnser to part 1: {part1()}")
print(f"awnser to part 2: {part2()}")