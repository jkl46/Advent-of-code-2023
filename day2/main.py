import sys
inp = [line.rstrip() for line in open("input.txt", "r")]

def part1():
	maxRed = 12
	maxGreen = 13
	maxBlue = 14

	idSum = 0

	for idx, line in enumerate(inp):
		possible = True
		gameId = idx + 1
		line = line.split(": ")[1].split("; ")
		for foo, x in enumerate(line):
			line[foo] = line[foo].split(" ") # transform line into [['1', 'red', '2', 'blue'], ['4', 'green', '9', 'blue', etc..], etc..]

		for subset in line:	
			r = 0	
			g = 0
			b = 0

			for thisIdx in range(1, len(subset), 2):
				cubeColor = subset[thisIdx]
				cubeAmount = int(subset[thisIdx-1])

				if cubeColor[-1] == ",":
					cubeColor = cubeColor.rstrip(",")

				match cubeColor:
					case 'red':
						r += cubeAmount

					case 'green':
						g += cubeAmount

					case 'blue':
						b += cubeAmount

			if r > maxRed:
				possible = False
			if g > maxGreen:
				possible = False
			if b > maxBlue:
				possible = False

		if possible:
			idSum += gameId

	return idSum

def part2(): # Starting with copy of part1

	powerSum = 0

	for idx, line in enumerate(inp):
		gameId = idx + 1
		line = line.split(": ")[1].split("; ")

		for foo, x in enumerate(line):
			line[foo] = line[foo].split(" ") # transform line into [['1', 'red', '2', 'blue'], ['4', 'green', '9', 'blue', etc..], etc..]

		maxRed = 0
		maxGreen = 0
		maxBlue = 0

		for subset in line:	
			r = 0	
			g = 0
			b = 0

			for thisIdx in range(1, len(subset), 2):
				cubeColor = subset[thisIdx]
				cubeAmount = int(subset[thisIdx-1])

				if cubeColor[-1] == ",":
					cubeColor = cubeColor.rstrip(",")

				match cubeColor:
					case 'red':
						r += cubeAmount

					case 'green':
						g += cubeAmount

					case 'blue':
						b += cubeAmount

			if r > maxRed:
				maxRed = r

			if g > maxGreen:
				maxGreen = g

			if b > maxBlue:
				maxBlue = b

		powerSum += maxRed * maxBlue * maxGreen 

	return powerSum


print(f"awnser to part 1: {part1()}")
print(f"awnser to part 2: {part2()}")