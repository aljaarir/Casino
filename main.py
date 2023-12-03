from blackjack_game import BlackjackGame
from slots import slots #get files
from baccarat import BaccaratGame

def main():
  
  while True:
    print("Choose a game:")
    print("1. Blackjack")
    print("2. Slots")
    print("3. Baccarat")
    print("4. Quit")
  
    choice = input("Enter the number of your choice: ")
  
    if choice == "1":
        blackjack_game = BlackjackGame()
        blackjack_game.play()
    elif choice == "2":
        slots_game = slots()
        slots_game.play()
    elif choice == "3":
      baccarat_game = BaccaratGame()
      baccarat_game.play()
    elif choice == "4":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
