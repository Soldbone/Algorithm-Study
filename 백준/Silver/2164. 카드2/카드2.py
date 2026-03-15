from collections import deque

N = int(input())
deck = deque(range(1, N + 1))

while N > 1:
    deck.popleft()
    deck.append(deck.popleft())
    N -= 1

print(deck[0])