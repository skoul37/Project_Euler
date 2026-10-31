# Project Euler - Problem 29: Distinct powers
# Βρες πόσοι ξεχωριστοί (distinct) όροι παράγονται από τη συνάρτηση a^b 
# για 2 <= a <= 100 και 2 <= b <= 100.

x = []

# Δημιουργία όλων των δυνατών συνδυασμών a^b για a και b από 2 έως 100
for a in range(2, 101):
    for b in range(2, 101):
        x.append(a**b)

# Ταξινόμηση της λίστας
x.sort()
c = x[0]

# Αφαίρεση των διπλότυπων τιμών συγκρίνοντας διαδοχικά στοιχεία
for i in x[1:len(x)]:
    c = c + i
    if c == 2 * i:
        x.remove(i)
        c = i
    else:
        c = i

# Εκτύπωση του πλήθους των μοναδικών όρων
print(len(x))
    
     
    
    
               
    
    
    
        
