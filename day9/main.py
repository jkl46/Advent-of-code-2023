import sys
inp = [[int(char) for char in line.rstrip().split(" ")] for line in open("input.txt", "r")]

def getDifference(num1, num2):
	if num1 < 0 and num2 < 0:
		return num1 - num2

	elif num1 < 0 and num2 > 0:
		return abs(num1) + num2

	elif num1 > 0 and num2 < 0:
		return num1 + abs(num2)

	return abs(num1 - num2)

def getNextValue(line):
	sequences = [line]
	lastValues = line[-1]
	while sequences[-1][-1] != 0 and len(sequences[-1]) != 1:
		cLine = sequences[-1]

		sequences.append([])

		for n1, n2 in zip(cLine, cLine[1:]):
			sequences[-1].append(n1 - n2)
		lastValues += abs(sequences[-1][-1])

	return lastValues

def part1():
	return sum([getNextValue(line) for line in inp])

def part2():
	pass

print(f"awnser to part 1: {part1()}")
print(f"awnser to part 2: {part2()}")