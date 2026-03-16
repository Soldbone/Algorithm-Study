a, b, c = map(int, input().split())


def pow_modulo(num, n):
    if n == 1:
        return num % c

    half_exp = pow_modulo(num, n // 2)
    if n % 2 == 0:
        return (half_exp * half_exp) % c
    else:
        return (num * half_exp * half_exp) % c


print(pow_modulo(a, b))