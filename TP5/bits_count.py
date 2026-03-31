def count_bits(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

n = int(input("Entrez un entier : "))
print("Nombre de bits à 1 :", count_bits(n))