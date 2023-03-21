Funcion opcion_menu <- menu()
	Escribir "    Menu"
	Escribir "1. Area rectangulo"
	Escribir "2. Area triangulo"
	Escribir "3. Area cuadrado"
	Escribir "4. Area circulo"
	Escribir "5. Salir"
	Escribir "Opcion: "
	Leer opcion_menu
Fin Funcion

Funcion area <- area_rectangulo ( base, altura )
	area = base * altura
Fin Funcion

Funcion area <- area_triangulo ( base, altura )
	area = base * altura / 2
Fin Funcion

Funcion area <- area_circulo ( radio )
	area = radio^2 * PI
Fin Funcion

Algoritmo menu_de_areas
	opcion_menu <- 0
	Mientras opcion_menu <>  5 Hacer
		opcion_menu <- menu()
		Segun opcion_menu Hacer
			1:
				Escribir "Escribe el valor de la base:"
				Leer base
				Escribir "Escribe el valor de la altura:"
				Leer altura
				area <- area_rectangulo(base, altura)
				Escribir "El area es ", area
			2:
				Escribir "Escribe el valor de la base:"
				Leer base
				Escribir "Escribe el valor de la altura:"
				Leer altura
				area <- area_triangulo(base, altura)
				Escribir "El area es ", area
			3:
				Escribir "Escribe el valor de un lado:"
				Leer lado
				area <- area_rectangulo(lado, lado)
				Escribir "El area es ", area
			4:
				Escribir "Escribe el valor del radio:"
				Leer radio
				area <- area_circulo(radio)
				Escribir "El area es ", area
			De Otro Modo:
				Escribir "Opcion invalida"
		Fin Segun
	Fin Mientras
FinAlgoritmo
