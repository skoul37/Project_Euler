# Project Euler - Problem 53: Combinatoric selections
# Υπολογισμός του πλήθους των συνδυασμών \binom{n}{r} για 1 <= n <= 100 
# που ξεπερνούν το 1.000.000.

# Αναδρομική συνάρτηση υπολογισμού του παραγοντικού ενός αριθμού (n!)
def paragontiko(n):
    if n == 0:
        return 1
    else:
        return n * paragontiko(n - 1)

# Συνάρτηση υπολογισμού των συνδυασμών (Combinatoric / Διωνυμικός συντελεστής)
def Combinatoric (n, r):
    c = paragontiko(n) / (paragontiko(r) * paragontiko(n - r))
    return c

counter = 0

# Σάρωση των τιμών του n από 23 έως 100 (καθώς για n < 23 δεν υπάρχουν τιμές > 1.000.000)
for n in range(23, 101):
    # Σάρωση των τιμών του r από 1 έως n
    for r in range(1, n + 1):
        # Έλεγχος αν ο συνδυασμός ξεπερνά το 1.000.000
        if Combinatoric(n, r) > 1000000:
            counter = counter + 1

# Εκτύπωση του συνολικού πλήθους των περιπτώσεων
print(counter)