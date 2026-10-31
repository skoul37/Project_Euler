import time

# Project Euler - Problem 62: Cubic permutations
# Εύρεση του μικρότερου κύβου του οποίου ακριβώς 5 αναγραμματισμοί (permutations) 
# των ψηφίων του είναι επίσης κύβοι.

def pandigital (n):
    # Μετατροπή του αριθμού σε λίστα ψηφίων, ταξινόμηση και επανασύνθεση 
    # ώστε να δημιουργηθεί μια κανονική μορφή (signature) για τον αναγραμματισμό
    x = list(str(n))
    x.sort()
    a = ''
    pandigital = a.join(x)
    return pandigital

t = time.time()

# Δημιουργία λίστας με κυβικούς αριθμούς (ξεκινώντας από 4642^3, 
# καθώς οι μικρότεροι δεν έχουν αρκετά ψηφία)
s = [i**3 for i in range(4642, 10000)]

# Σάρωση των κυβικών αριθμών για την εύρεση ισοδύναμων αναγραμματισμών
for n in range(0, len(s)):
    counter = 1
    for r in range(n + 1, len(s)):
        # Έλεγχος αν δύο κύβοι έχουν τα ίδια ακριβώς ψηφία (μετά από ταξινόμηση)
        if pandigital(s[n]) == pandigital(s[r]):
            counter = counter + 1
            # Αν βρεθούν ακριβώς 5 κύβοι με τα ίδια ψηφία
            if counter == 5:
                print(s[n])
                print(time.time() - t)
                exit()

