from fractions import Fraction

# Project Euler - Problem 57: Square root convergents
# Υπολογισμός των συνεχών κλασμάτων για το sqrt(2) έως το n = 1000 
# και μέτρηση πόσες φορές ο αριθμητής έχει περισσότερα ψηφία από τον παρονομαστή.

def frac (n):
    counter = 1
    x = Fraction(1, 2)
    if n == 1:
        return 1 + Fraction(1, 2)
    else:
        # Υπολογισμός του συνεχούς κλάσματος επαναληπτικά
        while counter < n:
            x = Fraction(1, 2 + x)
            counter = counter + 1
    return 1 + x

s = []
metritis = 0

# Υπολογισμός για τα πρώτα 1000 κλάσματα
for n in range(1, 1001):
    s.append(frac(n))
    print(len(s))  # Εμφάνιση προόδου

# Έλεγχος πλήθους ψηφίων αριθμητή και παρονομαστή για κάθε κλάσμα
for i in s:
    if len(str(i.numerator)) > len(str(i.denominator)):
        metritis = metritis + 1

print(metritis)

""" 
Ο αλγόριθμος χρειάζεται βελτιστοποίηση (περίπου 5 λεπτά εκτέλεσης)
"""

