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
        
        if player_score == 21 and len(player) == 2:
            # Player has a Blackjack (21 on first two cards)
            print("🤩 Blackjack! Player wins immediately (unless dealer also has Blackjack).")
            # Break the player's turn loop
            break
        
        # Check if player needs another card
        if player_score > 21:
            print(f"Your final hand: {player} (Score: {player_score})")
            print("BUST! You went over 21.")
            break
            
        # Get player decision
        choice = input("Type 'h' to **H**it, or 's' to **S**tand: ").lower()
        
        if choice == 'h':
            deal_card(player, deck)
            player_score = calculate_score(player, data)
            print(f"Your hand: {player}")
            print(f"Your current score: {player_score}")
        elif choice == 's':
            print("You stand.")
            break
        else:
            print("Invalid choice, please type 'h' or 's'.")
            
        # Re-check score after hitting
        if player_score > 21:
            print(f"Your final hand: {player} (Score: {player_score})")
            print("BUST! You went over 21.")
            
    # If the player has busted, the game ends here for the player.
    if player_score > 21:
        print("\nDealer wins (Player Busted).")
        return # End the game

    # --- Dealer's Turn (Only if Player hasn't busted) ---

    print(f"\n--- Dealer's Turn ---")
    print(f"Dealer's full hand: {dealer} (Score: {dealer_score})")

    # Dealer hits until score is 17 or higher
    while dealer_score < 17:
        print("Dealer hits (score < 17)...")
        deal_card(dealer, deck)
        dealer_score = calculate_score(dealer, data)
        print(f"Dealer's hand: {dealer}")
        print(f"Dealer's current score: {dealer_score}")
    
    if dealer_score > 21:
        print("Dealer BUSTS! You win!")
        return # End the game
    
    print("Dealer stands (score >= 17).")

    

    print("\n--- Final Results ---")
    print(f"Your final score: {player_score}")
    print(f"Dealer's final score: {dealer_score}")

    if player_score > dealer_score:
        print("🎉 You Win!")
    elif player_score < dealer_score:
        print("Dealer Wins!")
    else:
        print("Push (It's a Tie)!")

# --- Game Start ---
if __name__ == "__main__":
    
    while True:
        blackjack()
        
        # Ask to play again
        play_again = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
        if play_again != 'y':
            break

    print("Thanks for playing!")