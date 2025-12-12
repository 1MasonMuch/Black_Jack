import random
import json

# --- Data Loading ---
# Opens the JSON file containing card information
card_file = open("cards.json", encoding="utf8")
# Loads the data (a list of card objects) into the 'data' variable
data = json.load(card_file)
card_file.close() # Good practice to close the file

# --- Helper Functions ---

# Function to safely deal a card from the deck to a hand
def deal_card(target_hand, current_deck):
    """Pops the top card rank from the deck and appends it to the target hand."""
    if current_deck:
        target_hand.append(current_deck.pop(0))

# Function to accurately calculate the score of a hand, including Ace logic
def calculate_score(hand, card_data):
    """Calculates the Blackjack score of a hand, adjusting for Aces (11 or 1)."""
    score = 0
    num_aces = 0
    
    # 1. Calculate the raw score and count Aces
    for rank in hand:
        # Look up the value of that rank in the loaded data
        for card_info in card_data:
            if card_info["rank"] == rank:
                score += card_info["value"]
                if rank == "Ace":
                    num_aces += 1
                break # Stop searching the data once the rank is found

    # 2. Handle Aces (change value from 11 to 1 if score busts)
    while score > 21 and num_aces > 0:
        score -= 10 # Change one Ace from 11 to 1 (11 - 10 = 1)
        num_aces -= 1

    return score

# --- Main Game Function ---

def blackjack():
    # --- Initialization ---
    player = []
    dealer = []
    
    # Initialize scores to 0 (Scores are integers, not lists)
    player_score = 0
    dealer_score = 0
    
    # --- Deck Creation and Shuffle ---
    deck = []
    # Build the deck of card ranks from the loaded data
    for card in data:
        # Assuming 'data' contains 52 individual card objects
        deck.append(card["rank"])

    random.shuffle(deck)

    # --- Initial Deal ---
    deal_card(player, deck)
    deal_card(player, deck)
    deal_card(dealer, deck)
    deal_card(dealer, deck)

    print(f"\nYour starting hand: {player}")
    print(f"Dealer shows: {dealer[0]}") # Only show the first dealer card

    # Calculate initial scores
    player_score = calculate_score(player, data)
    dealer_score = calculate_score(dealer, data)
    
    # --- Player's Turn ---

    # Loop continues as long as the player hasn't busted
    while player_score <= 21:
        
        if player_score == 21 and len(player)