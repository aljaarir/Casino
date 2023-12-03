import os
import random

class BlackjackGame:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
        self.money = 0
        self.bet = 0
        self.count = 0

    def deal(self):
        hand = []
        for i in range(2):
            random.shuffle(self.deck)
            card = self.deck.pop()
            if card == 11:
                card = "J"
            elif card == 12:
                card = "Q"
            elif card == 13:
                card = "K"
            elif card == 14:
                card = "A"
            hand.append(card)
        return hand

    def play(self):
        start = input("Do you want to play Blackjack? (Y/N) : ").lower()
        if start == "y":
            self.dealer_hand = []
            self.player_hand = []
            self.count += 1
            if self.count == 1:
                self.money = 10000
            print("You have $" + str(self.money))
            self.bet = int(input("Start initial bet "))

            if self.bet > self.money:
                print("You don't have enough money, please rerun the program to keep gambling!")
                self.play()

            if self.money == 0 or self.bet == 0:
                print("You don't have a penny to your name, please leave the table :(")
                exit()
              
            self.money -= self.bet
            self.game()
        else:
            print("Bye!")
            exit()

    def total(self, hand):
        total = 0
        for card in hand:
            if card == "J" or card == "Q" or card == "K":
                total += 10
            elif card == "A":
                if total >= 11:
                    total += 1
                else:
                    total += 11
            else:
                total += card
        return total

    def hit(self, hand):
        card = self.deck.pop()
        if card == 11:
            card = "J"
        elif card == 12:
            card = "Q"
        elif card == 13:
            card = "K"
        elif card == 14:
            card = "A"
        hand.append(card)
        return hand

    def clear(self):
        if os.name == 'posix':
            os.system('clear')

    def score(self):
        if self.total(self.player_hand) == 21:
            self.print_results()
            print("Congratulations! You got a Blackjack!\n")
            self.money += (self.bet * 2)
            print("Your new balance is: $" + str(self.money))
        elif self.total(self.dealer_hand) == 21:
            self.print_results()
            print("Sorry, you lose. The dealer got a blackjack.\n")
            self.money -= self.bet
            print("Your new balance is: $" + str(self.money))
        elif self.total(self.player_hand) > 21:
            self.print_results()
            print("Sorry. You busted. You lose.\n")
            self.money -= self.bet
            print("Your new balance is: $" + str(self.money))
        elif self.total(self.dealer_hand) > 21:
            self.print_results()
            print("Dealer busts. You win!\n")
            self.money += (self.bet * 2)
            print("Your new balance is: $" + str(self.money))
        elif self.total(self.player_hand) < self.total(self.dealer_hand):
            self.print_results()
            print("Sorry. Your score isn't higher than the dealer. You lose.\n")
            self.money -= self.bet
            print("Your new balance is: $" + str(self.money))
        elif self.total(self.player_hand) > self.total(self.dealer_hand):
            self.print_results()
            print("Congratulations. Your score is higher than the dealer. You win\n")
            self.money += (self.bet * 2)
            print("Your new balance is: $" + str(self.money))

    def print_results(self):
        self.clear()
        print("The dealer has a " + str(self.dealer_hand) + " for a total of " + str(self.total(self.dealer_hand)))
        print("You have a " + str(self.player_hand) + " for a total of " + str(self.total(self.player_hand)))

    def blackjack(self):
        if self.total(self.player_hand) == 21:
            self.print_results()
            print("Congratulations! You got a Blackjack!\n")
            self.play()
        elif self.total(self.dealer_hand) == 21:
            self.print_results()
            print("Uh Oh, you lose. The dealer got a blackjack.\n")
            self.play()

    def game(self):
        choice = 0
        self.clear()
        print("WELCOME TO BLACKJACK!\n")
        self.dealer_hand = self.deal()
        self.player_hand = self.deal()
        while choice != "q":
            print("The dealer is showing a " + str(self.dealer_hand[0]))
            print("You have a " + str(self.player_hand) + " for a total of " + str(self.total(self.player_hand)))
            self.blackjack()
            choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
            self.clear()
            if choice == "h":
                self.hit(self.player_hand)
                while self.total(self.dealer_hand) < 17:
                    self.hit(self.dealer_hand)
                self.score()
                self.play()
            elif choice == "s":
                while self.total(self.dealer_hand) < 17:
                    self.hit(self.dealer_hand)
                self.score()
                self.play()
            elif choice == "q":
                print("99 of gamblers quit before hitting it big, don't be a quitter.")
                exit()
