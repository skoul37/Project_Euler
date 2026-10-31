from itertools import product, permutations

# Project Euler - Problem 61: Cyclical figurate numbers

# Αρχικοποίηση λιστών για τους πολυγωνικούς αριθμούς (P3 έως P8)
P3, P4, P5, P6, P7, P8 = [], [], [], [], [], []
l3, l4, l5, l6, l7, l8 = [], [], [], [], [], []

# Παραγωγή πολυγωνικών αριθμών για n από 1 έως 199 και φιλτράρισμα των 4-ψήφιων
for n in range(1, 200):
    p3 = n * (n + 1) / 2
    p4 = n**2
    p5 = n * (3 * n - 1) / 2
    p6 = n * (2 * n - 1)
    p7 = n * (5 * n - 3) / 2
    p8 = n * (3 * n - 2)
    
    if len(str(int(p3))) == 4:
        P3.append(int(p3))
    if len(str(int(p4))) == 4:
        P4.append(int(p4))
    if len(str(int(p5))) == 4:
        P5.append(int(p5))
    if len(str(int(p6))) == 4:
        P6.append(int(p6))
    if len(str(int(p7))) == 4:
        P7.append(int(p7))
    if len(str(int(p8))) == 4:
        P8.append(int(p8))

A = (P3, P4, P5, P6, P7, P8)
s = []

# Παραγωγή όλων των πιθανών διατάξεων (permutations) των κατηγοριών πολυγωνικών αριθμών
x = list(permutations(A))
for i in range(0, len(x)):
    k = list(x[i])
    s = s + k

# Σάρωση των συνδυασμών ανά 6 λίστες (μια για κάθε πολυγωνικό τύπο)
for i in range(0, len(s), 6):
    for a in s[i]:
        for b in s[i+1]:
            # Έλεγχος αν τα 2 τελευταία ψηφία του a ταιριάζουν με τα 2 πρώτα του b
            if str(a)[2:4] == str(b)[0:2]:
                for c in s[i+2]:
                    if str(b)[2:4] == str(c)[0:2]:
                        for d in s[i+3]:
                            if str(c)[2:4] == str(d)[0:2]:
                                for e in s[i+4]:
                                    if str(d)[2:4] == str(e)[0:2]:
                                        for f in s[i+5]:
                                            if str(e)[2:4] == str(f)[0:2]:
                                                # Έλεγχος κλεισίματος κύκλου (τα 2 τελευταία του f με τα 2 πρώτα του a)
                                                if str(f)[2:4] == str(a)[0:2]:
                                                    print(a, b, c, d, e, f)
                                                    print(a + b + c + d + e + f)
                                                    exit()
                            
    

    
               

                                        
                                    
           

