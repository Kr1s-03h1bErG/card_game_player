from functions import get_cards, get_deck, shuffle, get_response, give_hand
# this function needs to change later just ported over from API Projcect 
# this is outdated just rements of copying api project 
def main():
    print("Welcome to Deck of Cards!")
    has_deck_id = get_response("Do you have a Deck ID? Y/N: ")
    # has_deck_id = False
    if has_deck_id:
        print("Thanks for having a ID")
    else: 
        deck = get_deck()
        deck_id = deck["deck_id"]
        print(f"Making new deck. deck_id: {deck_id}")
        print("Supported games Poker, BlackJack, GoFish, Rummy, Whist")
        while True:
            good = ["poker", "blackjack", "gofish", "rummy", "whist"]
            game = get_response("What game are you playing: ")
            if game in good:
                break
            else:
                print("please type the game name exactly")
        while True:
            hand_amount = get_response("How many hands do you need ")
            try: 
                hands = give_hand(deck_id , game, hand_amount)
                break
            except: # if they pulled to many cards 
                deck = shuffle(deck_id)
                print("Please enter a number of hands that dosn't go over the deck limit!")
        if game == "poker":
            print(f"Comunity cards: {hands[0]}")
            hands.pop(0)
        for hand in hands:
            print(f"hand: {hand}")
            input("type anything to continue")
            for i in range(10):
                print("")
# goal is to try to login a user and if they cant see if they need to register
def register():
    pass
# checks if user is in db returns Bool
def is_user_in_user(username, password)
    user_data = username + "," + password
    with open("user.txt", "r") as file:
        for line_number, line in enumerate(file, 1): # starts numbering at 1
            if user_data in line:
                return True
        return False

# def pull_user_data()
#checks Returns if it succeeded or failed (bool)
def login():
    need_login = get_response("Do you need to login? Y/N: ")
    if need_login:
        username = get_response("What is your Username?: ")
        password = get_response("What is your Password?: ")
        return is_user_in_user(username, password)
    else: # return that it failed to login so we can register later
        print("Failed to find name in db")
        return False
#Returns suceeded or failed (bool)
def add_user(username, password):
    with open("user.txt", "a") as file:
        file.write(f"{username},{password}::\n")
        return True

def register()
    need_register = get_response("Do you need to register? Y/N: ")
        if need_register:
            while True:
                username = get_response("What will be your Username?: ")
                password = get_response("What will be your Password?: ")
                if is_user_in_user(username, password):
                    print("username and password already in db restarting register")
                else:
                    break
            return add_user(username, password)
            
        else: # return that it failed to login so we can register later
            print("User Didn't need to register for new account")
            return False



# r = get_response("r: ")
# print(r)
# print(type(r))

