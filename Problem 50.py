import time

s = [2, 3, 5]
l = []
k = []

# Project Euler - Problem 50: Consecutive prime sum
# Εύρεση πρώτου αριθμού κάτω από το 1.000.000 που είναι άθροισμα 
# των περισσότερων συνεχόμενων πρώτων.

# Συνάρτηση παραγωγής πρώτων αριθμών έως το n
def isprime (n):
    for i in range(7, n, 2):
        isprime = True
        for k in range(3, int(i**0.5) + 1, 2):
            if i % k == 0:
                isprime = False
                break
        if isprime:
            s.append(i)
    return s

t = time.time()
suma = 0
new_suma = 0
counter = 1
new_counter = 0

# Παραγωγή όλων των πρώτων αριθμών έως το 1.000.000
isprime(1000000)

# Σάρωση κάθε πιθανής αρχικής θέσης i στη λίστα των πρώτων αριθμών
for i in range(0, len(s)):
    suma = s[i]
    counter = 1
    # Πρόσθεση διαδοχικών επόμενων πρώτων
    for r in range(i + 1, len(s)):
        suma = suma + s[r]
        counter = counter + 1
        
        # Αν το άθροισμα είναι και το ίδιο πρώτος αριθμός
        if suma in s:
            # Ενημέρωση μέγιστου πλήθους όρων και αντίστοιχου αθροίσματος
            if new_counter <= counter:
                new_counter = counter
                new_suma = suma
            else:
                new_counter = new_counter
        # Αν το άθροισμα ξεπεράσει το όριο του 1.000.000, διακοπή της εσωτερικής επανάληψης
        elif suma > 1000000:
            break

# Εκτύπωση του μέγιστου πλήθους όρων, του ζητούμενου πρώτου αριθμού και του χρόνου εκτέλεσης
print(new_counter, new_suma)
print(time.time() - t)   
        
          



   
        




