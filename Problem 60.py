# Project Euler - Problem 60: Prime pair sets

# Συνάρτηση ελέγχου και αποθήκευσης πρώτων αριθμών στη λίστα s
def protos (n):
    isprime = True
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            isprime = False
            break
    if isprime:
        s.append(n)

# Συνάρτηση ελέγχου αν ένας αριθμός είναι πρώτος (προσοχή: επιστρέφει 0 αν ΕΙΝΑΙ πρώτος, 
# διαφορετικά δεν επιστρέφει τίποτα / None)
def protos2 (m):
    isprime = True
    for k in range(3, int(m**0.5) + 1, 2):
        if m % k == 0:
            isprime = False
            break
    if isprime:
        return 0

s = [3, 5, 7]
l = []

# Παραγωγή αρχικών πρώτων αριθμών έως το 10.000
for n in range(11, 10000, 2):
    protos(n)

# Έλεγχος με εμφωλευμένους βρόχους (nested loops) για την εύρεση 5 πρώτων (s[a], s[b], s[c], s[d], s[e]) 
# που ικανοποιούν τη συνθήκη ζευγαρώματος concatenation
for a in range(0, len(s)):
     for b in range(a + 1, len(s)):
         # Έλεγχος αν ο συνδυασμός των δύο πρώτων δίνει πρώτους αριθμούς και προς τις δύο κατευθύνσεις
         if protos2(int(str(s[a]) + str(s[b]))) == 0 and protos2(int(str(s[b]) + str(s[a]))) == 0:
             for c in range(b + 1, len(s)):
                 if protos2(int(str(s[a]) + str(s[c]))) == 0 and protos2(int(str(s[c]) + str(s[a]))) == 0 and protos2(int(str(s[b]) + str(s[c]))) == 0 and protos2(int(str(s[c]) + str(s[b]))) == 0:
                      for d in range(c + 1, len(s)):
                          if protos2(int(str(s[a]) + str(s[d]))) == 0 and protos2(int(str(s[d]) + str(s[a]))) == 0 and protos2(int(str(s[b]) + str(s[d]))) == 0 and protos2(int(str(s[d]) + str(s[b]))) == 0 and protos2(int(str(s[c]) + str(s[d]))) == 0 and protos2(int(str(s[d]) + str(s[c]))) == 0:
                              for e in range(d + 1, len(s)):
                                  if protos2(int(str(s[a]) + str(s[e]))) == 0 and protos2(int(str(s[e]) + str(s[a]))) == 0 and protos2(int(str(s[b]) + str(s[e]))) == 0 and protos2(int(str(s[e]) + str(s[b]))) == 0 and protos2(int(str(s[c]) + str(s[e]))) == 0 and protos2(int(str(s[e]) + str(s[c]))) == 0 and protos2(int(str(s[d]) + str(s[e]))) == 0 and protos2(int(str(s[e]) + str(s[d]))) == 0:
                                        # Εκτύπωση της πεντάδας και του αθροίσματός τους
                                        print(s[a], s[b], s[c], s[d], s[e])
                                        print(s[a] + s[b] + s[c] + s[d] + s[e])
                                        exit()
                                                                      
                                                                  
                                                                                 
                                                                                         
                                                                                                   
                                                                                                                                                                   
                                                                                          
                                                                                                  
                                                                                
                                                                                                  
                  
           
           
          

                                      
               
