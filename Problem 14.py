# Project Euler - Problem 14: Longest Collatz sequence
# Βρες ποιος αρχικός αριθμός κάτω από το 1.000.000 παράγει τη μεγαλύτερη ακολουθία Collatz.

s = []

# Συνάρτηση που υπολογίζει το μήκος της ακολουθίας Collatz για έναν αριθμό x
def Collatz (x):
    counter = 1
    y = x
    while x != 1:
        if x % 2 == 0:
            x = x / 2
            counter = counter + 1
        else:
            x = 3 * x + 1
            counter = counter + 1
    else:
        return counter, y

# Υπολογισμός της ακολουθίας για όλους τους αριθμούς από το 2 έως το 1.000.000
for i in range(2, 1000001):
    Collatz(i)
    s.append(Collatz(i))

# Ταξινόμηση της λίστας βάσει του πλήθους των βημάτων
s.sort()

# Εκτύπωση του ζευγαριού (βήματα, αρχικός αριθμός) με τη μεγαλύτερη ακολουθία
print(s[-1])
    
    
        
    



