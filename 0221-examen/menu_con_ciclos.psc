Algoritmo el_menu_con_ciclos
	opcion_menu <- 0
	Mientras opcion_menu < 5 Hacer
		Escribir "    Menu"
		Escribir "1. Suma"
		Escribir "2. Resta"
		Escribir "3. Multiplicacion"
		Escribir "4. Division"
		Escribir "5. Salir"
		Escribir "Opcion:"
		Leer opcion_menu
		si opcion_menu = 1 entonces
			Escribir "Ingresa el primer numero"
			Leer n1
			Escribir "Ingresa el segundo numero"
			Leer n2
			resultado <- n1 + n2 
			Escribir "El resutlado es ", resultado
		FinSi
		si opcion_menu = 2 entonces
			Escribir "Ingresa el primer numero"
			Leer n1
			Escribir "Ingresa el segundo numero"
			Leer n2
			resultado <- n1 - n2 
			Escribir "El resutlado es ", resultado
		FinSi
		Segun opcion_menu Hacer
			3:
				Escribir "Ingresa el primer numero"
				Leer n1
				Escribir "Ingresa el segundo numero"
				Leer n2
				resultado <- n1 * n2 
				Escribir "El resutlado es ", resultado
			4:
				Escribir "Ingresa el primer numero"
				Leer n1
				Escribir "Ingresa el segundo numero"
				Leer n2
				resultado <- n1 / n2 
				Escribir "El resutlado es ", resultado
		Fin Segun
	FinMientras
	
FinAlgoritmo
