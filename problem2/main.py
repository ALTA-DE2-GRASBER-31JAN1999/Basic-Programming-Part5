def pow(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / pow(x, -n)
    elif n % 2 == 0:
        half_power = pow(x, n // 2)
        return half_power * half_power
    else:
        half_power = pow(x, (n - 1) // 2)
        return x * half_power * half_power

if __name__ == '__main__':
    print(pow(2, 3)) # 8
    print(pow(7, 2)) # 49
    print(pow(10, 5)) # 100000
    print(pow(17, 6)) # 24137569
    print(pow(5, 3)) # 125
