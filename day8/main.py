import sys
import math

inp = [line.rstrip() for line in open("input.txt", "r")]

def part1():
	directions = [x for x in inp[0]]

	mapTable = {}

	for _map in inp[2:]:
		_map = _map.split(" = ")
		k = _map[0]
		v = tuple(_map[1][1:-1].split(", "))
		mapTable[k] = v

	step = 0
	cElement = 'AAA'
	while True:
		instruction = directions[step % len(directions)]

		if instruction == 'L':
			cElement = mapTable[cElement][0]
		elif instruction == 'R':
			cElement = mapTable[cElement][1]

		if cElement == 'ZZZ':
			return step + 1

		step += 1



# references https://www.reddit.com/r/adventofcode/comments/18dhqti/2023_day_8_part_2_eli5_how_the_much_discussed/
# Had to search for solution. Found solution with lcm
def part2(): # starting with copy of part 1
	directions = [x for x in inp[0]]
	directionsLength = len(directions)
	mapTable = {}

	ghosts = []

	for _map in inp[2:]:
		_map = _map.split(" = ")
		k = _map[0]
		if k[-1] == 'A':
			ghosts.append(k)
		v = tuple(_map[1][1:-1].split(", "))
		mapTable[k] = v

	ghostsSteps = []

	for ghost in ghosts:
		i = 0
		while ghost[-1] != 'Z':
			if directions[i % len(directions)] == 'L':
				ghost = mapTable[ghost][0]
			else:
				ghost = mapTable[ghost][1]
			i += 1

		ghostsSteps.append(i)

	return math.lcm(*ghostsSteps)

	
print(part1())
print(part2())