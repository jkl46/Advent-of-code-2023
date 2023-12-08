inp = [line.rstrip() for line in open("input.txt", "r")]

def part1():
	total = 0
	for card in inp:
		winsInCard = 0
		card = card[10:]
		card = card.replace("|", "")
		card = [x for x in card.split(" ") if x != ""]
		winning = card[:10]
		numbers = card[10:]

		for num in numbers:
			if num in winning:
				winsInCard += 1

		if winsInCard != 0:
			total += pow(2, winsInCard -1)

	return total


def part2(): 
	cardCount = {}
	for x in range(1,204):
		cardCount[str(x)] = 1

	for idx, card in enumerate(inp):
		winsInCard = 0
		card = card[10:]
		card = card.replace("|", "")
		card = [x for x in card.split(" ") if x != ""]
		winning = card[:10]
		numbers = card[10:]

		for num in numbers:
			if num in winning:
				winsInCard += 1

		for it in range(cardCount[str(idx+1)]):
			for x in range(winsInCard):
				cardCount[str(idx+2+x)] += 1
				
	return sum(cardCount.values())


print(f"awnser to part 1: {part1()}")
print(f"awnser to part 2: {part2()}")