#En la universidad un alumno paga su mensualidad según la carrera que estudia:
#Carrera	    Pago mensual $
#Ingeniería	        4500
#Adminisitración	2700
#Medicina	        6100
#Pero tiene un descuento adicional, según su promedio escolar
#Promedio	Descuento %
#0-50	        0
#51-60	        5
#61-70	        10
#71-80	        50
#81-90	        75
#91-100	        100
#Considera que la inscripción tiene un valor de $12,000 y que el cobro es por semestre, además si el alumno esta en el equipo deportivo escolar
#se ofrece un descuento del 7.5% adicional al descuento sobre su promedio.
nombre_del_alumno=input("Ingrese su nombre: ")
tipo_de_carrera=int(input("Seleccione el tipo de carrera que estudia: \n"
"1. Ingeniería\n" 
"2. Administración\n"
"3. Medicina\n"))
match tipo_de_carrera:
    case 1: 
        subtotal = 4500 * 6
        carrera="Ingeniería"
    case 2: 
        subtotal = 2700 * 6
        carrera="Administración"
    case 3: 
        subtotal = 6100 * 6
        carrera="Medicina"
    case _:
        print("ERROR! el tipo de carrera no esta disponible")
promedio_escolar = int(input("Ingrese su promedio escolar: "))
deporte = int(input("¿Está inscrito en algún equipo deportivo escolar? \n"
"1. Sí\n"
"2. No\n"))
inscripcion = 12000

if 0 <= promedio_escolar <= 50:
    descuento_promedio = 0
elif 51 <= promedio_escolar <= 60:
    descuento_promedio = subtotal * 0.05
elif 61 <= promedio_escolar <= 70:
    descuento_promedio = subtotal * 0.1
elif 71 <= promedio_escolar <= 80:
    descuento_promedio = subtotal * 0.5
elif 81 <= promedio_escolar <= 90:
    descuento_promedio = subtotal * 0.75
elif 91 <= promedio_escolar <= 100:
    descuento_promedio= subtotal * 1
else: 
    print("ERROR! el promedio ingresado no es válido")
if deporte == 1:
    descuento_deportivo = descuento_promedio* 0.075
    deporte_txt="Inscrito"
elif deporte == 2:
    descuento_deportivo = 0
    deporte_txt="No inscrito"
else: 
    print("ERROR! opción de deporte inválida")
total = inscripcion + subtotal - descuento_promedio - descuento_deportivo
print(f"Nombre: {nombre_del_alumno}")
print(f"Carrera: {carrera}")
print(f"Deporte: {deporte_txt}")
print(f"El costo de colegiatura por semestre es de ${subtotal:.2f}")
print(f"El descuento por promedio es de ${descuento_promedio:.2f}")
print(f"El descuento de deporte es de ${descuento_deportivo:.2f}")
print(f"El costo de inscripción es de ${inscripcion:.2f}")
print(f"El total a pagar es de ${total:.2f}")
