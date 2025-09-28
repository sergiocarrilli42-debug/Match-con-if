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
tipo_de_carrera=int(input("Seleccione el tipo de carrera que estudia: \n"
"1. Ingeniería\n" 
"2. Administración\n"
"3. Medicina\n"))
match tipo_de_carrera:
    case 1: mensualidad=4500*6
    case 2: mensualidad=2700*6
    case 3: mensualidad=6100*6
    case _: 
        print("ERROR! el tipo de carrera no es disponible")
        exit()
promedio_escolar=int(input("Ingrese su promedio escolar: "))
deporte=int(input("Esta inscrito en algún equipo deportivo escolar? \n"
"1. Si\n"
"2. No\n"))
inscripcion=12000
if promedio_escolar >=0 and promedio_escolar<=50:
    descuento_aplicado=0
elif promedio_escolar>=51 and promedio_escolar<=60:
    descuento_aplicado=mensualidad*0.05
elif promedio_escolar>=61 and promedio_escolar<=70:
    descuento_aplicado=mensualidad*0.1
elif promedio_escolar>=71 and promedio_escolar<=80:
    descuento_aplicado=mensualidad*0.5
elif promedio_escolar>=81 and promedio_escolar<=90:
    descuento_aplicado=mensualidad*0.75
elif promedio_escolar>=91 and promedio_escolar<=100:
    descuento_aplicado=mensualidad*1
else: 
    print("ERROR! el promedio ingresado es incorrecto")
    exit()
descuento_deportivo=0
if deporte==1:
    descuento_deportivo=(mensualidad-descuento_aplicado)*0.075
elif deporte==2:
    descuento_deportivo=0
else: 
    print("ERROR! opción de deporte inválida")
    exit()
total=inscripcion+mensualidad-descuento_aplicado-descuento_deportivo
print(f"El el costo de colegiatura por semestre es de {mensualidad:.2f}")
print(f"El descuento por promedio es de {descuento_aplicado:.2f}")
print(f"El descuento de deporte es de {descuento_deportivo:.2f}")
print(f"El costo de inscripción es de {inscripcion:.2f}")
print(f"El total a pagar es de {total:.2f}")