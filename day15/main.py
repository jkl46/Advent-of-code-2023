import sys
inp = open("input.txt", "r").read().rstrip().split(',')

def getHashValue(string):
	v = 0
	for c in string:
		cVal = v + ord(c)
		cVal *= 17
		cVal  = cVal % 256
		v = cVal
	return v

def part1():
	result = 0
	for string in inp:
		result += getHashValue(string)	

	return result

def part2():
	result = 0
	hashMap = {x: [] for x in range(256)}
	for string in inp:
		if string[-1] == '-':
			label = string[:-1]
			boxNumber = getHashValue(label)

			labelsInBox = [x[0] for x in hashMap[boxNumber]]
			if label in labelsInBox:
				hashMap[boxNumber].pop(labelsInBox.index(label))
		else:
			label = string[:-2]
			focalLength = string[-1]
			boxNumber = getHashValue(label)

			labelsInBox = [x[0] for x in hashMap[boxNumber]]
			if label in labelsInBox:
				hashMap[boxNumber][labelsInBox.index(label)] = (label, focalLength)
			else:
				hashMap[boxNumber].append((label, focalLength))

	for x in range(256):
		for idx, lens in enumerate(hashMap[x]):
			result += (x + 1) * (idx + 1) * (int(lens[1]))

	return result


print(f"awnser to part 1: {part1()}")
print(f"awnser to part 2: {part2()}")