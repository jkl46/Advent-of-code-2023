import sys
inp = [line.rstrip() for line in open('input.txt', 'r')]

def part1():
	maxRed = 12
	maxGreen = 13
	maxBlue = 14
	idSum = 0

	color = {}

	for idx, line in enumerate(inp):
		r = 0
		g = 0
		b = 0

		line = line.replace(";", "")
		line = line.replace(",", "")
		line = line.split()[2:]


		for x in range(1, len(line), 2):
			if line[x] not in color:
				color[line[x]] = 0
			else:
				color[line[x]] += int(line[x-1])

		print(color)
		if r <= color['red']:
			if g <= color['green']:
				if b <= color['blue']:
					idSum += idx + 1

	return idSum


def part2():
	pass

print(f"awnser part1: {part1()}")
print(f"awnser part2: {part2()}")
