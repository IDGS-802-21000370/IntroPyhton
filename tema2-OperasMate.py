num1=20
num2=20

print("La suma es: ", (num1+num2))
print("La resta es: ", (num1-num2))
print("La multiplicacion es: ", (num1*num2))
print("La division es: ", (num1/num2))
print("La potencia es es: ", (num1**num2))

#concatenacion en python

mensaje1 = "hola"
mensaje2 = "mundo"

mesnajeFinal = mensaje1 + " " + mensaje2
print(mesnajeFinal)
print("El saludo es: %s %s" %(mensaje1, mensaje2))

saludoFinal = "Saludo {} {}".format(mensaje1,mensaje2)
print(saludoFinal)


saludoFinal = "Saludo {x} {y}".format(x=mensaje1,y=mensaje2)
print(saludoFinal)

