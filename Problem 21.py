# Project Euler - Problem 21: Amicable numbers
# Βρες το άθροισμα όλων των φιλικών (amicable) αριθμών κάτω από το 10000.

# Συνάρτηση που ελέγχει αν ένας αριθμός είναι πρώτος και τον αφαιρεί από τη λίστα s
def isprime(x):
    isprime = True
    for y in range(2, int(x**0.5) + 1):
        if x % y == 0:
            isprime = False
            break
    if isprime:
        s.remove(x)

# Συνάρτηση που βρίσκει αν ο αριθμός x έχει φιλικό αριθμό y (άθροισμα γνήσιων διαιρετών)
def amicable(x):
    sumax = 0
    sumay = 0
    # Υπολογισμός αθροίσματος διαιρετών του x
    for i in range(1, int(x / 2) + 1):
        if x % i == 0:
            sumax = sumax + i
            y = sumax
    # Υπολογισμός αθροίσματος διαιρετών του y
    for r in range(1, int(y / 2) + 1):
        if y % r == 0:
            sumay = sumay + r
    # Αν ισχύει η ιδιότητα των φιλικών αριθμών, τους προσθέτουμε στη λίστα l και αφαιρούμε τον x
    if sumay == x and x != y:
        l.append(x + y)
        s.remove(x)

l = []
s = [i for i in range(4, 10000)]

# Αφαίρεση των πρώτων αριθμών από τη λίστα (καθώς δεν μπορούν να έχουν φιλικούς αριθμούς)
for x in s:
    isprime(x)

# Έλεγχος για φιλικούς αριθμούς στους εναπομείναντες αριθμούς
for x in s:
    amicable(x)

l.sort()

# Εκτύπωση του τελικού αθροίσματος (διαιρούμενο δια 2 επειδή τα ζευγάρια μετρούνται διπλά) και της λίστας
print(sum(int(i) / 2 for i in l))
print(l)




    


        
        

        
        
    

    
