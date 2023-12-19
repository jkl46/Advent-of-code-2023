import sys

inp = [[char for char in line.rstrip()] for line in open("input.txt", "r")]

NORTH = 1
EAST = 2
SOUTH = 3
WEST = 4

possibleConnections = {
	"S" : (NORTH, EAST, SOUTH, WEST),
	"|" : (NORTH, SOUTH),
	"-" : (EAST, WEST),
	"L" : (SOUTH, EAST), # southward is increasing index in a 2d grid. north and south need to be switched
	"J" : (SOUTH, WEST),
	"7" : (NORTH, WEST),
	"F" : (NORTH, EAST),
}

directionCoords = {
	NORTH : (0, 1),
	EAST : (1, 0),
	SOUTH : (0, -1),
	WEST : (-1, 0),
}

inverseDirection = {
	NORTH : SOUTH,
	SOUTH : NORTH,
	WEST : EAST,
	EAST : WEST,
}

lastPos = (0,0)

def getNextPos(cPos, start=False):
	global lastPos
	possiblePos = []
	cPipe = inp[cPos[1]][cPos[0]]

	for direction in [NORTH, EAST, SOUTH, WEST]:
		try:
			dPos = directionCoords[direction] # direction position
			nPos = (cPos[0]+dPos[0], cPos[1]+dPos[1]) # new pos
			pipe = inp[nPos[1]][nPos[0]]

		except IndexError:
			continue

		if pipe == ".":
			continue

		if inverseDirection[direction] in possibleConnections[pipe] and direction in possibleConnections[cPipe]:
			possiblePos.append(nPos)

	if start:
		lastPos = cPos
		return possiblePos[1]

	if possiblePos[0] == lastPos:
		lastPos = cPos
		return possiblePos[1]
	else:
		lastPos = cPos
		return possiblePos[0]


def part1():
	startPos = (0,0)

	for idy, row in enumerate(inp):
		for idx, pipe in enumerate(row):
			if pipe == "S":
				startPos = (idx, idy)

	assert startPos != (0, 0)
	cPos = startPos
	steps = 0
	start = True
	while True:
		if start:
			cPos = getNextPos(cPos, start=True)
			start = False
		else:
			cPos = getNextPos(cPos)
		steps += 1
		if cPos == startPos:
			break

	return steps // 2

def part2():
	pass

print(f"awnser to part 1: {part1()}")
print(f"awnser to part 2: {part2()}")