import time, itertools, random



def countyDots():
    for i in range(5):
            line = "." * i
            print(line, end="")
            print("\r", end="")
            time.sleep(0.5)



class Card(object):

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit

        self.valueChart = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "Q": 10,
            "K": 10,
            "A": 11,
        }


    def getValues(self):

        cardValues = self.valueChart
        returnedValue = 0

        for rank, value in cardValues.items():

            if self.rank == rank:
                returnedValue = value

        return returnedValue  
        



class Player(object):

    def __init__(self):
        self.name = self.defineName()

        #initialize player bank to $200
        self.balance = 200
        print("Beginning Balance: $200.00 USD\n")

        ##initialize player hand
        self.hand = []
        

        #initialize score and currentBet to 0
        self.score = 0


        self.bet = 0


    def placeBet(self):
        
        currentBet = input(f"BALANCE: ${self.balance}\nHow much would you like to bet? (1, 2, 5, 10, 25):  ")
        
        def is_number(n):
            try:
                int(n)# Type-casting the string to `float`.
                        # If string is not a valid `float`, 
                        # it'll raise `ValueError` exception
            except ValueError:
                return False
            return True

        if is_number(currentBet):
            currentBet = int(currentBet)
            if currentBet in (1, 2, 5, 10, 25):
                self.balance -= currentBet
                self.bet = currentBet
                print(f"\nCurrent Bet: {currentBet}\nBALANCE: {self.balance}\n")
            else:
                self.placeBet()
        else:
            self.placeBet()


        
    def defineName(self):

        #Ask for name from user
        newName = input("What is your Name?:  ")

        #confirm new name with user
        confirmation = input(f"Your name is {newName}, correct? (Y/N):   ")
        
        #convert confirmation to all lowercase and eliminate whitespace
        confirmation = confirmation.lower().strip()

        while confirmation != "y":

            newName = input("Sorry. What is your Name?:  ")
            countyDots()
            confirmation = input(f"So you prefer to be called {newName}?  (Y/N):   ")
            confirmation = confirmation.lower().strip()

        if confirmation == "y":
            return newName
            

    def showHand(self):

        print(f"{self.name}'s HAND")

        for card in self.hand:
            rank = card[0]
            suit = card[1]
            print(f"{rank} of {suit}")



    def getAction(self):

        action = input("Would you like to HIT or STAND?:  ")

        action = action.lower().strip()

        return action


    def calculateScore(self):

        self.score = 0

        for card in self.hand:
            rank = card[0]
            suit = card[1]
            card = Card(rank, suit)
            

            value = card.getValues()
            self.score += value
        
        print(f"{self.name}'s SCORE: {self.score}\n")
        return self.score

    def showBalance(self):

        print(f"BALANCE: {self.balance}")






class Dealer(object):

    def __init__(self):
        self.name = "Dealer"

        #initialize a dealer score to 0
        self.score = 0

        #initialize a dealer hand
        self.hand = []

        #initialize a dealer bank of 1,000,000
        self.bank = 1000000


    def showHand(self):

        print(f"{self.name}'s HAND")

        for card in self.hand:
            rank = card[0]
            suit = card[1]
            print(f"{rank} of {suit}")

        


    def calculateScore(self):

        self.score = 0

        for card in self.hand:
            rank = card[0]
            suit = card[1]
            card = Card(rank, suit)
            

            value = card.getValues()
            self.score += value
        
        print(f"{self.name}'s SCORE: {self.score}\n")
        return self.score

    






class Deck(object):


    def __init__(self):

        self.deck = []
        self.ranks = (
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
            "A",
        )



    def buildDeck(self):

        suits = ("Spades ♠", "Clubs ♣", "Hearts ♥", "Diamonds ♦")
        cards = list(itertools.product(self.ranks, suits))
        random.shuffle(cards)

        for card in cards:
            self.deck.append(card)

        return self.deck


class Shoe(Deck):

    def __init__(self):

        self.shoe = []

    
    def buildShoe(self):

        for i in range(5):


            newDeck = Deck()
            newDeck.buildDeck()
            for card in newDeck.deck:
                self.shoe.append(card)

    
    def dealCard(self):

        gameDeck = self.shoe
        dealtCard = self.shoe[0]
        self.shoe.pop(0)

        return dealtCard

    









    

