import seleccion_voluntariado_2023 as dt


def test_add_offset():
    augend = 1
    addend = 2
    expected = augend + addend
    obtained = dt.add_offset(augend, addend)
    assert expected == obtained

birds = [ "guacamaya", "ringo", "ave azul", "mirlo cuatro patas"]  #empezamos con este arreglo para meter nombres de pájaros

for val in range(0,len(birds)):    #con esta función obtenemos la primer letra de todo el string para nombre de los pájaros
  first_letter = birds[val][0] #first letter nos da la primer letra de cada string en el arreglo birds
  print(first_letter)

for val in range(0,len(birds)): #con esta función se obtiene la primer letra de cada nombre de los pájaros
  quit_space = birds[val].lower().split() #con split eliminamos los espacios en cada string con nombre de pajaros y lower nos permite almacenar el primer valor no nulo
  for res in quit_space:   #finalmente, imprimo la primer letra de cada palabra de los nombre de los pajaros
    print(res[0])

#con la siguiente instruccion, se pretende obtener las primeras cuatro letras de cada pájaro

code = [] #iniciamos con un arreglo vacío
for val in range(0,len(birds)):
  i=0 #contador que nos servirá de ayuda
  while i < 4:
    first_letter = birds[val][i] # de aqui obtenemos las primeras letras de los nombres
    code.append(first_letter) #guardamos cada letra con la función append
    i = i+1 #recorremos el contador

#la instruccion anterior nos falla en varios aspectos:
#primero, nos esta dando las cuatro letras de todo el nombre, sin importar las palabras
#segundo, da espacios como si fueran caracteres
#sin embargo, de momento nos sirve

#ahora, con la proxima instruccion planeo detectar donde estan los espacios en los nombres, y con esto poder obtener solamente las letras

#caso 1 espacio
n=birds[2].find(" ") #como el string cuenta con un espacio, entonces se tiene dos palabras, con find encontramos dicho espacio
birds2=[] #pongo un arreglo vacio temporal para el codigo
birds2.append(birds[2][0]) #primer letra de la primer palabra
birds2.append(birds[2][1]) #segunda letra de la primer palabra
birds2.append(birds[2][n+1]) #primer letra de la segunda palabra 
birds2.append(birds[2][n+2]) #segunda letra de la segunda palabra

#caso 2 espacios (equivalente a tres palabras)
n=birds[3].find(" ") #encontramos el primer espacio
m=birds[3].find(" ",n) #encontramos el segundo espacio
birds3=[]
birds3.append(birds[3][0]) #primer letra de la primer palabra
birds3.append(birds[3][n+1]) #primer letra de la segunda palabra
birds3.append(birds[3][n+m+3]) #tercera letra de la tercera palabra
birds3.append(birds[3][n+m+4]) #cuarta letra de la tercera palabra
