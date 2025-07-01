def temperatura_media_alta(temperaturas:list, umbral:int)->bool:#parametros formales
    #funcion que recibe dos parametros y saca el promedio de temperatura, y segun eso se fija con un condicional si supera el umbral devuelve true sino devuelve false
    acumulador=0
    es_mayor = False
    for i in temperaturas:
        acumulador += i
    promedio = acumulador / 5
    if promedio > umbral:
        es_mayor = True
    return es_mayor


temperaturas=[18,22,25,20,21]
umbral=20

es_mayor_que_umbral=temperatura_media_alta(temperaturas,umbral)#parametros actuales #invocacion
print(es_mayor_que_umbral)