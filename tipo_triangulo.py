#Declaración de variables
lado1 = int(input("Ingrese la longitud del primer lado del triángulo: "))
lado2 = int(input("Ingrese la longitud del segundo lado del triángulo: "))
lado3 = int(input("Ingrese la longitud del tercer lado del triángulo: "))

#condicional que permite verificar si los 3 lados son iguales
if lado1 == lado2 == lado3:
   	 	print("Es un triángulo equilátero")
#condicional que permite verificar si los 3 lados son diferentes
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("Es un triángulo escaleno")
#condicional que permite verificar si dos de sus lados son iguales
elif (lado1==lado2 and lado1 != lado3) or (lado1==lado3 and lado1 != lado2) or(lado2==lado3 and lado2 != lado1):
    		print("Es un triángulo isósceles")

