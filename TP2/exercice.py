def contient_doublons(t):
    return len(t) != len(set(t))

def est_anagramme(s, t):
    return sorted(s) == sorted(t)

print(contient_doublons([1, 2, 3, 1]))
print(contient_doublons([1, 2, 3, 4]))

print(est_anagramme("python", "onhtyp"))
print(est_anagramme("tp", "tps"))
