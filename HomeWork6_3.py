Multiplication  = input("Enter number: ")

MultiplicationFin = Multiplication[0]
while len(Multiplication) > 1:
    MultiplicationFin = str( int(MultiplicationFin) * int(Multiplication[1]) )
    Multiplication = Multiplication[1:]
    if int(MultiplicationFin) >= 9 and len(Multiplication) == 1 :
        Multiplication = MultiplicationFin
        MultiplicationFin = MultiplicationFin[0]

print(MultiplicationFin)


