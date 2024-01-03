import sys
from sympy.utilities.iterables import multiset_permutations
# from sympy.utilities.iterables import multiset_permutations

# references: https://stackoverflow.com/a/43816996

inp = [line.rstrip() for line in open("input.txt", "r")]

def part1():
	totalSum = 0

	def isValidSpring(springMap, springGroups):
		springMap = ''.join(springMap)
		springMap = springMap.split('.')
		springCount = [len(x) for x in springMap if x != '']
		if springCount == springGroups:
			return True
		else:
			return False


	for idx, line in enumerate(inp):
		print(idx)
		line = line.split(' ')

		springMap = line[0]
		springGroupMap = [int(x) for x in line[1].split(',')]
		unknownCount = springMap.count('?')
		knownCount = springMap.count('#')

		springHolder = ['#' for _ in range(sum(springGroupMap) - knownCount)]
		springHolder.extend(['.' for _ in range(unknownCount - len(springHolder))])
		springToIdx = [idx for idx in range(len(springMap)) if springMap[idx] == '?']

		validCount = 0
		for _springMap in multiset_permutations(springHolder): 
			newSpring = [x for x in springMap]
			for idx in range(len(_springMap)):
				newSpring[springToIdx[idx]] = _springMap[idx]

			if isValidSpring(newSpring, springGroupMap):
				validCount += 1

		totalSum += validCount
	return totalSum

def part2():
	pass

print(f"awnser to part 1: {part1()}")
print(f"awnser to part 2: {part2()}")

