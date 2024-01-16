"""
LAS TUPLAS son inmutables
()
"""
tupla = ("uno", "dos", "tres")
print(tupla)
print(type(tupla))

tuplaVariosDatos = (12, True, 23.6, "hola", 12+3j)
print(tuplaVariosDatos)

tuplaConTuplas = (1,2,3,4,(1,2,3))
print(tuplaConTuplas)

print(tuplaVariosDatos[3])
print(tuplaVariosDatos[-2])
print(tuplaVariosDatos[0:2])

a, b, c = tupla
print(a)
print(b)
print(c)