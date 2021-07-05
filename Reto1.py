def tiempo_caida_libre(altura: int, masa: int) -> str:
    gravedad = 9.807 
    tiempo = (2*altura/gravedad)**(1/2) 
    return(f"El tiempo que tarda un balón de {masa}kg en caída libre desde una altura de {altura}m en impactar en el suelo es de: {(round(tiempo, 2))} seg")
pass

print((tiempo_caida_libre(10,85)))