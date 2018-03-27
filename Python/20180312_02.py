#sommare tutte le potenze dei numeri da 1 a n con ciclo for

limit =int( input ("Inserire il limite: "))

sumPowers=0
counter = 1

for counter in range(1,limit +1):
    sumPowers+= counter**counter    
    print(counter, counter**counter, sumPowers, sep="\t")

print("la somma è: ", sumPowers)
