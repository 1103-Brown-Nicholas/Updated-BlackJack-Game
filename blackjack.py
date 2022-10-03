import random, itertools, functools,re
from time import sleep

class Intro:
    def introduction(self):
        print("***WELCOME TO BLACKJACK***")
        sleep(2)
        print("***GOODLUCK, MAY FORTUNE BE ON YOUR SIDE***")
        sleep(2)

class Cards:
    def deck(self):
        deck = list(itertools.product(range(1,14), ['SPADE','DIAMOND','CLUB','HEART']))    
        return deck

    def shuffle(self):
        newDeck = Cards.deck(self)
        random.shuffle(newDeck)
        return newDeck
        
class Deal:
    def randomDeal(self):
        pHand = []
        hHand = []
        dealIter = 0
        dealer = Cards.shuffle(self)
        x = 0
        
        while dealIter < 4:
            pHand.append(dealer[x])
            dealer.remove(dealer[x])
            dealIter += 1
            x += 1
            hHand.append(dealer[x])
            dealer.remove(dealer[x])
            dealIter += 1
            x += 1

        return pHand,hHand,dealer

class Hands:
    def makingHand(self):
        hands = Deal().randomDeal()
        playerHand = [hands[0]]
        houseHand = [hands[1]]
        updatedDeck = hands[2]

        return playerHand,houseHand,updatedDeck

class Updatehands:
    def playerHit(self,deck):
        x = 0
        newCard = []
        newCard.append(deck[x])
        deck.remove(newCard[x])

        return newCard,deck

    def originalSum(self,firstHand):
        originalSum = firstHand[0][0][0] + firstHand[0][1][0]
        
        return originalSum

    def newSum(self,firstSum,newCard):
        newSum = firstSum + newCard[0][0]

        return newSum

class Outcome:
    def rankComp(self,playerSum,houseSum):
        if(playerSum and houseSum < 21):
            if(playerSum > houseSum):
                print("\nThe player won the hand!")
            
            elif(playerSum == houseSum):
                print("\nIt is a push!")
            
            else:
                print("\nThe house won the hand!")

        elif(playerSum > 21):
            print("\nThe player busted!")

        elif(houseSum > 21):
            print("\nThe house busted!")
       
    def hitorStand(self,playerSum,houseSum,hands):
        while(playerSum < 21):
            if(playerSum < 21):
                hit = input("Would you like to [H]it or [S]tand?").upper()
                if(hit == "H"):
                    newCard = Updatehands().playerHit(hands[2])
                    hands[0].append(newCard[0])
                    print("Your hand is: ",hands[0])
                    print("The house has: ",hands[1])
                    playerSum = Updatehands().newSum(playerSum,newCard[0])    
                    
                elif(hit == "S"):
                    winner = Outcome().rankComp(playerSum,houseSum)
                    return winner
                
                elif(hands[0][0][0][0] + hands[0][0][1][0] == 21):
                    print("BLACK JACK!")

                else:
                    print("You chose to stand.")


    def houseHit(self,houseSum,hands):
        if(houseSum < 17):
            newhouseCard = Updatehands().playerHit(hands[2])
            hands[1].append(newhouseCard[0])
            print("The house has: ",hands[1])
            houseSum = Updatehands().newSum(houseSum,newhouseCard[0])


class Initialhands:
    def initialPLayer(self,hands):
         playerSum = Updatehands().originalSum(hands[0])
         print("Your hand is: ",hands[0])
         return playerSum

    def initialHouse(self,hands):
        houseSum =  Updatehands().originalSum(hands[1])
        print("The house has: ",hands[1])
        print("\n")
        return houseSum

class Main:
    def mainFunction(self): 
        Intro().introduction()   
        x = True
        while(x):
            hands = Hands().makingHand()
            playerSum = Initialhands().initialPLayer(hands)
            houseSum = Initialhands().initialHouse(hands)
            Outcome().houseHit(houseSum,hands)
            winner = Outcome().hitorStand(playerSum,houseSum,hands)

Main().mainFunction()   