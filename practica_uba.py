#prcticas con diccionario en python
"""alumnos = {
   'alumno1':( 'rodrigo',47828881,18,'6to año'),
   'alumno2':( 'juan',47828698,17,'5to año'),
   'alumno3':( 'maria',47828981,16,'4to año'),
   'alumno4':( 'jose',45823581,15,'3er año'),
}
informacion_adicional = {
   'alumno1':( 'rodrigo',47828881,18,'6to año',['division B','juega futbol','prom 9.5']),
   'alumno2':( 'juan',47828698,17,'5to año',['division A','juega voley','prom 8.9']),
   'alumno3':( 'maria',47828981,16,'4to año',['divison C','juega basquet','prom 9.2']),
   'alumno4':( 'jose',45823581,15,'3er año',['division A','juega futbol','prom 9.1']),
}
alumnos.update(informacion_adicional)
print(alumnos['alumno1'])"""
#se necesita un sistema que guarde las plantas a medida que van llegando
"""
def plantas_nuevas(planta_nueva,especie_planta,luz_solar,precio_planta):
   planta_nueva={
      "especie":especie_planta,
      "luz":luz_solar,
      "precio":precio_planta,
   }
   plantas_vivero.append(planta_nueva)
plantas_vivero=[]
plantas_nuevas("rosa","rosa",True,5000)
print(plantas_vivero)
"""
#Se pide hacer una función que reciba el ticket y devuelva el monto total a pagar.
#donde cada diccionario tiene
#la siguiente información:Nombre del producto,Precio por unidad,Cantidad
"""ticket = [
    {'nombre': 'pan', 'precio': 200, 'cantidad': 2},
    {'nombre': 'leche', 'precio': 300, 'cantidad': 1},
    {'nombre': 'huevos', 'precio': 400, 'cantidad': 10},
]

def calcular_total(ticket):
    total = 0
    for producto in ticket:
        total += producto['precio'] * producto['cantidad']
    return total

resultado_ticket=(calcular_total(ticket))
for n in ticket:
   print(n)
print()
print(f'el valor final abonar es {resultado_ticket}')
"""
#cuatro unidad
"""best_movies=[
   {'nombre':'avengers','año':2012,'puntuacion':9},
   {'nombre':'titanic','año':1997,'puntuacion':8},
   {'nombre':'batman','año':2022,'puntuacion':6},
   {'nombre':'el padrino','año':1972,'puntuacion':10},
]   
def mejores_peliculas(best_movies):
      return best_movies['puntuacion'] > 7
         
lista_mejores_peliculas=list(filter(mejores_peliculas, best_movies))
for n in lista_mejores_peliculas:
   print(n)"""
#quinto unidad 5
#Se pide hacer una función que, dado esta lista de diccionarios, devuelva el promedio de las notas en la
#primera oportunidad que rindieron los alumnos
"""
lista_alumnos=[
   {'nombre':'juan','apellido':'perez','intento':1,'nota':10},
   {'nombre':'maria','apellido':'gomez','intento':1,'nota':7},
   {'nombre':'ana','apellido':'martinez','intento':1,'nota':9},
   {'nombre':'pedro','apellido':'sanchez','intento':2,'nota':8},
   {'nombre':'luis','apellido':'lopez','intento':2,'nota':6},
   {'nombre':'carla','apellido':'rodriguez','intento':3,'nota':5},
   {'nombre':'sara','apellido':'fernandez','intento':3,'nota':4}
]
def promedio_notas (a):
   sumar=0
   cantidad_alumnos=0
   for r in lista_alumnos:
    if r['intento'] == a:
      sumar+= r['nota']
      cantidad_alumnos+=1
   resultado=sumar / cantidad_alumnos  
   return int(resultado)
resultado_prom=promedio_notas(3) 
print(resultado_prom)
"""
#Se pide hacer una función que reciba esta lista de diccionarios y elimine todos los productos que no
#pasaron el chequeo de calidad 

productos =[
   {'codigo del producto':2937829,'fecha de vencimiento':'12/12/2025','chequeo de calidad':True},
   {'codigo del producto':2986879,'fecha de vencimiento':'12/03/2025','chequeo de calidad':False},
   {'codigo del producto':2909869,'fecha de vencimiento':'12/02/2025','chequeo de calidad':True},
   {'codigo del producto':2456829,'fecha de vencimiento':'12/10/2025','chequeo de calidad':False}
]
def eliminar_productos(productos):
    return productos['chequeo de calidad'] == True
def productos_mal(productos):
    if productos['chequeo de calidad'] == False:
        return True
lista_productos_apto=list(filter(eliminar_productos,productos))
lista_productos_noapto=list(filter(productos_mal,productos))
cantidad_productos_a=(len(lista_productos_apto))
productos_2=[]
productos_2.append(lista_productos_noapto)
productos_2.append(cantidad_productos_a)
productos_2=tuple(productos_2)
print('productos aptos:')
for n in lista_productos_apto:
 print(n)
print()
print('tupla de productos no aptos,mas la cantidad de productos aptos')
for l in productos_2:
   print(l)




