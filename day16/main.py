import sys
inp = [[x for x in line.rstrip()] for line in open("input.txt", "r")]

directionToVec = {
	"N" : (0, -1), 	# NORTH
	"E" : (1, 0), 	# EAST
	"S" : (0, 1), 	# SOUTH
	"W" : (-1, 0), 	# WEST
}

directionOnDiagonal = {
	"N" : {"\\" : "W", "/" : "E"},
	"E" : {"\\" : "S", "/" : "N"},
	"S" : {"\\" : "E", "/" : "W"},
	"W" : {"\\" : "N", "/" : "S"},
}

directionOnSplit = {
	"N" : "-",
	"E" : "|",
	"S" : "-",
	"W" : "|",
}


class Beam:
	def __init__(self, position, direction): # position (x, y), direction NORTH, EAST, SOUTH, WEST
		self.pos = position
		self.direction = direction

def part1():
	energisedCells = [[0 for _ in range(len(inp[0]))] for _ in range(len(inp))]
	beams = [Beam((0,0), "E")]
	gridWidth = len(inp[0]) - 1
	gridHeight = len(inp) - 1
	while len(beams) != 0:
		for beam in beams:
			x = beam.pos[0]
			y = beam.pos[1]
			if x < 0 or x > gridWidth or y < 0 or y > gridHeight:
				beams.remove(beam)
				continue
			cBlock = inp[y][x]

			if cBlock in ["\\", "/"]:
				beam.direction = directionOnDiagonal[beam.direction][cBlock]

			elif cBlock == directionOnSplit[beam.direction]:
				if energisedCells[y][x] == 1:
					beams.remove(beam)
				else:
					if cBlock == "-":
						beams.append(Beam(beam.pos, "E"))
						beams.append(Beam(beam.pos, "W"))
					elif cBlock == "|":
						beams.append(Beam(beam.pos, "N"))
						beams.append(Beam(beam.pos, "S"))

					beams.remove(beam)

			if beam in beams:	
				beam.pos = tuple((sum([*v]) for v in zip(beam.pos, directionToVec[beam.direction])))
			energisedCells[y][x] = 1

	return sum([sum(row) for row in energisedCells])

def part2(): # starting with copy of part 1
	gridWidth = len(inp[0]) - 1
	gridHeight = len(inp) - 1
	
	def getEnergy(initialBeam):
		energisedCells = [[0 for _ in range(len(inp[0]))] for _ in range(len(inp))]
		beams = [initialBeam]
		gridWidth = len(inp[0]) - 1
		gridHeight = len(inp) - 1
		while len(beams) != 0:
			for beam in beams:
				x = beam.pos[0]
				y = beam.pos[1]
				if x < 0 or x > gridWidth or y < 0 or y > gridHeight:
					beams.remove(beam)
					continue
				cBlock = inp[y][x]

				if cBlock in ["\\", "/"]:
					beam.direction = directionOnDiagonal[beam.direction][cBlock]

				elif cBlock == directionOnSplit[beam.direction]:
					if energisedCells[y][x] == 1:
						beams.remove(beam)
					else:
						if cBlock == "-":
							beams.append(Beam(beam.pos, "E"))
							beams.append(Beam(beam.pos, "W"))
						elif cBlock == "|":
							beams.append(Beam(beam.pos, "N"))
							beams.append(Beam(beam.pos, "S"))

						beams.remove(beam)

				if beam in beams:	
					beam.pos = tuple((sum([*v]) for v in zip(beam.pos, directionToVec[beam.direction])))
				energisedCells[y][x] = 1
		return sum([sum(row) for row in energisedCells])

	maxEnergy = 0
	startBeams = [Beam((x, 0), "S") for x in range(gridWidth)] \
		+  [Beam((x, gridHeight), "N") for x in range(gridWidth)] \
		+  [Beam((0, y), "E") for y in range(gridHeight)] \
		+  [Beam((gridWidth, y), "W") for y in range(gridHeight)] \

	for startBeam in startBeams:
		energy = getEnergy(startBeam)
		if energy > maxEnergy:
			maxEnergy = energy

	return maxEnergy	

print(f"awnser to part 1: {part1()}")
print(f"awnser to part 2: {part2()}")