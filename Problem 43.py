# Project Euler - Problem 43: Sub-string divisibility
# Εύρεση του αθροίσματος όλων των 0-9 πανψηφιακών αριθμών των οποίων οι διαδοχικές 
# 3ψήφιες υποομάδες διαιρούνται αντίστοιχα με τους πρώτους αριθμούς από το 2 έως το 17.

# Συνάρτηση που επιστρέφει τα πρώτα 2 ψηφία ενός αριθμού (χρησιμοποιείται για την επέκταση προς τα αριστερά)
def sub_string (n):
    return str(n)[0:2]

# Συνάρτηση ελέγχου πανψηφιακότητας (0 έως 9)
def pandigital (n):
    x = list(str(n))
    x.sort()
    a = '0123456789'
    b = ''
    pandigital = b.join(x)
    # Αν ο αριθμός περιέχει ακριβώς τα ψηφία 0-9, επιστρέφει τον αριθμό, αλλιώς 0
    if pandigital == a:
        return n
    else:
        return 0

s = []
k = []
suma = 0

# Βήμα 1: Εύρεση όλων των 3ψήφιων αριθμών που διαιρούνται με το 17 (τελευταία υποομάδα)
for i in range(100, 1000):
    if i % 17 == 0:
        s.append(i)

# Βήμα 2: Αναδρομική επέκταση προς τα αριστερά ελέγχοντας τη διαιρετότητα με το 13
for a in s[:]:
    for b in range(0, 10):
        if int(str(b) + sub_string(a)) % 13 == 0:
            k.append(str(b) + str(a))

# Βήμα 3: Επέκταση ελέγχοντας τη διαιρετότητα με το 11
s = []
for a in k[:]:
    for b in range(0, 10):
        if int(str(b) + sub_string(a)) % 11 == 0:
            s.append(str(b) + str(a))

# Βήμα 4: Επέκταση ελέγχοντας τη διαιρετότητα με το 7
k = []
for a in s[:]:
    for b in range(0, 10):
        if int(str(b) + sub_string(a)) % 7 == 0:
            k.append(str(b) + str(a))

# Βήμα 5: Επέκταση ελέγχοντας τη διαιρετότητα με το 5
s = []
for a in k[:]:
    for b in range(0, 10):
        if int(str(b) + sub_string(a)) % 5 == 0:
            s.append(str(b) + str(a))

# Βήμα 6: Επέκταση ελέγχοντας τη διαιρετότητα με το 3
k = []
for a in s[:]:
    for b in range(0, 10):
        if int(str(b) + sub_string(a)) % 3 == 0:
            k.append(str(b) + str(a))

# Βήμα 7: Επέκταση ελέγχοντας τη διαιρετότητα με το 2
s = []
for a in k[:]:
    for b in range(0, 10):
        if int(str(b) + sub_string(a)) % 2 == 0:
            s.append(str(b) + str(a))

# Βήμα 8: Προσθήκη του τελευταίου (πρώτου) ψηφίου (από 1 έως 9, χωρίς προπορευόμενο μηδενικό)
k = []
for a in s:
    for b in range(1, 10):
        k.append(str(b) + str(a))

# Βήμα 9: Έλεγχος ποιοι από τους τελικούς αριθμούς είναι πραγματικά πανψηφιακοί (0-9)
s = []
for n in k[:]:
    s.append(pandigital(int(n)))

# Υπολογισμός συνολικού αθροίσματος των εγκύρων πανψηφιακών αριθμών
for i in s:
    suma = suma + int(i)

# Εκτύπωση του τελικού αποτελέσματος
print(suma)


