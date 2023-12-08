inp = [line.rstrip() for line in open('input.txt', 'r')]

def part1():
	maxRed = 12
	maxGreen = 13
	maxBlue = 14
	idSum = 0

	for idx, line in enumerate(inp):
		r = 0
		g = 0
		b = 0

		line = line.replace(";", "")
		line = line.replace(",", "")
		line = line.split()[2:]
		print(line)

		for x in range(0, len(line), 2):
			n = int(line[x])
			color = line[x+1]

			if color == 'red':
				r += n

			elif color == 'green':
				g += n

			elif color == 'blue':
				b += n

		if r <= maxRed:
			if g <= maxGreen:
				if b <= maxBlue:
					idSum += idx + 1

	return idSum


def part2():
	pass

print(f"awnser part1: {part1()}")
print(f"awnser part2: {part2()}")
