# 여행 가자
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

parent = [ i for i in range(N+1) ]
rank = [ 0 for _ in range(N+1) ]

def union(a: int, b: int) -> None:
    '''
    a와 b를 합친다.
    int, int -> void
    '''
    a = find(a)
    b = find(b)
    if a == b:
        return
    
    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[b] = a
        rank[a] += 1

def find(a: int) -> int:
    '''
    a의 부모를 찾는다.
    int -> int
    '''
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

for i in range(1, N+1):
    input_line = list(map(int, input().split()))
    for j in range(i, N):
        if input_line[j] == 1:
            union(i, j+1) # parent[j+1] = i

target_path = list(map(int, input().split()))
for i in range(M-1):
    if find(target_path[i]) != find(target_path[i+1]):
        print("NO")
        break
else:
    print("YES")
