#игра в дурака

import random

ace_of_hearts = "Ace of hearts"
ace_of_diamonds = "Ace of diamonds"
ace_of_clubs = "Ace of clubs"
ace_of_spades = "Ace of spades"
one_of_hearts = "One of hearts"
one_of_diamonds = "One of diamonds"
one_of_clubs = "One of clubs"
one_of_spades = "One of spades"
two_of_hearts = "Two of hearts"
two_of_diamonds = "Two of diamonds"
two_of_clubs = "Two of clubs"
two_of_spades = "Two of spades"
three_of_hearts = "Three of hearts"
three_of_diamonds = "Three of diamonds"
three_of_clubs = "Three of clubs"
three_of_spades = "Three of spades"
four_of_hearts = "Four of hearts"
four_of_diamonds = "Four of diamonds"
four_of_clubs = "Four of clubs"
four_of_spades = "Four of spades"
five_of_hearts = "Five of hearts"
five_of_diamonds = "Five of diamonds"
five_of_clubs = "Five of clubs"
five_of_spades = "Five of spades"
six_of_hearts = "Six of hearts"
six_of_diamonds = "Six of diamonds"
six_of_clubs = "Six of clubs"
six_of_spades = "Six of spades"
seven_of_hearts = "Seven of hearts"
seven_of_diamonds = "Seven of diamonds"
seven_of_clubs = "Seven of clubs"
seven_of_spades = "Seven of spades"
eight_of_hearts = "Eight of hearts"
eight_of_diamonds = "Eight of diamonds"
eight_of_clubs = "Eight of clubs"
eight_of_spades = "Eight of spades"
nine_of_hearts = "Nine of hearts"
nine_of_diamonds = "Nine of diamonds"
nine_of_clubs = "Nine of clubs"
nine_of_spades = "Nine of spades"
jack_of_hearts = "Jack of hearts"
jack_of_diamonds = "Jack of diamonds"
jack_of_clubs = "Jack of clubs"
jack_of_spades = "Jack of spades"
queen_of_hearts = "Queen of hearts"
queen_of_diamonds = "Queen of diamonds"
queen_of_clubs = "Queen of clubs"
queen_of_spades = "Queen of spades"
king_of_hearts = "King of hearts"
king_of_diamonds = "King of diamonds"
king_of_clubs = "King of clubs"
king_of_spades = "King of spades"

print("Your cards:")
hearts_cube = random.randint(1, 15)
if hearts_cube == 1:
    print("You got Ace of hearts")
    heart_card = ace_of_hearts
if hearts_cube == 2:
    print("You got One of hearts")
    heart_card = one_of_hearts
if hearts_cube == 3:
    print("You got Two of hearts")
    heart_card = two_of_hearts