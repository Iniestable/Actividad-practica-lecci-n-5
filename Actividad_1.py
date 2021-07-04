import pandas as pd
try: 
    df = pd.read_csv("finanzas2020.csv", delimiter = "\t")
    contador = 0
    for i in df:
        contador = contador + 1
except IOError:
    print("No he encontrado el fichero")
else:
    print(f"El fichero se ha leido correctamente y tiene {contador} columnas")


#BUCLE PARA VER LOS VALORES DEL FICHERO Y SUSTITUIRLO POR 0 EN CASO DE QUE SE ENCUENTRE UN ERROR 
for i in df:    
    try:
        df[i] = pd.to_numeric(df[i], downcast='float')   #Con el valor coerce lo que se consigue es poner un nan en los datos que no se puedan transformar 
    except ValueError:
        df[i] = 0

#BUCLE PARA CALCULAR EL MES DE MÁXIMO GASTO
a = 0
b = 0   
for i in df:        #Con este bucle recorro todas las columnas 
    for j in df.index:  #Con este todas las filas
        if (df[i][j] < 0):     #Si el número es negativo, los sumo
            a = a + df[i][j]
    if (b > a):             #En b guardo el numero más pequeño y el mes en el que se encuentra 
        b = a 
        mes = i
    a = 0
print(f"El mes en el que más se gasta es: {mes} con un total de {b}")

#BUCLE PARA CALCULAR EL MES EN EL QUE SE HA AHORRADO MÁS 
total = 0
suma = 0
for i in df:
    for j in df.index:
        suma = suma + df[i][j]      #Voy sumando todos los datos
    if (suma > total):              #Si la suma es mayor que el total entro en esta condición
        total = suma
        mes = i
    suma = 0            #Reseteo la variable
print(f"El més donde se ha ahorrado más ha sido en {mes} con un valor de {total}")

#BUCLE PARA CALCULAR LA MEDIA DE GASTOS AL AÑO
gasto = 0
a = 0  
contador = 0 
for i in df:        #Con este bucle recorro todas las columnas 
    for j in df.index:  #Con este todas las filas
        if (df[i][j] < 0):     #Si el número es negativo, los sumo
            a = a + df[i][j]
    gasto = gasto + a
    a = 0
    contador = contador + 1     #Mediante la variable contador puedo ver el número de veces que se hace el bucle
media = gasto/contador
print(f"El gasto medio a lo largo del año ha sido de: {media}")

#BUCLE PARA CALCULAR EL GASTO TOTAL 
gasto = 0
a = 0   
for i in df:        #Con este bucle recorro todas las columnas 
    for j in df.index:  #Con este todas las filas
        if (df[i][j] < 0):     #Si el número es negativo, los sumo
            a = a + df[i][j]
    gasto = gasto + a
    a = 0
print(f"El gasto total a lo largo del año ha sido de: {gasto}")

#BUCLE PARA CALCULAR LOS INGRESOS
ingreso = 0
a = 0   
for i in df:        #Con este bucle recorro todas las columnas 
    for j in df.index:  #Con este todas las filas
        if (df[i][j] > 0):     #Si el número es positivo, los sumo
            a = a + df[i][j]
    ingreso = ingreso + a
    a = 0
print(f"Los ingresos totales a lo largo del año han sido de: {ingreso}")
