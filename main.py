import random
game = True

# Useful function

def hand_total1(hand,cards1):
  # Running total of hand
  total = 0
  for cards in hand:
    value = cards1[cards]  
    
    total = total + value
  return total
  
print("Welcome to Blackjack!")
  
chips = 2000

while chips > 0:
  print("\nYou have " + str(chips) + " dollars remaining")
  bet = input("\nHow much will you bet? ")
  bet = int(bet)

  # Create a deck of 52 cards
  values = '2','3','4','5','6','7','8','9','10','J','Q','K','A'
  suits = 'Clubs', 'Diamonds', 'Hearts', 'Spades'
  
  cards = {}
  player_hand = []
  dealer_hand = []
  for number in values:
    for suit in suits:
      card = number + ' ' + suit
      if number[0].isdigit():
        cards[card] = int(number[0:2])
      elif number[0].isalpha():
        cards[card] = 10
      if number[0] == "A":
        cards[card] = 11
  cards_list = list(cards)
  
  random.shuffle(cards_list)
  #Start dealing cards
  
  for card in range(2):
    deal = cards_list.pop()
    player_hand.append(deal)
    
  for card in range(2):
    deal = cards_list.pop()
    dealer_hand.append(deal)
    
  hand_total = hand_total1(player_hand, cards)
  dealer_total = hand_total1(dealer_hand, cards)
  
  print("\nHere are your 2 cards", str(player_hand) , "for a total of", int(hand_total))
  
  print("\nOne of the dealer's two cards is", dealer_hand[1])
  
  if hand_total == 21:
    print("\nCongratulations! You have achieved Blackjack!")
    chips = chips + bet
  
  while hand_total < 21 and not(hand_total >21) :
    hit = input("\nHit or stand? ")
    
    if hit == 'hit':
      deal = cards_list.pop()
      player_hand.append(deal)
      hand_total = hand_total1(player_hand, cards)
      print('\nHere is your current hand ' + str(player_hand) + ' for a total of ' + str(hand_total))
   
    if hit == 'stand':
      print("\nThis is your final hand " + str(player_hand))
      print('\nFor a total of ' + str(hand_total))
      break
    
    if hand_total == 21:
      print("\nYou reached 21! You win!")
      chips = chips + bet
      
    if hand_total > 21:
      print("\nYou went over 21. You lose!")
      chips = chips - bet
      break
  
  # 1. Create a hand for the dealer
  # 2. Tell the player one of the dealers cards
  # 3. As long as the dealer's hand is less than or equal to 17, they can hit
  
  
  while dealer_total < 17 and hand_total < 21:
    deal = cards_list.pop()
    dealer_hand.append(deal)
    dealer_total = hand_total1(dealer_hand, cards)
    
  
  if dealer_total >= 17:
    print("\nThis is the dealer's final hand " + str(dealer_hand) + " for a total of " + str(dealer_total))
    
  if dealer_total > 21 and hand_total < 21:
    print("\nThe dealer is busted. You win!")
    chips = chips + bet
    
  if dealer_total == 21:
    print("\nThe dealer reaches 21. You lose!")
    chips = chips - bet
    continue
    
  if dealer_total == hand_total and dealer_hand < 21:
    print("\nIt's a draw. Push!")
    
  if dealer_total < hand_total and hand_total < 21:
    print("\nThe dealer's total is less than yours. You win!")
    chips = chips + bet
    
  if dealer_total > hand_total and dealer_total <= 21:
    print("\nThe dealer's total is more than yours. You lose!")
    chips = chips - bet
    continue