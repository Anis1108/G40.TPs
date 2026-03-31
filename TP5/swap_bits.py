def swap_bits(n: int, i: int, j: int) -> int:
    bit_i = (n >> i) & 1
    bit_j = (n >> j) & 1

    if bit_i != bit_j:
        mask = (1 << i) | (1 << j)
        n ^= mask

    return n

n = int(input("n = "))
i = int(input("i = "))
j = int(input("j = "))

print("Résultat après swap :", swap_bits(n, i, j))