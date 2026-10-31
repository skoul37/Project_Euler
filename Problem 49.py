from itertools import permutations

# Project Euler - Problem 49: Prime permutations
# Εύρεση 4-ψήφιων πρώτων αριθμών που αποτελούν αριθμητική πρόοδο με βήμα 3330 
# και ταυτόχρονα είναι αναδιατάξεις (permutations) των ίδιων ψηφίων.

# Συνάρτηση ελέγχου πρώτου αριθμού και αποθήκευσης στη λίστα s
def protos(n):
    isprime = True
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            isprime = False
            break
    if isprime:
        s.append(n)

# Συνάρτηση που παράγει όλες τις πιθανές μεταθέσεις (permutations) των ψηφίων ενός αριθμού
def permut(n):
    for m in permutations(str(n), 4):
        l.append(''.join(m))

l = []
s = []

# Παραγωγή όλων των περιττών 4-ψήφιων πρώτων αριθμών
for i in range(1001, 10000, 2):
    protos(i)

counter = 0

# Σάρωση των πρώτων αριθμών για την εύρεση τριάδας με βήμα 3330 (π.χ. p, p+3330, p+6660)
for i in range(0, len(s)):
     if s[i] + 3330 in s and s[i] + 2 * 3330 in s:
         permut(s[i])  # Παραγωγή των μεταθέσεων ψηφίων του πρώτου αριθμού
         
         # Έλεγχος αν οι άλλοι δύο αριθμοί της ακολουθίας προέρχονται από τα ίδια ψηφία
         if str(s[i] + 3330) in l and str(s[i] + 2 * 3330) in l:
             print(s[i], s[i] + 3330, s[i] + 2 * 3330, str(s[i]) + str(s[i] + 3330) + str(s[i] + 2 * 3330))  
             counter = counter + 1
             
             # Τερματισμός μετά την εύρεση της δεύτερης (ζητούμενης) ακολουθίας, 
             # καθώς η πρώτη είναι η γνωστή (1487, 4817, 8147)
             if counter == 2:
                 exit()
         else:
             l = []  # Καθαρισμός λίστας μεταθέσεων αν δεν ταιριάζουν
