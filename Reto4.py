def procesar_frase(frase_celebre_programacion: str)->dict:
    
    quitar = "‘’,;:.\n!\"'´"
    for caracter in quitar:
        frase_celebre_programacion = frase_celebre_programacion.replace(caracter, "")
        
    lista = frase_celebre_programacion.split()
    repetidos = {}

    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j:
                if lista[i] == lista[j] and lista[i] not in repetidos:
                   
                    repetidos[lista[i]] = lista.count(lista[i])
                                    
    return repetidos
        
print(procesar_frase("Depurar código es dos veces más difícil que escribir código, por lo tanto, si escribes el código tan inteligentemente como te sea posible, por definición no serás lo suficientemente inteligente como para depurarlo"))