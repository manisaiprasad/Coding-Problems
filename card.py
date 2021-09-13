import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class DeckCards:
    def __init__(self):
        self.deckOfCards = []
        self.suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.ranks = ['ace', 2, 3, 4, 5, 6, 7,
                      8, 9, 10, 'jack', 'queen', 'king']

    def createCards(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.deckOfCards.append(Card(rank, suit))

    def printCard(self, rank, suit, postion):
        print("The {0} card is the {1} of {2}!".format(postion, rank, suit))

    def peekCard(self):
        #  Example: "The top card is the Ace of Spades!"
        peek = len(self.deckOfCards) - 1
        self.printCard(self.deckOfCards[peek].rank,
                       self.deckOfCards[peek].suit, "Top")

    def bottomCard(self):
        self.printCard(self.deckOfCards[0].rank,
                       self.deckOfCards[0].suit, "Bottom")

    def shuffleCards(self):
        # rondom __init__
        # array 2,5,6,7,
        shuffledcars = []
        for i in range(52):
            length = len(self.deckOfCards)
            randomNumber = random.randint(0, length-1)
            shuffledcars.append(self.deckOfCards[randomNumber])
            value = self.deckOfCards[randomNumber]
            self.deckOfCards.remove(value)

        self.deckOfCards = shuffledcars


cards = DeckCards()
cards.createCards()
cards.peekCard()
cards.bottomCard()
cards.shuffleCards()
cards.peekCard()
