def blackjack_hand_total(cards: list[int]) -> int:
    
    somma = 0

    # Sum all cards
    for i in range(len(cards)):
        somma += cards[i]

        # Check if the card is an Ace
        if cards[i] == 11:

            # If the sum is greater than 21, count Ace as 1
            if somma > 21:
                somma -= 10

    return somma

# Test cases
print(blackjack_hand_total([2, 3, 4]))  # 9
print(blackjack_hand_total([10, 11, 1]))  # 21
print(blackjack_hand_total([11, 11, 1]))  # 13