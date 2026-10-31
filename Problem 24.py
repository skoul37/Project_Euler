# Project Euler - Problem 24: Lexicographic permutations
# Βρες τη 1.000.000στή λεξικογραφική μεταθέση (permutation) των ψηφίων 0, 1, 2, 3, 4, 5, 6, 7, 8 και 9.

from itertools import permutations

s = []

# Δημιουργία όλων των δυνατών μεταθέσεων των 10 ψηφίων
for i in permutations('0123456789', 10):
    s.append(''.join(i))

# Λεξικογραφική ταξινόμηση όλων των μεταθέσεων
s.sort()

# Εκτύπωση του 1.000.000στού στοιχείου (δείκτης 999.999 επειδή η μέτρηση στη Python ξεκινά από το 0)
print(s[999999])
    




    
   
       
    

        
        
        

    
