import sys
inp = [[int(x) for x in line.rstrip().split(" ")[1:] if x != ''] for line in open("input.txt", "r")]


def part1():
	getDistance = lambda timePressed, timing :  (x * (timing - x))

	points = 1

	for time, distance in zip(inp[0], inp[1]):
		fasterTimes = 0

		for x in range(1, time):
			if getDistance(x, time) > distance:
				fasterTimes += 1

		points *= fasterTimes

	return points

def part2(): 
	getDistance = lambda timePressed, timing :  (x * (timing - x))
	points = 1

	time = int(''.join([str(x) for x in inp[0]]))
	distance = int(''.join([str(x) for x in inp[1]]))

	lowerBounds = 0
	running = True
	significance = 1

	x = 0
	steps = 1

	while getDistance(x, time) < distance: # Find first faster time
		x += 1

	lowerBounds = x

	while getDistance(x, time) > distance: # Find first slower time, increase steps exponetionally
		steps *= 2
		x += steps

	steps = 1
	while getDistance(x, time) < distance: # Find last faster time by decreasing steps
		x -= steps

	x += 1

	return x - lowerBounds


print(f"awnser to part 1: {part1()}")
print(f"awnser to part 2: {part2()}")