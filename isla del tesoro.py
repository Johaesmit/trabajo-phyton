print("Bienvenido a el juego LA ISLA DEL TESORO.\n Tipo de usuario\n\t1- Pirata \n\t2- Soldado\n")
tipo = input("Introduce el número correspondiente a usuario que deseas:")

if tipo == "1":
    print("LISTO PARA LA BÚSQUEDA DEL TESORO RESUELVE EL ACERTIJO\n\t 1-El Capitán Blood enterró monedas de oro, pero no lo hizo en el centro de la isla.lo enterró en la coordenada de una circunferencia en el ángulo 360 menos la suma de los ángulos de un triángulo su respuesta lo llevará al tesoro  \n\t2-El capitán Blood , se gira 360 grados dando la vuelta y descubre que no hay huellas. Tampoco había viento que las pudiera borrar. ¿Por qué no había huellas? El pirata caminaba hacia atrás y el tesoro está en la mitad del camino ")
    ingrediente = input("Introduce  solo tres dígitos con la respuesta a el acertijo: ")
    print("El  tesoro del Capitán Blood:", end="")
    if ingrediente == "180":
        print("es tuyo pirata GANASTE  ")
    else: 
        print("El soldado encontró primero el tesoro GAME OVER")
else:
    print("LISTO PARA LA BÚSQUEDA DEL TESORO SOLDADO  RESUELVE LOS ACERTIJOS \n\t1- El camino del pirata deja huellas date por vencido el  pirata caminaba hacia atrás solo si sabes la el octavo número primo más uno  \n\t2-Cuántos 9 hay entre el 1 y el 100 \n")
    ingrediente = input("INTRODUCE SOLO DÍGITOS PARA LA RESPUESTA ")
    print("El tesoro del capitán Blood:", end="")
    if ingrediente == "20":
        print("Es tuyo soldado GANASTE")
    else :
        print("El pirata encontró primero el tesoro GAME OVER ")

