inp = [[55, 401], [99, 1485], [97, 2274], [93, 1405]] # only 8 numbers for input. parsing from file not really necessary

def part1():
	getDistance = lambda timePressed, timing :  (x * (timing - x))

	points = 1

	for race in inp:
		fasterTimes = 0

		time = race[0]
		distance = race[1]

		for x in range(1, time):
			if getDistance(x, time) > distance:
				fasterTimes += 1

		points *= fasterTimes

	return points

def part2(): # takes a very long time calculate. the part2.cpp should calculate it in just a few seconds. this function could take 60+ minutes
	getDistance = lambda timePressed, timing :  (x * (timing - x))
	points = 1

	time = ''
	distance = ''

	for x in inp:
		time += str(x[0])
		distance += str(x[1])

	time = int(time)
	distance = int(distance)

	fasterTimes = 0

	for x in range(1, time):
		if getDistance(x, time) > distance:
			print(x / time * 100)
			fasterTimes += 1

	return fasterTimes



print(f"awnser to part 1: {part1()}")
print(f"awnser to part 2: {part2()}")