import requests
# all of these are designed to return the giant motherload of a deck dictionary
# gets the basic deck with no arguments needed
def get_deck(url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"):
    response = requests.get(url)
    return response.json() 
# this is same as function above it just renamed for clarity and removed default argument 
def get_url_response(url):
    response = requests.get(url)
    r = response.json()
    return r
# pulls cards from main deck
def get_cards(_id, amount):
    get_url = f"https://deckofcardsapi.com/api/deck/{_id}/draw/?count={amount}"
    response = requests.get(get_url)
    cards = response.json()
    
    # hand = []
    # for card in cards:
    #     nice_card = card["value"] + " of " + card["suit"]
    #     hand.append(nice_card)
    # 
    return cards
# This moves specific cards from main to a pile like 'player 1'
def move_cards(deck_id, pile_name, card_list):
    cards = []
    for card in card_list:
        cards.append(card["code"])
    card_codes = ""
    for card in cards:
        card_codes += card + ","
    card_codes = card_codes[:-1] # just removes last item in the string the ","
    print(card_codes)
    move_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile_name}/add/?cards={card_codes}"
    print(move_url)
    r = get_url_response(move_url)
    return r
# pulls cards from specific pile
def get_pile_cards(_id, pile_name ,amount):
    get_url = f"https://deckofcardsapi.com/api/deck/{_id}/pile/{pile_name}/draw/?count={amount}"
    response = requests.get(get_url)
    cards = response.json()
    return cards
# This is interesting this moved the cards dict to current pile rather than adding and ajusting one 
def list_pile_cards(_id, pile_name):
    list_url = f"https://deckofcardsapi.com/api/deck/{_id}/pile/{pile_name}/list/"
    r = get_url_response(list_url)
    return r
# This fully resets the entire dictionary and shuffle order randoly and removes any and all piles 
def shuffle(_id):
    get_url = f"https://deckofcardsapi.com/api/deck/{_id}/shuffle/"
    response = requests.get(get_url)
    return response.json()  
# this dosn't do anything with the deckofcards api just is a fancier 
# input function that detects and tries to auto scrub responces and set to 
# apporpiate data types like int str bool. text what is printed on screen
#just handy in general
# only supports str ints and bools tho
def get_response(text):
    player_response = input(text)
    stripped_player_response = player_response.strip()
    nice_player_response = stripped_player_response.lower()
    # makes the response useable 

    # checks if y/n and sets it to false or True

    if nice_player_response == "y":
        return True
    elif nice_player_response == "n":
        return False
    # checks if y/n and sets it to false or True

    # checks if player input is a number
    # print(nice_player_response)
    # print(type(nice_player_response))
    try:
        old_player_response = nice_player_response
        nice_player_response = int(nice_player_response)
        nums = [1,2,3,4,5,6,7,8,9,0]
        if  nice_player_response in nums:
            return int(nice_player_response)
    except:
        nice_player_response = old_player_response
    return nice_player_response



     
