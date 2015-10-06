#dado un intervalo de tiempo en segundos, calcular los segundos restantes que corresponden para convertirse en minuto. Este programa debe funcionar para 5 oportunidades
#Bolivar Gonzalez
for x in range (0, 5):
	segundos = int(input("Segundos: "))
	minutos = segundos / 60
	if minutos != 0:
		segundos = 60-segundos %60
		print(segundos)
