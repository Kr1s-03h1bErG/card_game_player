from functions import get_cards, get_deck, shuffle, get_response, give_hand, move_cards ,get_url_response, get_pile_cards, list_pile_cards

deck = get_deck()
deck_id = deck["deck_id"]
deck = get_cards(deck_id , 5)
print(deck)
deck = move_cards(deck_id, "player_1", deck["cards"])
print(deck)
deck = get_pile_cards(deck_id, "player_1", 3)
print(deck)
deck = list_pile_cards(deck_id, "player_1")
print(deck)
deck = shuffle(deck_id)
print(deck)