# гра в карти

import random
import time

time.sleep(5)

ace_of_hearts = "Ace of hearts", 14
ace_of_diamonds = "Ace of diamonds", 14
ace_of_clubs = "Ace of clubs", 14
ace_of_spades = "Ace of spades", 14
one_of_hearts = "One of hearts", 1
one_of_diamonds = "One of diamonds", 1
one_of_clubs = "One of clubs", 1
one_of_spades = "One of spades", 1
two_of_hearts = "Two of hearts", 2
two_of_diamonds = "Two of diamonds", 2
two_of_clubs = "Two of clubs", 2
two_of_spades = "Two of spades", 2
three_of_hearts = "Three of hearts", 3
three_of_diamonds = "Three of diamonds", 3
three_of_clubs = "Three of clubs", 3
three_of_spades = "Three of spades", 3
four_of_hearts = "Four of hearts", 4
four_of_diamonds = "Four of diamonds", 4
four_of_clubs = "Four of clubs", 4
four_of_spades = "Four of spades", 4
five_of_hearts = "Five of hearts", 5
five_of_diamonds = "Five of diamonds", 5
five_of_clubs = "Five of clubs", 5
five_of_spades = "Five of spades", 5
six_of_hearts = "Six of hearts", 6
six_of_diamonds = "Six of diamonds", 6
six_of_clubs = "Six of clubs", 6
six_of_spades = "Six of spades", 6
seven_of_hearts = "Seven of hearts", 7
seven_of_diamonds = "Seven of diamonds", 7
seven_of_clubs = "Seven of clubs", 7
seven_of_spades = "Seven of spades", 7
eight_of_hearts = "Eight of hearts", 8
eight_of_diamonds = "Eight of diamonds", 8
eight_of_clubs = "Eight of clubs", 8
eight_of_spades = "Eight of spades", 8
nine_of_hearts = "Nine of hearts", 9
nine_of_diamonds = "Nine of diamonds", 9
nine_of_clubs = "Nine of clubs", 9
nine_of_spades = "Nine of spades", 9
ten_of_hearts = "Ten of hearts", 10
ten_of_diamonds = "Ten of diamonds", 10
ten_of_clubs = "Ten of clubs", 10
ten_of_spades = "Ten of spades", 10
jack_of_hearts = "Jack of hearts", 11
jack_of_diamonds = "Jack of diamonds", 11
jack_of_clubs = "Jack of clubs", 11
jack_of_spades = "Jack of spades", 11
queen_of_hearts = "Queen of hearts", 12
queen_of_diamonds = "Queen of diamonds", 12
queen_of_clubs = "Queen of clubs", 12
queen_of_spades = "Queen of spades", 12
king_of_hearts = "King of hearts", 13
king_of_diamonds = "King of diamonds", 13
king_of_clubs = "King of clubs", 13
king_of_spades = "King of spades", 13


print("Your cards:")
hearts_cube = random.randint(1, 14)
if hearts_cube == 1:
    print("You got Ace of hearts ❤")
elif hearts_cube == 2:
    print("You got One of hearts ❤")
elif hearts_cube == 3:
    print("You got Two of hearts ❤")
elif hearts_cube == 4:
    print("You got Three of hearts ❤")
elif hearts_cube == 5:
    print("You got Four of hearts ❤")
elif hearts_cube == 6:
    print("You got Five of hearts ❤")
elif hearts_cube == 7:
    print("You got Six of hearts ❤")
elif hearts_cube == 8:
    print("You got Seven of hearts ❤")
elif hearts_cube == 9:
    print("You got Eight of hearts ❤")
elif hearts_cube == 10:
    print("You got Nine of hearts ❤")
elif hearts_cube == 11:
    print("You got Ten of hearts ❤")
elif hearts_cube == 11:
    print("You got Jack of hearts ❤")
elif hearts_cube == 12:
    print("You got Queen of hearts ❤")
elif hearts_cube == 13:
    print("You got King of hearts ❤")


diamonds_cube = random.randint(1, 14)
if diamonds_cube == 1:
    print("You got Ace of diamonds ♦")
elif diamonds_cube == 2:
    print("You got One of diamonds ♦")
elif diamonds_cube == 3:
    print("You got Two of diamonds ♦")
elif diamonds_cube == 4:
    print("You got Three of diamonds ♦")
elif diamonds_cube == 5:
    print("You got Four of diamonds ♦")
elif diamonds_cube == 6:
    print("You got Five of diamonds ♦")
elif diamonds_cube == 7:
    print("You got Six of diamonds ♦")
elif diamonds_cube == 8:
    print("You got Seven of diamonds ♦")
elif diamonds_cube == 9:
    print("You got Eight of diamonds ♦")
elif diamonds_cube == 10:
    print("You got Nine of diamonds ♦")
elif diamonds_cube == 11:
    print("You got Ten of diamonds ♦")
elif diamonds_cube == 11:
    print("You got Jack of diamonds ♦")
elif diamonds_cube == 12:
    print("You got Queen of diamonds ♦")
elif diamonds_cube == 13:
    print("You got King of diamonds ♦")


clubs_cube = random.randint(1, 14)
if clubs_cube == 1:
    print("You got Ace of clubs ♣")
elif clubs_cube == 2:
    print("You got One of clubs ♣")
elif clubs_cube == 3:
    print("You got Two of clubs ♣")
elif clubs_cube == 4:
    print("You got Three of clubs ♣")
elif clubs_cube == 5:
    print("You got Four of clubs ♣")
elif clubs_cube == 6:
    print("You got Five of clubs ♣")
elif clubs_cube == 7:
    print("You got Six of clubs ♣")
elif clubs_cube == 8:
    print("You got Seven of clubs ♣")
elif clubs_cube == 9:
    print("You got Eight of clubs ♣")
elif clubs_cube == 10:
    print("You got Nine of clubs ♣")
elif clubs_cube == 11:
    print("You got Ten of clubs ♣")
elif clubs_cube == 11:
    print("You got Jack of clubs ♣")
elif clubs_cube == 12:
    print("You got Queen of clubs ♣")
elif clubs_cube == 13:
    print("You got King of clubs ♣")


spades_cube = random.randint(1, 14)
if spades_cube == 1:
    print("You got Ace of spades ♠")
elif spades_cube == 2:
    print("You got One of spades ♠")
elif spades_cube == 3:
    print("You got Two of spades ♠")
elif spades_cube == 4:
    print("You got Three of spades ♠")
elif spades_cube == 5:
    print("You got Four of spades ♠")
elif spades_cube == 6:
    print("You got Five of spades ♠")
elif spades_cube == 7:
    print("You got Six of spades ♠")
elif spades_cube == 8:
    print("You got Seven of spades ♠")
elif spades_cube == 9:
    print("You got Eight of spades ♠")
elif spades_cube == 10:
    print("You got Nine of spades ♠")
elif spades_cube == 11:
    print("You got Ten of spades ♠")
elif spades_cube == 11:
    print("You got Jack of spades ♠")
elif spades_cube == 12:
    print("You got Queen of spades ♠")
elif spades_cube == 13:
    print("You got King of spades ♠")


print("Now, computer need to get cards...")
time.sleep(10)

first_ch_card = ten_of_hearts
second_ch_card = seven_of_diamonds
third_ch_card = jack_of_clubs
fourth_ch_card = king_of_spades
card_chooseh = input("It's your time to shine! Type a number of your hearts card (e.g. Ace of hearts).\n")
if card_chooseh == ace_of_hearts or one_of_hearts or two_of_hearts or three_of_hearts or four_of_hearts or five_of_hearts or six_of_hearts or seven_of_hearts or eight_of_hearts or nine_of_hearts or ten_of_hearts or jack_of_hearts or queen_of_hearts or king_of_hearts:
    chosen_heart: tuple = ace_of_hearts or one_of_hearts or two_of_hearts or three_of_hearts or four_of_hearts or five_of_hearts or six_of_hearts or seven_of_hearts or eight_of_hearts or nine_of_hearts or ten_of_hearts or jack_of_hearts or queen_of_hearts or king_of_hearts
    if first_ch_card > chosen_heart:
        print("Maybe tomorrow you'll be luckier!")
        time.sleep(3)
        print("What's in the computer's bag of diamonds?")
        time.sleep(2)
        print("Seven!")
    elif first_ch_card < chosen_heart:
        print("It seems the Computer has no response to your move!")
        time.sleep(2)
        print("Let me do it for you...")
    time.sleep(3)
    chosen_diamond: tuple = ace_of_diamonds or one_of_diamonds or two_of_diamonds or three_of_diamonds or four_of_diamonds or five_of_diamonds or six_of_diamonds or seven_of_diamonds or eight_of_diamonds or nine_of_diamonds or ten_of_diamonds or jack_of_diamonds or queen_of_diamonds or king_of_diamonds
    if second_ch_card > chosen_diamond:
        print("Seems like it's Computer's turn now!")
    elif second_ch_card < chosen_diamond:
        print("You're good!")
    time.sleep(3)
    card_choosec = input("I hope you didn't forget that's the game. Type a number of your clubs card.\n")
    if card_choosec == ace_of_clubs or one_of_clubs or two_of_clubs or three_of_clubs or four_of_clubs or five_of_clubs or six_of_clubs or seven_of_clubs or eight_of_clubs or nine_of_clubs or ten_of_clubs or jack_of_clubs or queen_of_clubs or king_of_clubs:
        chosen_club: tuple = ace_of_clubs or one_of_clubs or two_of_clubs or three_of_clubs or four_of_clubs or five_of_clubs or six_of_clubs or seven_of_clubs or eight_of_clubs or nine_of_clubs or ten_of_clubs or jack_of_clubs or queen_of_clubs or king_of_clubs
        time.sleep(1)
        if third_ch_card > chosen_club:
            print("Don't lose your grip!")
        elif chosen_club > third_ch_card:
            print("( •̀ .̫ •́ )✧")
        time.sleep(2)
        print("Alright, let me do it again...")
        time.sleep(3)
        chosen_spades: tuple = ace_of_spades or one_of_spades or two_of_spades or three_of_spades or four_of_spades or five_of_spades or six_of_spades or seven_of_spades or eight_of_spades or nine_of_spades or ten_of_spades or jack_of_spades or queen_of_spades or king_of_spades
        if fourth_ch_card > chosen_spades:
            print("Computer is lucky this time!")
        elif chosen_spades > fourth_ch_card:
            print("I'm sure that you prefer to win!")