#Dado un intervalo de tiempo en minutos, calcular los días, horas y minutos correspondientes.
#BolivarGonzalez 8-887-2405



tiempo = 0
tiempo = int(input("Tiempo: "))
tiempo = tiempo/1440
if tiempo >= 0:
	dias = tiempo
	x = tiempo %140
	horas = x / 60
	minutos = x %60
	print("Cantidad De Dias: " + str(dias) + "Cantidad De Horas: " + str(horas) + "Cantidad de Minutos: "+ str(minutos))
