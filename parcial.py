def calcular_promedio(lista:list,valor:list)->bool:#parametros formales
    acumulador=0
    for i in range(len(lista)):
        acumulador += lista[i]
    promedio = (acumulador / 4)
    if promedio > valor:
        resultado = True
    elif promedio < valor:
        resultado = False
    return resultado
        


entrada = [10,20,30,40]
valor = 24
resultado = calcular_promedio(entrada,valor)#parametros actuales #invocacion
print(resultado)