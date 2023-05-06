# Títulos
# --------------- Primera parte
print('Desafío 01: Conversión de unidades de tiempo')
print('Primera parte - Convertir segundos a horas:minutos:segundos')

# Carga de datos...
s1 = int(input('Primera cantidad de segundos a convertir: '))
s2 = int(input('Segunda cantidad de segundos a convertir: '))
s3 = int(input('Tercera cantidad de segundos a convertir: '))
s4 = int(input('Cuarta  cantidad de segundos a convertir: '))


# --------------------- Proceso para s1... Todavía no usamos ciclos...
# Cantidad parcial de minutos...
# ... un minuto tiene 60 segundos...
cpm = s1 // 60

# Cantidad final de segundos que quedaron sin convertir...
# ... y ya va al resultado final...
cfs1 = s1 % 60

# Cantidad final de horas, que va al resultado final...
# ... una hora tiene 60 minutos...
cfh1 = cpm // 60

# Cantidad final de minutos que quedaron sin convertir...
# ... y ya va al resultado final...
cfm1 = cpm % 60

# --------------------- Proceso para s2...
cpm = s2 // 60
cfs2 = s2 % 60
cfh2 = cpm // 60
cfm2 = cpm % 60

# --------------------- Proceso para s3...
cpm = s3 // 60
cfs3 = s3 % 60
cfh3 = cpm // 60
cfm3 = cpm % 60

# --------------------- Proceso para s4...
cpm = s4 // 60
cfs4 = s4 % 60
cfh4 = cpm // 60
cfm4 = cpm % 60

# Resultados
print()
if cfh1 <= 24:
    print('Cantidad de segundos: ', s1, '\t\tConvertido: ', cfh1, ':', cfm1, ':', cfs1, sep='')
else:
    print('Cantidad de segundos: ', s1, '\t\tExcedido (conversión no informada)', sep='')

if cfh2 <= 24:
    print('Cantidad de segundos: ', s2, '\t\tConvertido: ', cfh2, ':', cfm2, ':', cfs2, sep='')
else:
    print('Cantidad de segundos: ', s2, '\t\tExcedido (conversión no informada)', sep='')

if cfh3 <= 24:
    print('Cantidad de segundos: ', s3, '\t\tConvertido: ', cfh3, ':', cfm3, ':', cfs3, sep='')
else:
    print('Cantidad de segundos: ', s3, '\t\tExcedido (conversión no informada)', sep='')

if cfh4 <= 24:
    print('Cantidad de segundos: ', s4, '\t\tConvertido: ', cfh4, ':', cfm4, ':', cfs4, sep='')
else:
    print('Cantidad de segundos: ', s4, '\t\tExcedido (conversión no informada)', sep='')

# --------------- Segunda parte
print()
print('Segunda parte - Convertir horas:minutos:segundos a segundos')

# Carga de datos
hini = int(input('Horas: '))
mini = int(input('Minutos: '))
sini = int(input('Segundos: '))

# Procesos
stot = sini + mini*60 + hini*3600

# Resultados
print('Original: ', hini, ':', mini, ':', sini, '\t\tTotal de segundos: ', stot, sep='')


