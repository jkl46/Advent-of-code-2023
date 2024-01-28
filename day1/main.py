import sys, re
inp = [line.rstrip() for line in open("input.txt", "r")] 

def part1():
	result = 0
	numsREG = re.compile(r'\d')

	for line in inp:
		nums = numsREG.findall(line)
		result += int(nums[0] + nums[-1])

	return result

def part2():
	result = 0

	nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', *[str(x) for x in range(10)]]
	numToInt = {key: x % 10 for key, x in zip(nums, range(20))} 

	getNums = re.compile(f'{"|".join(nums)}')
	getReversedNums = re.compile(f'{"|".join(list(map(lambda x: x[::-1], nums)))}')

	for line in inp:
		firstNum = numToInt[getNums.search(line).group()]
		lastNum = numToInt[getReversedNums.search(line[::-1]).group()[::-1]]
		result += int(str(firstNum) + str(lastNum))

	return result


print(f"awnser to part 1: {part1()}")
print(f"awnser to part 2: {part2()}")