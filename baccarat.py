import os
import random
import time
# not finished yet
class BaccaratGame:
    def __init__(self):
        self.deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0] * 8
        self.money = 0
        self.bet = 0
        self.count = 0

    def deal(self):
        hand = []
        for i in range(2):
            random.shuffle(self.deck)
            card = self.deck.pop()
            hand.append(card)
        return hand

    def play(self):
        start = input("Do you want to play Baccarat? (Y/N) : ").lower()
        if start == "y":
            self.dealer_hand = self.deal()
            self.player_hand = self.deal()
            self.count += 1
            if self.count == 1:
                self.money = 10000
            print("You have $" + str(self.money))
            self.bet = int(input("Place bet: "))

            if self.bet > self.money:
                print("You don't have enough money, please rerun the program to keep gambling!")
                self.play()

            if self.money == 0 or self.bet == 0:
                print("You don't have a penny to your name, please leave the table :(")
                exit()

            self.game()
        else:
            print("Bye!")
            exit()

    def total(self, hand):
        total = sum(hand) % 10
        return total

    def hit(self, hand):
        card = self.deck.pop()
        hand.append(card)
        return hand

    def clear(self):
        if os.name == 'posix':
            os.system('clear')

    def score(self):
        player_total = self.total(self.player_hand)
        dealer_total = self.total(self.dealer_hand)

        print("The dealer has a " + str(self.dealer_hand[0]) + " and an unknown card")
        print("You have a " + str(self.player_hand) + " for a total of " + str(player_total))

        if player_total > dealer_total and player_total < 9:
            print("Congratulations. Your score is higher than the dealer. You win!\n")
            self.money += (self.bet * 2)
        elif player_total < dealer_total:
            print("Sorry. Your score isn't higher than the dealer. You lose.\n")
            self.money -= self.bet
        else:
            print("It's a tie!\n")

        print("Your new balance is: $" + str(self.money))

    def game(self):
      choice = 0
      self.clear()
      print("WELCOME TO BACCARAT\n")
      self.hit(self.player_hand)
      self.hit(self.dealer_hand) 

      #check for bacarat constraints
      if(self.total(self.player_hand) == 8  or self.total(self.player_hand) == 9):
        self.score
      if(self.total(self.dealer_hand) == 8  or self.total(self.dealer_hand) == 9):
        self.score
    
      while choice != "n":
          print("The dealer is showing a " + str(self.dealer_hand) + " and an unknown card")
          print("You have a " + str(self.player_hand) + " for a total of " + str(self.total(self.player_hand)))
          self.score()
    
          choice = input("Do you still want to play? (Y/N): ").lower()
      if choice == "n":
          print("99% of gamblers quit before hitting it big, don't be a quitter.")
          exit()
      elif choice == "y":
          self.clear()
          self.game()
    
