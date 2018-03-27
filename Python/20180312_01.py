#sommare tutti i quadrati dei numeri da 1 a n con ciclo while

limit =int( input ("Inserire il limite: "))

sumSquare=0
counter = 1

while counter <= limit:
    sumSquare += counter*counter
    counter=counter+1
    
print("la somma è: ", sumSquare)
