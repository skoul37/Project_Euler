# Project Euler - Problem 27: Quadratic primes
# Βρες το γινόμενο των συντελεστών a και b (όπου |a| < 1000 και |b| <= 1000) 
# για το τετραγωνικό πολυώνυμο n^2 + an + b που παράγει τους περισσότερους 
# διαδοχικούς πρώτους αριθμούς ξεκινώντας από το n = 0.

# Συνάρτηση που ελέγχει αν ένας αριθμός είναι πρώτος (επιστρέφει 1 αν είναι πρώτος, 0 αλλιώς)
def protos(n):
    isprime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            isprime = False
            return 0
            break
    if isprime:
        return 1

new_counter = 0
new_product = 0

# Έλεγχος για όλες τις πιθανές τιμές των a και b εντός των ορίων
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        counter = 0
        product = a * b
        # Υπολογισμός διαδοχικών πρώτων για n = 0, 1, 2, ...
        while protos(abs(n**2 + a * n + b)) == 1:
            counter = counter + 1
            n = n + 1
            # Αν βρούμε μεγαλύτερη ακολουθία πρώτων, αποθηκεύουμε το μέγιστο πλήθος και το γινόμενο a*b
            if new_counter <= counter:
                new_counter = counter
                new_product = product

# Εκτύπωση του γινομένου των συντελεστών a και b που δίνουν το μέγιστο αποτέλεσμα
print(new_product)
            
        
