#practicas de manejo de errores
#ejercicio 1
"""x=input('ingrese un valor')
while not x.isnumeric():
   print('no es un numero entero')
   x=input('ingresa un numero entero')
print(x)"""
"""
x=None
while type(x) is not int:
   try:
      x=int(input('agrega un nuero entero'))
      print(f'numero valido{x}')
   except ValueError:
     print('erroneo el valor')
""" 
#ejercicio 2
"""
def multiplicacion():
  a=None
  b=None
  while type(a) is not int:
     try:
        a=int(input('agrega un nuero entero'))
        print(f'numero valido{a}')
     except ValueError:
        print('erroneo el valor')
  while type(b) is not int:
     try:
        b=int(input('agrega un nuero entero'))
        print(f'numero valido{b}')
     except ValueError:
        print('erroneo el valor')
  return a*b
valor=multiplicacion()
print(valor)"""
#ejercicio 3
#Se quiere hacer un programa que le solicite al usuario un número divisor y un dividendo, y calcule el cociente entre ellos
"""def division():
   divisor=None
   dividendo=None
   while  type(divisor) is not int:
      try:
         divisor=int(input('agrega un numero entero'))
      except ValueError:
         print('erroneo el valor')
      if divisor == 0:
         print('no se puede dividir por 0')
         divisor=None
   while type(dividendo) is not int: 
      try:
         dividendo=int(input('agrega un numero entero'))
      except ValueError:
         print('erroneo el valor')
   return dividendo/divisor
valor=division()
print(valor)"""
#ejercicio 4
#Crear un programa para abrir un archivo llamado “file.txt” en modo lectura y en caso de que este
#archivo no exista, mostrar el mensaje “No se pudo encontrar el archivo file.txt”
"""
try:
   with open('file.txt','r') as file:
      print(file.readlines())
except FileNotFoundError:
   (print('no se pudo encontrar el archivo file.txt'))
else:
   print('el archvio se abrio correctamente')
"""
#ejercicio 5
#Crear una función cuyos parámetros sean una lista y un índice de posición para mostrar el valor de la lista en esa ubicación
"""
lista=['camion','auto','moto','bicicleta','lancha']
def valor_segun_ubicabion (lista):
   indice=None
   while  type(indice) is not int:
      try:
       indice_num=int(input('ingresa un nuemro del indice para conocer su valor en la lista '))
       indice=lista[indice_num]
       return indice
      except IndexError:
        print('el numero no se encuentra en el indice')
      except ValueError:
        print('no es un entero,pon uno')
valor=valor_segun_ubicabion(lista)
print(valor)
"""
#ejercicio 6
#Crear una función que pida al usuario informar el número de jugadores, considerando que este puede ingresa
"""
def chichon():
   cantidad_de_personas = None
   print('para poder jugar se necesitan mas de dos jugadores y menos de 4')
   while type(cantidad_de_personas) is not int:
      try:
         cantidad_de_personas = int(input('cuantos van a jugar'))
         if cantidad_de_personas < 2:
            print('el valor es menor')
            cantidad_de_personas= None
         elif cantidad_de_personas > 4:
            print('el valor es mayor')
            cantidad_de_personas= None
      except ValueError:
         print('el valor no es entero')
   return('pueden jugar')
personas=chichon()
print(personas)
""" 
#Crear una función que pida al usuario informar el número de jugadores, considerando que este puede ingresar
#ejercicio 7
"""
def truco():
   cantidad_pe=None
   print('se puede jugar de a 2,4,6 con un solo mazo')
   while type(cantidad_pe) is not int:
      try:
         cantidad_pe= int(input('cuantos van a jugar'))
         if cantidad_pe < 2:
            print('el valor es menor')
            cantidad_pe= None
         elif cantidad_pe > 6:
            print('el valor es mayor')
            cantidad_pe= None
         elif cantidad_pe % 2 != 0:
            print('no podes jugar ni de a 3 ni de a 5')
            cantidad_pe= None
      except ValueError:
         print('no es un numero')
   return 'a jugaaaar'
personas=truco()
print(personas)
"""
#ejercicio 8
#
opciones = {
1: "hamburguesas",
2: "milanesas",
3: "gaseosa",
4: "alfajor",
5: "papas fritas",
6: "agua"
}
valores = {
1:1000,
2:1500,
3:500,
4:300,
5:600,
6:350
}
valores_opciones={
   1:('hamburguesas',1000),
   2: ("milanesas",1500),
   3: ("gaseosa",500),
   4: ("alfajor",300),   
   5: ("papas fritas",600),
   6: ("agua",350)
}
valores.update(valores_opciones)
for p in valores:
   print(p,valores[p],)
   
def menu():
   o=None
   c=None
   while o not in valores.keys():
      try:
         o=int(input('ingresa una de las opciones con un numero'))
         if o not in valores.keys():
            print('no tenemos esa opcion en el menu')
            o=None
      except ValueError:
         print('agregar un numero entero')
   while type(c) is not int:
      try:
        c=int(input('agrega la cantidad que quieres'))
        if c < 1:
            print('tienes que elegir por lo menos uno')
            c=None
      except ValueError:
         print('no es un entero la cantidad')
   return valores[o][1]*c
total=menu()
print(total)


   
   
         
   
  