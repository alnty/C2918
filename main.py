#игра в дурака

import random
import time

time.sleep(5)

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
ten_of_hearts = "Ten of hearts"
ten_of_diamonds = "Ten of diamonds"
ten_of_clubs = "Ten of clubs"
ten_of_spades = "Ten of spades"
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
hearts_cube = random.randint(1, 14)
if hearts_cube == 1:
    print("You got Ace of hearts ❤")
    heart_card = ace_of_hearts
elif hearts_cube == 2:
    print("You got One of hearts ❤")
    heart_card = one_of_hearts
elif hearts_cube == 3:
    print("You got Two of hearts ❤")
    heart_card = two_of_hearts
elif hearts_cube == 4:
    print("You got Three of hearts ❤")
    heart_card = three_of_hearts
elif hearts_cube == 5:
    print("You got Four of hearts ❤")
    heart_card = four_of_hearts
elif hearts_cube == 6:
    print("You got Five of hearts ❤")
    heart_card = five_of_hearts
elif hearts_cube == 7:
    print("You got Six of hearts ❤")
    heart_card = six_of_hearts
elif hearts_cube == 8:
    print("You got Seven of hearts ❤")
    heart_card = seven_of_hearts
elif hearts_cube == 9:
    print("You got Eight of hearts ❤")
    heart_card = eight_of_hearts
elif hearts_cube == 10:
    print("You got Nine of hearts ❤")
    heart_card = nine_of_hearts
elif hearts_cube == 11:
    print("You got Ten of hearts ❤")
    heart_card = ten_of_hearts
elif hearts_cube == 11:
    print("You got Jack of hearts ❤")
    heart_card = jack_of_hearts
elif hearts_cube == 12:
    print("You got Queen of hearts ❤")
    heart_card = queen_of_hearts
elif hearts_cube == 13:
    print("You got King of hearts ❤")
    heart_card = king_of_hearts


diamonds_cube = random.randint(1, 14)
if diamonds_cube == 1:
    print("You got Ace of diamonds ♦")
    diamond_card = ace_of_diamonds
elif diamonds_cube == 2:
    print("You got One of diamonds ♦")
    diamond_card = one_of_diamonds
elif diamonds_cube == 3:
    print("You got Two of diamonds ♦")
    diamond_card = two_of_diamonds
elif diamonds_cube == 4:
    print("You got Three of diamonds ♦")
    diamond_card = three_of_diamonds
elif diamonds_cube == 5:
    print("You got Four of diamonds ♦")
    diamond_card = four_of_diamonds
elif diamonds_cube == 6:
    print("You got Five of diamonds ♦")
    diamond_card = five_of_diamonds
elif diamonds_cube == 7:
    print("You got Six of diamonds ♦")
    diamond_card = six_of_diamonds
elif diamonds_cube == 8:
    print("You got Seven of diamonds ♦")
    diamond_card = seven_of_diamonds
elif diamonds_cube == 9:
    print("You got Eight of diamonds ♦")
    diamond_card = eight_of_diamonds
elif diamonds_cube == 10:
    print("You got Nine of diamonds ♦")
    diamond_card = nine_of_diamonds
elif diamonds_cube == 11:
    print("You got Ten of diamonds ♦")
    diamond_card = ten_of_diamonds
elif diamonds_cube == 11:
    print("You got Jack of diamonds ♦")
    diamond_card = jack_of_diamonds
elif diamonds_cube == 12:
    print("You got Queen of diamonds ♦")
    diamond_card = queen_of_diamonds
elif diamonds_cube == 13:
    print("You got King of diamonds ♦")
    diamond_card = king_of_diamonds


clubs_cube = random.randint(1, 14)
if clubs_cube == 1:
    print("You got Ace of clubs ♣")
    club_card = ace_of_clubs and 14
elif clubs_cube == 2:
    print("You got One of clubs ♣")
    club_card = one_of_clubs and 1
elif clubs_cube == 3:
    print("You got Two of clubs ♣")
    club_card = two_of_clubs and 2
elif clubs_cube == 4:
    print("You got Three of clubs ♣")
    club_card = three_of_clubs and 3
elif clubs_cube == 5:
    print("You got Four of clubs ♣")
    club_card = four_of_clubs and 4
elif clubs_cube == 6:
    print("You got Five of clubs ♣")
    club_card = five_of_clubs and 5
elif clubs_cube == 7:
    print("You got Six of clubs ♣")
    club_card = six_of_clubs and 6
elif clubs_cube == 8:
    print("You got Seven of clubs ♣")
    club_card = seven_of_clubs and 7
elif clubs_cube == 9:
    print("You got Eight of clubs ♣")
    club_card = eight_of_clubs and 8
elif clubs_cube == 10:
    print("You got Nine of clubs ♣")
    club_card = nine_of_clubs and 9
elif clubs_cube == 11:
    print("You got Ten of clubs ♣")
    club_card = ten_of_clubs and 10
elif clubs_cube == 11:
    print("You got Jack of clubs ♣")
    club_card = jack_of_clubs and 11
elif clubs_cube == 12:
    print("You got Queen of clubs ♣")
    club_card = queen_of_clubs and 12
elif clubs_cube == 13:
    print("You got King of clubs ♣")
    club_card = king_of_clubs and 13


spades_cube = random.randint(1, 14)
if spades_cube == 1:
    print("You got Ace of spades ♠")
    spades_card = ace_of_spades
elif spades_cube == 2:
    print("You got One of spades ♠")
    spades_card = one_of_spades
elif spades_cube == 3:
    print("You got Two of spades ♠")
    spades_card = two_of_spades
elif spades_cube == 4:
    print("You got Three of spades ♠")
    spades_card = three_of_spades
elif spades_cube == 5:
    print("You got Four of spades ♠")
    spades_card = four_of_spades
elif spades_cube == 6:
    print("You got Five of spades ♠")
    spades_card = five_of_spades
elif spades_cube == 7:
    print("You got Six of spades ♠")
    spades_card = six_of_spades
elif spades_cube == 8:
    print("You got Seven of spades ♠")
    spades_card = seven_of_spades
elif spades_cube == 9:
    print("You got Eight of spades ♠")
    spades_card = eight_of_spades
elif spades_cube == 10:
    print("You got Nine of spades ♠")
    spades_card = nine_of_spades
elif spades_cube == 11:
    print("You got Ten of spades ♠")
    spades_card = ten_of_spades
elif spades_cube == 11:
    print("You got Jack of spades ♠")
    spades_card = jack_of_spades
elif spades_cube == 12:
    print("You got Queen of spades ♠")
    spades_card = queen_of_spades
elif spades_cube == 13:
    print("You got King of spades ♠")
    spades_card = king_of_spades

print("Now, computer need to get cards...")
time.sleep(10)

comp_cards_cube = random.randint(1, 3)
if comp_cards_cube == 1:
    first_ch_card = ten_of_hearts
    second_ch_card = seven_of_diamonds
    third_ch_card = jack_of_clubs
    fourth_ch_card = king_of_spades
    card_choose = input("It's your time to shine! Choose a card you want to start with.\n")
    if card_choose == club_card:
        if club_card > third_ch_card and first_ch_card != club_card and third_ch_card != club_card and fourth_ch_card != club_card:
             print("Seems like it's Computer's card now!")
if comp_cards_cube == 2:
    first_ch_card = one_of_hearts
    second_ch_card = six_of_diamonds
    third_ch_card = queen_of_clubs
    fourth_ch_card = four_of_spades
    card_choose = input("It's your time to shine! Choose a card you want to start with.\n")
    if card_choose == heart_card:
        if heart_card > first_ch_card and second_ch_card != heart_card and third_ch_card != heart_card and fourth_ch_card != heart_card:
             print("Seems like it's Computer's card now!")
        if heart_card < first_ch_card or second_ch_card == heart_card or third_ch_card == heart_card or fourth_ch_card == heart_card:
            to_choose = random.randint(1,4)
            if to
    if card_choose == diamond_card:
        if diamond_card > third_ch_card and second_ch_card != diamond_card and first_ch_card != diamond_card and fourth_ch_card != diamond_card:
             print("Seems like it's Computer's card now!")
    if card_choose == club_card:
        if club_card > third_ch_card and first_ch_card != club_card and third_ch_card != club_card and fourth_ch_card != club_card:
             print("Seems like it's Computer's card now!")
    if card_choose == spades_card:
        if spades_card > fourth_ch_card and first_ch_card != spades_card and third_ch_card != spades_card and third_ch_card != spades_card:
             print("Seems like it's Computer's card now!")
if comp_cards_cube == 3:
    first_ch_card = nine_of_hearts
    second_ch_card = ace_of_diamonds
    third_ch_card = two_of_clubs
    fourth_ch_card = eight_of_spades
    card_choose = input("It's your time to shine! Choose a card you want to start with.\n")
    if card_choose == club_card:
        if club_card > third_ch_card and first_ch_card != club_card and third_ch_card != club_card and fourth_ch_card != club_card:
             print("Seems like it's Computer's card now!")