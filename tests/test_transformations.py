import seleccion_voluntariado_2023 as dt


def test_add_offset():
    augend = 1
    addend = 2
    expected = augend + addend
    obtained = dt.add_offset(augend, addend)
    assert expected == obtained

birds = [ "guacamaya", "ringo", "ave azul", "mirlo cuatro patas"]
print(birds)