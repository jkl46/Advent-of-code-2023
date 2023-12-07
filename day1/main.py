inp = [line.rstrip() for line in open("input.txt", "r")] # store lines in input.txt as array, remove \n

def part1():
	nums = '1234567890'
	totalSum = 0
	for line in inp:
		for x in range(len(line)):
			if line[x] in nums:
				a = line[x]
				break

		for x in range(len(line)-1, -1, -1): 
			if line[x] in nums:
				b = line[x]
				break
		totalSum += int(a + b)
	return totalSum

def part2():
	nums = "1234567890"
	numsInWord = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	totalSum = 0

	def findFirstChar(line, reverse=False): # better to use function to break out of multiple for loops using return
		for idx, char in enumerate(line):
			if char in nums: # if character is 1 or 2 or 3, etc
				return char

			else: # if character maybe is part of "one", "two", "three"
				for thisIdx, number in enumerate(numsInWord): # note: going out of index while slicing a string will not cause error
					if reverse:
						number = number[::-1]

					if line[idx:idx+len(number)] == number:
						return str(thisIdx) # i.e "eight", is at index 8 in numsInWord array, no need to extract value from dictionary

		raise Exception("not good")

	for line in inp:
		a = findFirstChar(line)
		b = findFirstChar(line[::-1], reverse=True) # to find the last number in line use same function but reverse string and reverse search match i.e "eight" -> "thgie"
		totalSum += int(a + b)
	return totalSum

print(f"awnser to part 1: {part1()}")
print(f"awnser to part 2: {part2()}")