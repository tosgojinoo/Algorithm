def count_bit(n):
    return n % 2 + count_bit(n // 2) if n >= 2 else n

print('1000은 2진수로', bin(1000), '이고, 1의 개수는', count_bit(1000), '개입니다.')
print(bin(1000),count_bit(1000))

def bit_count(n):
    k = 0
    count = 0

    while n >= (1 << k):
        if n & (1 << k) != 0:
            count += 1
        k += 1

    return count

print('1000은 2진수로', bin(1000), '이고, 1의 개수는', bit_count(1000), '개입니다.')