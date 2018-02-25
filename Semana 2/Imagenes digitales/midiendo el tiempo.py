from math import sin #para usar la función seno
 
from time import time #importamos la función time para capturar tiempos
 
x = list(range(0,100)) #vector de valores desde 0 a 99
y = [0.0 for i in range(len(x))] #inicializamos el vector de resultados con 100 valores 0.0
 
tiempo_inicial = time() 
 
for i in range(100):
 
    y[i] = sin(x[i])
 
tiempo_final = time() 
 
tiempo_ejecucion = tiempo_final - tiempo_inicial
 
print ('El tiempo de ejecucion fue:',tiempo_ejecucion) #En segundos