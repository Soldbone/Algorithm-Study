# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164
"""
1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.
규칙성을 찾아보려고 했으나 잘 모르겠다. 연속된 수라는 특성과 대칭적인 형태 때문에 뭔가 수학적인 규칙이 있을 것 같다.

1234    top: 1 bottom: 4
342     top: 3 bottom: 2
24      top: 2 bottom: 4
4       top: 4 bottom: 4

123456  top: 1 bottom: 6
34562   top: 3 bottom: 2
5624    top: 5 bottom: 4
246     top: 2 bottom: 6
64      top: 6 bottom: 4
4       top: 4 bottom: 4

1 11 111 1111 11111 111111
111 1111 11111 111111 11
11111 111111 11 1111
11 1111 111111
111111 1111
1111

123456789
34567892
5678924
789246
92468
4682
826
62
2
"""

from collections import deque

N = int(input())
cards = [i for i in range(1, N + 1)]
deck = deque(cards)

while len(deck) > 1:
    deck.popleft()
    deck.append(deck.popleft())

print(deck[0])
