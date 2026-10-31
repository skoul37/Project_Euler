# Project Euler - Problem 20: Factorial digit sum
# Βρες το άθροισμα των ψηφίων του αριθμού 100! (100 παραγοντικό).

# Συνάρτηση για τον υπολογισμό του παραγοντικού ενός αριθμού (n!)
def paragontiko(n):
    if n == 0:
        return 1
    else:
        return n * paragontiko(n - 1)

# Υπολογισμός του 100!, μετατροπή του σε string, μετατροπή κάθε ψηφίου σε ακέραιο και εκτύπωση του αθροίσματός τους
print(sum(int(i) for i in str(paragontiko(100))))
