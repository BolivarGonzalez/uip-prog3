#Crear un programa en Python que resuelva el siguiente problema de física: Una ambulancia se mueve con una velocidad de 120 km/h y necesita recorrer un tramo recto de 60km. 
#Calcular el tiempo necesario, en segundos, para que la ambulancia llegue a su destino. La fórmula a utilizar es: velocidad = distancia / tiempo.
#Bolivar Gonzalez 8-887-2405

vel = 120
dis = 60
#vel = dis / tim
tim = dis / vel
tim = tim * 3600 
print('A La Ambulancia Le Toma' +str(tim) +'Segundos En Llegar A Su Destino')
