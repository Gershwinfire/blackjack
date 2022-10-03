from blackjackhelpers import Shoe, Player, Dealer, countyDots




class GameLogic(object):

    def __init__(self, player, dealer, shoe):

        self.player = player
        self.dealer = dealer
        self.gameShoe = shoe

    
    def beginGame(self):

        self.dealer.hand = []
        self.player.hand = []

        #initalize the players first bet
        self.player.placeBet()

        #initialize the shoe of cards (5 decks of cards)
        self.gameShoe.buildShoe()
        

        self.player.hand.append(self.gameShoe.dealCard())
        self.dealer.hand.append(self.gameShoe.dealCard())
        self.player.hand.append(self.gameShoe.dealCard())
        self.dealer.hand.append(self.gameShoe.dealCard())

        self.player.showHand()
        self.player.calculateScore()
        countyDots()
        self.dealer.showHand()              #These need to be changed so that they reflect one face up card
        self.dealer.calculateScore()        #and one face down card
        countyDots()

        self.playerAction(self.player.getAction())

    def keepPlaying(self):

        userResponse = input("\nPRESS ENTER FOR NEXT HAND\nType 'EXIT' to quit game\n")
        userResponse = userResponse.lower().strip()

        if userResponse == "":
            self.beginGame()

        elif userResponse == "exit":
            exit()

        else:
            self.keepPlaying()
    
    def playerAction(self, action):

        

        if action == "hit":
            print("You chose to Hit")

            #player takes on an additional card
            self.player.hand.append(self.gameShoe.dealCard())
            self.player.showHand()
            self.player.calculateScore()


            if self.player.score <= 21:
                newAction = self.player.getAction()
                self.playerAction(newAction)

            elif self.player.score > 21:
                print("BUSTED!!! YOU LOSE")
                #Proceed to 
                self.dealer.showHand()

                #set currentbet to 0
                self.player.bet = 0

                self.keepPlaying()
                    #show dealers hand for good faith
                    #set player bet to 0
                    #set forth with "would you like to play another round"

            #if player total score isnt higher than 21, we ask the same question
                #if the player total score is higher than 21, we end the game immediately and proceed to ask endgame()

        elif action == "stand":
            print("You chose to STAND\n")

            #if action is to stand then we need to proceed forward with the game logic for the dealer.
            self.dealer.showHand()
            self.dealer.calculateScore()

            while self.dealer.score < 16:
                countyDots()
                self.dealer.hand.append(self.gameShoe.dealCard())
                self.dealer.showHand()
                self.dealer.calculateScore()
                


            if self.dealer.score > 21:
                print("The dealer has busted!")
                
                #pay the player the player 2times their bet
                payout = self.player.bet * 2
                self.player.balance += payout
                print(f"{self.player.name} WON {self.player.bet}")
                self.player.showBalance()

                #reset bet to 0 for the next round
                self.player.bet = 0
                self.keepPlaying()

            
            elif self.dealer.score <= 21 and self.dealer.score >= 16:
                
                if self.player.score > self.dealer.score:
                    print("The player WINS!")
                    #pay the player the player 2times their bet
                    payout = self.player.bet * 2
                    self.player.balance += payout
                    print(f"{self.player.name} WON {self.player.bet}")
                    self.player.showBalance()

                    #reset bet to 0 for the next round
                    self.player.bet = 0
                    self.keepPlaying()


                elif self.player.score <= self.dealer.score:
                    print("The PLAYER LOSES!")
                    print(f"{self.player.name} LOST {self.player.bet}")
                    self.player.showBalance()

                    #reset bet to 0 for the next round
                    self.player.bet = 0
                    self.keepPlaying()    

        else:
            print("Some Real Bad shit happened herrrrrr")


    















#initialize a dealer
dealer1 = Dealer()

#initialize a player
player1 = Player()

#initialize a game shoe
gameShoe = Shoe()

#Initialize GamePlay
game = GameLogic(player1, dealer1, gameShoe)

#Begin Game Play
game.beginGame()



