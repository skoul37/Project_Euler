# Project Euler - Problem 23: Non-abundant sums
# Βρες το άθροισματος όλων των θετικών ακεραίων που δεν μπορούν να γραφτούν 
# ως άθροισμα δύο (abundant) αριθμών.

# Συνάρτηση που ελέγχει αν ένας αριθμός είναι άφθονος (το άθροισμα των διαιρετών του είναι μεγαλύτερο από τον ίδιο)
def abundant (n):
    suma = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            suma = suma + i
    if suma > n:
        l.append(n)

l = []
total = 0
s = [i for i in range(1, 28124)]

# Εύρεση όλων των αφθόνων αριθμών μέχρι το 28123
for i in s:
    abundant(i)

# Αφαίρεση από τη λίστα s των αριθμών που μπορούν να γραφτούν ως άθροισμα δύο αφθόνων αριθμών
for i in range(0, len(l)):
    for n in range(i, len(l)):
        if l[i] + l[n] >= 28124:
            break
        elif l[i] + l[n] in s:
            s.remove(l[i] + l[n])

# Υπολογισμός του αθροίσματος των εναπομειάντων αριθμών
for a in s:
    total = total + a

# Εκτύπωση του τελικού αποτελέσματος
print(total)

                   
