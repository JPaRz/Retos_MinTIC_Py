def analisis_datos_nav(lista_datos_nav: list)->dict:
    
    enteros = []
    flotantes = [] 
    cadenas = []
    booleanos = []
    tuplas = []
    listas = []
    diccionario = [] 
    
    for elemento in lista_datos_nav:
        if type(elemento) == int:
            enteros.append(elemento)
        elif type(elemento) == float:
            flotantes.append(elemento)
        elif type(elemento) == str:
            cadenas.append(elemento)
        elif type(elemento) == bool:
            booleanos.append(elemento)
        elif type(elemento) == tuple:
            tuplas.append(elemento)
        elif type(elemento) == list:
            listas.append(elemento)
        elif type(elemento) == dict:
            diccionario.append(elemento)
        
        dic = {
            "int":enteros,
            "float":flotantes,
            "str":cadenas,
            "bool":booleanos,
            "tuple":tuplas,
            "list":listas,
            "dict":diccionario
        }
     
    return dic
     
print(analisis_datos_nav([560, 'a', False, 10, 23.2, True, 'x', (1, ), {'a':'a'}, [23, 'b']]))