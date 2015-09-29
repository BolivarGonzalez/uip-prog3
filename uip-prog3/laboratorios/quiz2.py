#El Emperador esta celebrando aniversario y ofrecera a sus clientes una serie de ofertas que se traduciran en un incremento en sus ventas. las reglas de las ofertas se basan en un porcentaje de descuento sobre el total de la compra
#por un monto mayor a 500 descuento de 30%
#por un monto menor de 500 pero mayor o igual a 200 descuento de 20%
#por un monto menor de 200 pero mayor o igual a 100 descuento del 10%

clientes = 0
while clientes <=6:
	compra = int(input("Monto: "))
	
	clientes = clientes + 1
	if compra >= 500:
		descuento=compra*0.30
		tp=compra-descuento
		print("El Monto A Pagar Es De:" + str(tp) +"Con Un Descuento Total De: " + str(descuento))
	if compra<500 and compra>=200:
		descuento=compra*0.20
		tp=compra-descuento
		print("El Monto A Pagar Es De:" + str(tp) +"Con Un Descuento Total De: " + str(descuento))
	if compra<200 and compra>=100:
		descuento=compra*0.10
		tp=compra-descuento
		print("El Monto A Pagar Es De:" + str(tp) +"Con Un Descuento Total De: " + str(descuento))
			
	else: 
		print('El Monto A Pagar Es De: ' +str(compra))
