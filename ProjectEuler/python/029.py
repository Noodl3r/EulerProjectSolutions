# How many distinct terms are in the sequence generated by a^b for 2 <= a <= 100 and 2 <= b <= 100

# Solution found : 9183


terms = {}
for a in range(2, 101):
    for b in range(2, 101):
        if a**b in terms:
            continue
        terms[a**b] = True
print(len(terms))
