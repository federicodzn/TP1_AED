# Ingreso de datos
patente = input("Ingrese la patente del vehículo: ")
tipo_vehiculo = int(input("Ingrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): "))
forma_pago = int(input("Ingrese la forma de pago (1: manual, 2: telepeaje): "))
pais = int(input("Ingrese el país donde se encuentra la cabina (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay): "))
distancia = float(input("Ingrese la distancia recorrida desde la última cabina en kilómetros: "))
print()

# Validación de la patente
if len(patente) == 7:
    if patente[:2].isalpha() and patente[2:5].isdigit() and patente[5:].isalpha():
        print("El vehículo corresponde a el país de Argentina")
    elif patente[:3].isalpha() and patente[3:].isdigit():
        print("El vehículo corresponde a el país de Uruguay")
    elif patente[:2].isalpha() and patente[2:].isdigit():
        print("El vehículo corresponde a el país de Bolivia")
    elif patente[:4].isalpha() and patente[4:].isdigit():
        print("El vehículo corresponde a el país de Paraguay")
    elif patente[:3].isalpha() and patente[3:4].isdigit() and patente[4:5].isalpha() and patente[5:].isdigit():
        print("El vehículo corresponde a el país de Brasil")
    else:
        print("El vehículo es de otro país")
else:
    print("El vehículo es de otro país")

# Cálculo del importe básico
if pais == 2:
    importe_base = 400
elif pais == 1:
    importe_base = 200
else:
    importe_base = 300

if tipo_vehiculo == 0:
    importe_base *= 0.5
elif tipo_vehiculo == 2:
    importe_base *= 1.6

print("El importe básico a pagar por el vehículo es:", importe_base)

# Aplicación del descuento por telepeaje
if forma_pago == 2:
    importe_final = importe_base * 0.9
else:
    importe_final = importe_base

print("El valor final del ticket es:", importe_final)

# Cálculo del valor promedio pagado por kilómetro recorrido
if distancia != 0:
    valor_promedio_por_kilometro = round(importe_final / distancia, 2)
    print("El valor promedio pagado por kilómetro recorrido es:", valor_promedio_por_kilometro)
else:
    print("No aplica el cálculo del promedio porque los kilometros recorridos son 0")
