import random

# Code for building a deck of cards and drawing a card to the players hand taken from:
# https://www.youtube.com/watch?v=t8YkjDH86Y4

#Dictates the individual cards including their suit and value.
class Card(object):
	def __init__(self, suit, val):
		self.suit = suit
		self.value = val
	
	def getCard(self):
		if self.value > 9:
			return f"{self.suit}{self.value}"
		else:
			return f"{self.suit} {self.value}"
	
	def getValue(self):
		return int(self.value)
		
	#Displays the card suit and value
	def show(self):			
		print(" _____ ")
		print("|     |")
		if self.value > 9:
			print(f"| {self.value}{self.suit} |")
		else:
			print(f"| {self.value}{self.suit}  |")
		print("|     |")
		print("|     |")
		print(" ----- ")
		
	#def ability(self):
		
class Deck(object):
	def __init__(self):
		self.cards = []
		self.build()
		
	def build(self):
		for s in ["\u2663","\u2664","\u2665","\u2666"]:
			for v in range(1,14):
				self.cards.append(Card(s,v))
						
	def show(self):
		for c in self.cards:
			c.show()
	
	def shuffle(self):
		for i in range(len(self.cards)-1, 0, -1):
			r = random.randint(0, i)
			self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
	
	def drawCard(self):
		return self.cards.pop()
	
	
class Player(object):
	def __init__(self, name):
		self.name = name
		self.hand = []
		self.score = 0
		
		
	def draw(self, deck):
		self.hand.append(deck.drawCard())
	
	def deal(self, deck):
		self.hand.append(deck.drawCard())
		self.hand.append(deck.drawCard())
		self.hand.append(deck.drawCard())
		self.hand.append(deck.drawCard())
		
	def showHand(self):
		print(" _____     _____")
		print("|     |   |     |")
		print(f"| {self.hand[0].getCard()} |   | {self.hand[1].getCard()} |")
		print("|     |   |     |")
		print("|     |   |     |")
		print(" -----     -----")
		
		print(" _____     _____")
		print("|     |   |     |")
		print(f"| {self.hand[2].getCard()} |   | {self.hand[3].getCard()} |")
		print("|     |   |     |")
		print("|     |   |     |")
		print(" -----     -----")
	
	def discard(self):
		return self.hand.pop()
	
	def displayGrid(self):
		print(" _____     _____")
		print("|#####|   |#####|")
		print("|# 1 #|   |# 2 #|")
		print("|#####|   |#####|")
		print("|#####|   |#####|")
		print(" -----     -----")
		
		print(" _____     _____")
		print("|#####|   |#####|")
		print("|# 3 #|   |# 4 #|")
		print("|#####|   |#####|")
		print("|#####|   |#####|")
		print(" -----     -----")
	
	def showCard(self, number):
		self.hand[number-1].show()
		
	def test(self):
		print(len(self.hand[0].getCard()))
	
	def displayScore(self):
		for card in self.hand:
			self.score += card.getValue()
		
		print(f"Your final score is {self.score}")
		
		


			
		
deck = Deck()
deck.shuffle()


player = Player("Player1")
player.deal(deck)
player.displayGrid()

player.showHand()
player.displayScore()
