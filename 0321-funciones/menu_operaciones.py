import math

def menu():
    print("    Menu")
    print("1. Área de rectángulo")
    print("2. Área de triángulo")
    print("3. Área de cuadrado")
    print("4. Área de circulo")
    print("5. Salir")
    opcion = eval(input("Opción: "))
    return opcion

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return base * altura / 2

def area_circulo(radio):
    return radio**2 * math.pi

opcion_menu = 0
while opcion_menu != 5:
    opcion_menu = menu()
    
    if opcion_menu == 1:
        base = eval(input("Escribe el valor de la base: "))
        altura = eval(input("Escribe el valor de la altura: "))
        area = area_rectangulo(base, altura)
        print("El área es: ", area)
    elif opcion_menu == 2:
        base = eval(input("Escribe el valor de la base: "))
        altura = eval(input("Escribe el valor de la altura: "))
        area = area_triangulo(base, altura)
        print("El área es: ", area)
    elif opcion_menu == 3:
        lado = eval(input("Escribe el valor de un lado: "))
        area = area_rectangulo(lado, lado)
        print("El área es: ", area)
    elif opcion_menu == 4:
        radio = eval(input("Escribe el valor del radio: "))
        area = area_circulo(radio)
        print("El área es: ", area)        
    elif opcion_menu == 5:
        pass
    else:
        print(" -- Opción invalida")
    
    

                  
                  