def produit_des_autres(tab):
    n = len(tab)
    resultat = []

    for i in range(n):
        produit = 1
        for j in range(n):
            if i != j:
                produit *= tab[j]
        resultat.append(produit)

    return resultat


if __name__ == "__main__":
    print(produit_des_autres([1,2,3,4,5]))
    print(produit_des_autres([3,2,1]))
