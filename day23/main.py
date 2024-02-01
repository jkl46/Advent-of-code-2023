import sys

inp = [[c for c in line.rstrip()] for line in open("input.txt", "r")]

NORTH = 1	
EAST = 2
SOUTH = 3
WEST = 4

dirToVec = {
	NORTH : (0, -1),	
	EAST : (1, 0),	
	SOUTH : (0, 1),	
	WEST : (-1, 0),	
}

noSlope = {
	NORTH :	'v',
	EAST :	'<',
	SOUTH :	'^',
	WEST :	'>',
}


class Walker:
	def __init__(self, steps, pos, lastPos, paths, slopes):
		self.steps = steps
		self.pos = pos
		self.lastPos = lastPos
		self.paths = paths
		self.slopes = slopes

def part1():
	def getNeighbours(pos):
		neighbours = []
		for direction in dirToVec.keys():
			nPos = dirToVec[direction]
			nX = pos[0] + nPos[0]
			nY = pos[1] + nPos[1]

			if nX < 0 or nY < 0 or nX >= len(inp[0]) or nY >= len(inp):
				continue
			c = inp[nY][nX]
			if c == '.':
				neighbours.append((nX, nY))

			elif c != '#':
				if c not in noSlope[direction]:
					neighbours.append((nX, nY))

		return neighbours

	start = (1, 0)
	finish = (len(inp[0])-2, len(inp)-1)
	lastPos = (0,0)
	longestSteps = 0

	walkers = [Walker(0, start, lastPos, [], [])]
	while len(walkers) != 0:
		cWalker = walkers.pop(0)

		while True:
			neighbours = getNeighbours(cWalker.pos)
			if cWalker.lastPos in neighbours:
				neighbours.remove(cWalker.lastPos)

			for path in cWalker.paths:
				if path in neighbours:
					cWalker.paths.remove(path)

			if len(neighbours) == 0:
				if cWalker.steps > longestSteps:
					longestSteps = cWalker.steps
				break

			if len(neighbours) == 1:
				cWalker.lastPos = cWalker.pos
				cWalker.pos = neighbours[0]
				cWalker.steps += 1
			else:
				for neighbour in neighbours:
					nPaths = cWalker.paths
					nPaths.append(neighbour)
					walkers.append(Walker(cWalker.steps+1, neighbour, cWalker.pos, nPaths, cWalker.slopes))
				break

	return longestSteps


def part2():
	return 0


print(f"awnser to part 1: {part1()}")
print(f"awnser to part 2: {part2()}")
