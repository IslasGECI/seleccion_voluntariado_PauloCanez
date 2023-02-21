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

# esto será todo por hoy, para crear la función de obtener el codigo para las aves, mi punto de partida es obtener 
# las primeras letras de los nombres
