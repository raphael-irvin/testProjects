import random
import os

os.system('CLS' if os.name=='nt' else 'clear')

class Deck:
    def __init__(self):
        self.main_deck = []
        for x in range(1,26):
            self.main_deck.append(x)

class User:
    def __init__(self, username):
        self.username = username
        self.card_in_hand = []
        for x in range(5):
            self.card_in_hand.append(main_deck.main_deck.pop(random.randrange(0, len(main_deck.main_deck))))
        print(f'Your cards are: {self.card_in_hand}') #pop card from deck to hand
        NPC.__init__(self) #get opponent card
        User.choose_action(self) #go to action list

    def choose_action(self):
        print("Type (1) to Re-Deal your card")
        print("Type (2) to Show your card")
        user_action = 0
        while True:
            user_action = input(f'Please type your action, {self.username}: ')
            try:
                user_action = int(user_action)
                break
            except:
                print("Error! Please type a valid response!")
                pass

        if user_action == 1:
                User.redealcard(self) #return current card, get 5
                NPC.redealcard(self) #return current card, get 5
                User.choose_action(self)

        if user_action == 2:
                Game.run_game(self) #run game
                Game.ending_screen(self) #end screen

    def redealcard(self):
        for x in self.card_in_hand:
            main_deck.main_deck.append(x)
        self.card_in_hand = []
        for x in range(5):
            self.card_in_hand.append(main_deck.main_deck.pop(random.randrange(0, len(main_deck.main_deck))))
        print(f'Your new cards are: {self.card_in_hand}') #Pop card from deck to hand

    def get_my_card(self):
        return self.card_in_hand
    
    def return_card_to_deck(self):
        for x in self.card_in_hand:
            main_deck.main_deck.append(x)

class NPC:
    def __init__(self):
        self.opponent_name = f'User 0{random.randrange(100, 999)}'
        self.opponent_card = []
        for x in range(5):
            self.opponent_card.append(main_deck.main_deck.pop(random.randrange(0, len(main_deck.main_deck))))

    def redealcard(self):
        for x in self.opponent_card:
            main_deck.main_deck.append(x)
        self.opponent_card = []
        for x in range(5):
            self.opponent_card.append(main_deck.main_deck.pop(random.randrange(0, len(main_deck.main_deck))))

    def return_card_to_deck(self):
        for x in self.opponent_card:
            main_deck.main_deck.append(x)

class Game:
    def __init__(self):
        pass

    def run_game(self): #run main game (value comparison) system
        os.system('CLS' if os.name=='nt' else 'clear')
        print("MATCH BEGINS!")
        print(f'{self.opponent_name} Cards are: {self.opponent_card}')
        print(f'The value is: {sum(self.opponent_card)}')
        print("")
        print(f'Your card is: {User.get_my_card(self)}')
        print(f'The value is: {sum(User.get_my_card(self))}')
        print("")

        if sum(User.get_my_card(self)) > sum(self.opponent_card):
            print(f'Congratulations, You Won by {sum(User.get_my_card(self)) - sum(self.opponent_card)}')

        if sum(User.get_my_card(self)) < sum(self.opponent_card):
            print(f'Bad Luck! You lost by {sum(self.opponent_card) - sum(User.get_my_card(self))}')
        
        User.return_card_to_deck(self)
        NPC.return_card_to_deck(self)

    def ending_screen(self):
        print("")
        print("Do you want to play again?")
        while True:
            self.user_response = input("(1) YES / (2) NO: ")
            try:
                self.user_response = int(self.user_response)
                break
            except:
                print("ERROR! Please type a valid Number: ")

        if self.user_response == 1:
            global username
            username = User(username)
        elif self.user_response == 2:
            os.system('CLS' if os.name == "nt" else 'clear')
            print("Thank you for Playing!")
        else:
            print("Sorry, unregistered action, please try again!")
            print("")
            Game.ending_screen(self)

main_deck = Deck() #Setup Deck

user = input("Please type your name: ")
user = User(user) #Install User as Class