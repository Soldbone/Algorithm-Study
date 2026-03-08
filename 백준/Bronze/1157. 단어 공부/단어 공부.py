"""
ChatGPT의 도움을 받아 개선한 버전
"""
word = input().upper()

counts_for_alpha = [0] * 26

for char in word:
    counts_for_alpha[ord(char) - ord("A")] += 1

max_count = max(counts_for_alpha)

if counts_for_alpha.count(max_count) == 1:
    print(chr(counts_for_alpha.index(max_count) + ord("A")))
else:
    print("?")