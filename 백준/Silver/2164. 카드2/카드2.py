from collections import deque

N = int(input())
cards = [i for i in range(1, N + 1)]
deck = deque(cards)

while N > 1:
    deck.popleft()
    deck.append(deck.popleft())
    N -= 1

print(deck[0])