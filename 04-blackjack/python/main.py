""" 
[Start Date: 2025|03|12] [Total Time (hr): 04 Hours 50 Minutes] [Finish Date: 2025|03|13]
[Author: FirstOfLast]
"""
import random

def player(deck_of_cards, index):

    hand = []

    card, index = drawCard(deck_of_cards, index)
    hand.append(card)

    card, index = drawCard(deck_of_cards, index)
    hand.append(card)

    adjustForAce(hand)
    print(f"\nYour hand: {hand} (Total: {sum(hand)})")

    choice = input("Do you want to Hit or Stand?: ")

    while choice.lower() not in ["hit","stand"] :
        choice = input("Enter a valid choice of Hit or Stand: ")

    while choice.lower() == "hit" and sum(hand) <= 21:
        card, index = drawCard(deck_of_cards, index)
        hand.append(card)
        
        adjustForAce(hand)
        print(f"Your hand: {hand} (Total: {sum(hand)})")

        if sum(hand) <= 21:
            choice = input("Enter a valid choice of Hit or Stand: ")

            while choice.lower() not in ["hit","stand"] :
                choice = input("Enter a valid choice of Hit or Stand: ")
        
    if sum(hand) <= 21:
        return (sum(hand), index)
    else:
        return ("Bust", index)

def dealer(deck_of_cards, index):

    hand = []

    card, index = drawCard(deck_of_cards, index)
    hand.append(card)

    card, index = drawCard(deck_of_cards, index)
    hand.append(card)

    adjustForAce(hand)
    print(f"\nDealers hand: {hand} (Total: {sum(hand)})")

    while sum(hand) <= 17:
        card, index = drawCard(deck_of_cards, index)
        hand.append(card)
        adjustForAce(hand)
        print(f"Dealers hand: {hand} (Total: {sum(hand)})")
        
    if sum(hand) <= 21:
        return (sum(hand), index)
    else:
        return ("Bust", index)

def drawCard(deck_of_cards, index):
    return deck_of_cards[index], index + 1

def adjustForAce(hand):
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1

def main():

    print("Welcome to Blackjack! \nThe goal is to get as close to 21 as possible without going over.")

    ch = "yes"
    while ch.lower() == "yes":
        index = 0
        playerHandValue = 0
        dealerHandValue = 0

        # Jack, Queen, King = 10 and Ace = 11 which can also become 1 if required. Multipled by 4, Hearts, Diamonds, Clubs & Spades
        deck_of_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 
        random.shuffle(deck_of_cards)

        playerHandValue, index = player(deck_of_cards, index)

        dealerHandValue, index = dealer(deck_of_cards, index)

        if playerHandValue == "Bust" or dealerHandValue == "Bust":
            if playerHandValue == "Bust":
                print("\nPlayer hand is a bust. Dealer wins!")
            else:
                print("\nDealer hand is a bust. Player wins!")
            
        else:
            if playerHandValue > dealerHandValue:
                print("\nYou win!!!")
            elif playerHandValue < dealerHandValue:
                print("\nDealer wins!!!")
            else:
                print("\nDraw")
    
        ch = input("\nWould you like to play another game of blackjack? (Yes/No): ")

        while ch.lower() not in ["yes", "no"]:
            ch = input("Invalid! Please answer with Yes or No: ")

main()