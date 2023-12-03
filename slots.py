import os
import random
import time

class slots:
    def __init__(self): # constructor
        self.deck = ['Cherry', 'Orange', 'Bar', 'Seven', 'Lemon','$','Apple']
        self.money = 0
        self.bet = 0
        self.count = 0
        self.slotmachine = []

    def gen(self):
      slotmachine = [] # need to make into a 3x3 array so it looks more like a slot machine
      for i in range(0, 3):
        # Randomly select a symbol from the list
        value = random.choice(self.deck)
        # Append the selected symbol to slotmachine
        slotmachine.append(value)
      return slotmachine

    def play(self):
        start = input("Do you want to play Slots? (Y/N) : ").lower()
        if start == "y":
            self.count += 1
            if self.count == 1:
                self.money = 10000
            print("You have $" + str(self.money))
            self.bet = int(input("Input coins:"))

            if self.bet > self.money:
                print("You don't have enough money, please rerun the program to keep gambling!")
                self.play()

            if self.bet == 0:
                print("Enter a valid bet")
                exit()

            self.money -= self.bet
            self.game()
        else:
            print("Say something im giving up on you...")
            exit()

    def clear(self): #idk how this works tbh
        if os.name == 'posix':
            os.system('clear')

    def score(self):
#checks for full matches
        if (self.slotmachine[0] == self.slotmachine[1] == self.slotmachine[2] == 7):
          self.money += (self.bet * 100)
          print("JACKPOT! You won 100x your bet!\n")
        elif (self.slotmachine[0] == self.slotmachine[1] == self.slotmachine[2] == 'Bar'):
          self.money += (self.bet * 50)
          print("HUGE DUB! You won 50x your bet!\n")
        elif (self.slotmachine[0] == self.slotmachine[1] == self.slotmachine[2] == '$'):
          self.money += (self.bet * 80)
          print("LETS GOOOO! You won 80x your bet!\n")
        elif (self.slotmachine[0] == self.slotmachine[1] == self.slotmachine[2] == 'Cherry'):
          self.money += (self.bet * 25)
          print("Congrats! You won 25x your bet!\n")
        elif (self.slotmachine[0] == self.slotmachine[1] == self.slotmachine[2] == 'Lemon'):
          self.money += (self.bet * 10)
          print("Congrats! You won 25x your bet!\n")
        elif (self.slotmachine[0] == self.slotmachine[1] == self.slotmachine[2] == 'Orange'):
          self.money += (self.bet * 5)
          print("Congrats! You won 25x your bet!\n")
#checks for half matches
        elif (self.slotmachine[0] == self.slotmachine[1] == 'Seven' or self.slotmachine[0] == self.slotmachine[2] == 'Seven' or self.slotmachine[1] == self.slotmachine[2] == 'Seven'):
          self.money += (self.bet * 2)
          print("You won 2x your bet!\n")
        elif (self.slotmachine[0] == self.slotmachine[1] == '$' or self.slotmachine[0] == self.slotmachine[2] == '$' or self.slotmachine[1] == self.slotmachine[2] == '$'):
          self.money += (self.bet * 1.8)
          print("You won 1.8x your bet!\n")
        elif (self.slotmachine[0] == self.slotmachine[1] == 'Bar' or self.slotmachine[0] == self.slotmachine[2] == 'Bar' or self.slotmachine[1] == self.slotmachine[2] == 'Bar'):
            self.money += (self.bet * 1.5)
            print("You won 1.5x your bet!\n")
        else:
          print("Just one more bet & you'll hit it big ;)")

    def print_centered(self, text):
      width = 25 
      padding = (width - len(text)) // 2
      print(" " * padding + text + " " * padding)

    def display_slowly(self, items):
      print("||", end='', flush=True)
      for item in items:
          print(item, end='||', flush=True)  # Print the item followed by "||"
        #  flush=True will force our terminal to print it. flush does not matter if end=\n
          time.sleep(0.5)  
      print()  # Print a newline after displaying all items
    

    def game(self):
      choice = 0
      self.clear()
      print("WELCOME TO RYAN'S SLOT MACHINE!\n")
      self.slotmachine = self.gen() # RNG slot machine
      self.clear()
      while choice != "q":
        self.print_centered("Slot Machine result:")
        self.print_centered("    -----------------    ")
        self.print_centered("  ---------------------  ")
        self.print_centered("-------------------------")
        self.display_slowly(self.slotmachine)
        self.print_centered("-------------------------")
        self.print_centered("-------------------------")
        self.print_centered("-{Cash out}-------{SPIN}-")
        self.print_centered("--||----------------||--")
        self.print_centered("-------------------------\n")
        self.score()
        print("You have $" + str(self.money))
        choice = input("Do you want to [P]lay again, [C]hange bet size or [Q]uit: ").lower()
        if self.money == 0:
          print("You are broke :(")
          exit()
        if choice == "p":
            self.money -= self.bet
            self.count += 1
            self.game()
            self.clear()
        if choice == "c":
            self.play()
        elif choice == "q":
            print("Thanks for playing! Your final balance is: $" + str(self.money))
            exit()
        else:
          print("Enter a valid input")
          choice = input("Do you want to [P]lay again or [Q]uit: ").lower()
          exit()
            
