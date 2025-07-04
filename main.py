import random

# Code for building a deck of cards and drawing a card to the players hand taken from:
# https://www.youtube.com/watch?v=t8YkjDH86Y4

class Card(object):
	def __init__(self, suit, val):
		self.suit = suit
		self.value = val
		
	def show(self):
		print(f"{self.value} of {self.suit}")
	
	
class Deck(object):
	def __init__(self):
		self.cards = []
		self.build()
		
	def build(self):
		for s in ["Spades","Clubs","Diamonds","Hearts"]:
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
		self.topLine = []
		self.bottomLine = []
		self.grid = [self.topLine, self.bottomLine]
		
	def draw(self, deck):
		self.hand.append(deck.drawCard())
	
	def deal(self, deck):
		self.hand.append(deck.drawCard())
		self.hand.append(deck.drawCard())
		self.hand.append(deck.drawCard())
		self.hand.append(deck.drawCard())
		
	def showHand(self):
		for card in self.hand:
			card.show()
	
	def discard(self):
		return self.hand.pop()
	
	def addToGrid(self):
		self.topLine.append(self.hand[0])
		self.topLine.append(self.hand[1])
		self.bottomLine.append(self.hand[2])
		self.bottomLine.append(self.hand[3])
	
	def displayGrid(self):
		print(self.grid[0][0])

#https://stackoverflow.com/questions/76803097/python-noob-question-what-is-class-object-at-0x
			
		
deck = Deck()
deck.shuffle()


player = Player("Player1")
player.deal(deck)
player.showHand()
player.addToGrid()
player.displayGrid()
