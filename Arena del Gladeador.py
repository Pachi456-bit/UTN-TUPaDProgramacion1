vida_gladeador = int(100)
vida_enemigo = int(100)
pociones_vida = int(3)
daño_base_ataque_pesado = int(15)
daño_base_enemigo = int(12)
turno_gladeador = True

while True:
    nombre = input("Ingrese su nombre: ")
    print()
    if nombre.isalpha() and nombre != "":
        break
    else:
        print("Error: solo letras")
        print("---------------")
while vida_gladeador > int(0) and vida_enemigo > int(0): 
    print(f"Vida del Gladiador: {vida_gladeador}")
    print(f"Vida del Enemigo: {vida_enemigo}")
    print(f"Pociones Restantes: {pociones_vida}")
    print()
    print("1_Ataque pesado")
    print("2_Rafaga veloz")
    print("3_Curar")
    print("--------------")
    opcion = input("Ingresa que habilidad usar(1-2-3): ")
    if not opcion.isdigit():
            print("Error, ingrese un numero")
            continue
    opcion = int(opcion)
    print("--------------")
    if opcion < 1 or opcion > 3:
         print("Opcion invalida")
         continue
    if opcion == int(1):
        if vida_enemigo < int(20):
             daño = int(daño_base_ataque_pesado*1.5)
             vida_enemigo -= daño
             print(f"Atacaste al enemigo por {daño} puntos de daño")
             daño_base_ataque_pesado = int(15)
             print()
             vida_gladeador -= daño_base_enemigo
             print(f"El enemigo te ataco por {daño_base_enemigo} puntos de daño")
             print("---------------")
        else:
             vida_enemigo -= daño_base_ataque_pesado
             print(f"Atacaste al enemigo por {daño_base_ataque_pesado} puntos de daño")
             daño_base_ataque_pesado = int(15)
             print()
             vida_gladeador -= daño_base_enemigo
             print(f"El enemigo te ataco por {daño_base_enemigo} puntos de daño")
             print("--------------")

    elif opcion == int(2):
         for con in range(1,3+1):
              vida_enemigo -= 5
              print(f"{con}° Golpe conectado por 5")
         print()
         vida_gladeador -= daño_base_enemigo
         print(f"El enemigo te ataco por {daño_base_enemigo} puntos de daño")
         print("---------------")

    elif opcion == int(3):
         if pociones_vida > int(0):
              vida_gladeador += int(30)
              pociones_vida -= int(1)
              print(f"Teas curado +30 de vida")
              print()
              if vida_gladeador > 100:
                   vida_gladeador = 100
              print()
              vida_gladeador -= daño_base_enemigo
              print(f"El enemigo te ataco por {daño_base_enemigo} puntos de daño")
              print("---------------")
         elif pociones_vida <= int(0):
              print("¡¡¡Te quedaste sin pociones!!!")
              print()
              vida_gladeador -= daño_base_enemigo
              print(f"El enemigo te ataco por {daño_base_enemigo} puntos de daño")
              print("---------------")

if vida_gladeador > int(0) and vida_enemigo <= int(0):
     print("¡¡¡VICTORIA!!!")
     print(f"¡¡¡{nombre} HAZ GANADO LA BATALLA!!!")
elif vida_gladeador <= int(0) and vida_enemigo > int(0):
     print("DERROTA")
     print("HAZ CAIDO EN COMBATE")

