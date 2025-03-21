m, n = map(int, input().split())

def prime_numbers(n):
    arr = [i for i in range(n+1)]
    arr[1] = 0
    end = int(n**(1/2))
    for i in range(2, end+1):
        if arr[i] != 0:
            for j in range(i*i, n+1, i):
                arr[j] = 0
            
    return [i for i in arr[m:] if arr[i]]

print(*prime_numbers(n), sep='\n')