# Project Euler - Problem 17: Number letter counts
# Αν γραφτούν ολογράφως οι αριθμοί από το 1 έως το 1000 στα αγγλικά, πόσα γράμματα συνολικά χρησιμοποιούνται;

def diairesi(n):
    e = n // 100
    d = (n - e * 100) // 10
    m = (n - e * 100 - d * 10)
    s.append(e)
    s.append(d)
    s.append(m)
    return s

lex1 = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}
lex2 = {10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8}
lex3 = {0: 0, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}
lex4 = {100: 7, 1000: 8}

suma = 0

for i in range(1, 1000):
    if len(str(i)) == 3:
        s = []
        suma = suma + 10
        diairesi(i)
        suma = suma + lex1[s[0]]
        if s[1] == 1:
            suma = suma + lex2[int(str(s[1]) + str(s[2]))]
        else:
            suma = suma + lex3[int(str(s[1]) + str(0))] + lex1[s[2]]
    elif len(str(i)) == 2:
        s = []
        diairesi(i)
        if s[1] == 1:
            suma = suma + lex2[int(str(s[1]) + str(s[2]))]
        else:
            suma = suma + lex3[int(str(s[1]) + str(0))] + lex1[s[2]]
    else:
        suma = suma + lex1[i]

print(suma - 27 + 11)
    
    

    
