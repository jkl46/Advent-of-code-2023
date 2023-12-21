inp = [line.rstrip() for line in open("input.txt", "r")]

seeds = list(map(int,inp[0][7:].split(" ")))

seed2soil = [tuple(map(int, x.split(" "))) for x in inp[3:13]]
soil2fertilizer = [tuple(map(int, x.split(" "))) for x in inp[15:31]]
fertilizer2water = [tuple(map(int, x.split(" "))) for x in inp[33:48]]
water2light = [tuple(map(int, x.split(" "))) for x in inp[50:95]]
light2temperature = [tuple(map(int, x.split(" "))) for x in inp[97:112]]
temperature2humidity = [tuple(map(int, x.split(" "))) for x in inp[114:137]]
humidity2location = [tuple(map(int, x.split(" "))) for x in inp[139:150]]

def part1():
	locations = []
	def getNewRange(_map, num):
		for destinationStart, sourceStart, rangeLength in _map:
			if sourceStart <= num and num <= sourceStart + rangeLength - 1:
				return destinationStart + num - sourceStart

		return num

	for seed in seeds:
		seed = getNewRange(seed2soil, seed)
		seed = getNewRange(soil2fertilizer, seed)
		seed = getNewRange(fertilizer2water, seed)
		seed = getNewRange(water2light, seed)
		seed = getNewRange(light2temperature, seed)
		seed = getNewRange(temperature2humidity, seed)
		seed = getNewRange(humidity2location, seed)
		locations.append(seed)

	return min(locations)


def part2(): # Brute force too slow, going from location to seed
	def getNewRange(_map, num):
		for destinationStart, sourceStart, rangeLength in _map:
			if destinationStart <= num and num <= destinationStart + rangeLength - 1:
				return sourceStart + num - destinationStart

		return num

	location = 0
	while True:
		seed = location
		seed = getNewRange(humidity2location, seed)
		seed = getNewRange(temperature2humidity, seed)
		seed = getNewRange(light2temperature, seed)
		seed = getNewRange(water2light, seed)
		seed = getNewRange(fertilizer2water, seed)
		seed = getNewRange(soil2fertilizer, seed)
		seed = getNewRange(seed2soil, seed)

		for seedStart, seedRange in zip(seeds[::2], seeds[1::2]):
			if seedStart <= seed and seed <= seedStart + seedRange:
				return location

		location += 1

print(f"awnser to part 1: {part1()}")
print(f"awnser to part 2: {part2()}")

