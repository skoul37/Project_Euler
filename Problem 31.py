# Project Euler - Problem 31: Coin sums
# Βρες πόσοι διαφορετικοί τρόποι υπάρχουν για να σχηματιστεί το ποσό των £2 (200p) 
# χρησιμοποιώντας συνδυασμούς κερμάτων (£1, 50p, 20p, 10p, 5p, 2p, 1p).

# Αρχικοποίηση του μετρητή συνδυασμών (ξεκινάει από 1 για την περίπτωση 
# όπου χρησιμοποιείται αποκλειστικά και μόνο ένα κέρμα των 200p / £2)
counter = 1

# Εξωτερικός βρόχος για τα κέρματα των £1 (100p) [0, 100, 200]
for a in range(0, 201, 100):
    if a == 200:
        counter = counter + 1
        
    # Βρόχος για τα κέρματα των 50p [0, 50, 100, 150, 200]
    for b in range(0, 201, 50):
        # Αν το τρέχον άθροισμα ισκριμένα κάνει ακριβώς 200p, αυξάνουμε τον μετρητή και σταματάμε (break)
        if a + b == 200 and b != 0:
            counter = counter + 1
            break
        # Βελτιστοποίηση: αν ξεπεράσουμε τα 200p, διακόπτουμε τον εσωτερικό βρόχο
        elif a + b > 200:
            break
            
        # Βρόχος για τα κέρματα των 20p [0, 20, 40, ...]
        for c in range(0, 201, 20):
            if a + b + c == 200 and c != 0:
                counter = counter + 1
                break
            elif a + b + c > 200:
                break
                
            # Βρόχος για τα κέρματα των 10p [0, 10, 20, ...]
            for d in range(0, 201, 10):
                if a + b + c + d == 200 and d != 0:
                    counter = counter + 1
                    break
                elif a + b + c + d > 200:
                    break
                    
                # Βρόχος για τα κέρματα των 5p [0, 5, 10, ...]
                for e in range(0, 201, 5):
                    if a + b + c + d + e == 200 and e != 0:
                        counter = counter + 1
                        break
                    elif a + b + c + d + e > 200:
                        break
                        
                    # Βρόχος για τα κέρματα των 2p [0, 2, 4, ...]
                    for f in range(0, 201, 2):
                        if a + b + c + d + e + f == 200 and f != 0:
                            counter = counter + 1
                            break
                        elif a + b + c + d + e + f > 200:    
                            break
                            
                        # Εσωτερικός βρόχος για τα κέρματα των 1p (1 πέννας) [0, 1, 2, ...]
                        for g in range(0, 201, 1):
                            if a + b + c + d + e + f + g == 200 and g != 0:
                                counter = counter + 1
                                break
                            elif a + b + c + d + e + f + g > 200:
                                break

# Εκτύπωση των τελικών τιμών των μεταβλητών και του συνολικού πλήθους των τρόπων (counter)
print(a, b, c, d, e, f, g, counter)
                

            
                
      
      
            
        
