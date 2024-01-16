import os

class OperasBas:
#declaración de propiedades
    num1=0
    num2=0
    res=0


#declaración de contructor
    def __init__(self,a,b):
        self.num1=a
        self.num2=b


#declaracion de metodos de clase
    def suma(self):
        self.res=self.num1+self.num2
        print("La suma es: {}".format(self.res))

def main():
    #Linea para limpiar la terminal
    os.system("cls")
    obj = OperasBas(3,4)
    obj.suma()


if __name__ == "__main__":
    main()