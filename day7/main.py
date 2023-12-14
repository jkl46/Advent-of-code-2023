import sys
from collections import Counter
inp = [line.rstrip() for line in open("input.txt", "r")]

rankMax = len(inp)

FIVE_OF_A_KIND 	= 7
FOUR_OF_A_KIND 	= 6
FULL_HOUSE 		= 5
THREE_OF_A_KIND = 4
TWO_PAIR 		= 3
ONE_PAIR 		= 2
HIGH_CARD 		= 1

cardToVal = {
	"A" : 14,
	"K" : 13,
	"Q" : 12,
	"J" : 11,
	"T" : 10,
	"9" : 9,
	"8" : 8,
	"7" : 7,
	"6" : 6,
	"5" : 5,
	"4" : 4,
	"3" : 3,
	"2" : 2,
}

class Hand:
	def __init__(self, hand, bid):
		self.hand = hand
		self.handScore = self.getHandScore(hand)
		self.bid = int(bid)

		# Create hashlike value from hand with (cardValue*1000)**(position*10). position is index in hand. AA9AB will be greater than AA9KB 
		self.handValue = sum([pow(cardToVal[x] * 1000, (len(hand) - idx) *10) for idx, x in enumerate(hand)]) 


	def getHandScore(self, hand):
		cards = [x for x in Counter(hand).values()]
		cards = [x for x in sorted(cards, reverse=True)]

		if cards[0] == 5:
			return FIVE_OF_A_KIND

		elif cards[0] == 4:
			return FOUR_OF_A_KIND

		elif cards[0] == 3 and cards[1] == 2:
			return FULL_HOUSE

		elif cards[0] == 3:
			return THREE_OF_A_KIND

		elif cards[0] == 2 and cards[1] == 2:
			return TWO_PAIR

		elif cards[0] == 2: 
			return ONE_PAIR

		else:
			return HIGH_CARD

	def __repr__(self):
		return str(self.hand)

def part1():
	cards = {
		FIVE_OF_A_KIND: [],
		FOUR_OF_A_KIND: [],
		FULL_HOUSE: [],
		THREE_OF_A_KIND: [],
		TWO_PAIR: [],
		ONE_PAIR: [],
		HIGH_CARD: [],
	}

	for line in inp:
		line = line.split(" ")
		handCards = line[0]	
		bid = line[1]

		hand = Hand(handCards, bid)
		cards[hand.handScore].append(hand)


	for x in range(1, 8): 
		cards[x] = sorted(cards[x], reverse=True, key=lambda x : x.handValue)


	total = 0
	cRank = rankMax
	for cardList in cards.values():
		for card in cardList:
			total += card.bid * cRank
			cRank -= 1

	return total

def part2():
	pass

print(f"awnser to part 1: {part1()}")
print(f"awnser to part 2: {part2()}")