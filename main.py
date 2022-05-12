import sys


def componentesDelGrafo(arr):
    maxa = max(arr)
    mina = min(arr)

    if arr[0] == maxa:
        return 1
    partirEn = arr.index(maxa)

    if arr[0] == mina:
        return 1 + componentesDelGrafo(arr[1: len(arr)])

    arrIzq = arr[0: partirEn]
    arrDer = arr[partirEn: len(arr)]

    maxIzq = max(arrIzq)
    minDer = min(arrDer)

    if maxIzq > minDer:
        return 1
    else:
        return componentesDelGrafo(arrIzq) + componentesDelGrafo(arrDer)


# a= [3,2,1,6,5,4]
# print(componentesDelGrafo(a))





if __name__ == '__main__':
    
    lec = input().split('\n')
    
    nCasos = int(lec[0])
    print("numero de casos: ", nCasos)
    for i in range(1, nCasos + 1):
        casoStr = lec[i].split(" ")
        caso = [int(i) for i in casoStr] #Convertimos los strings del arreglo en enteros
        #print(caso)
        print(componentesDelGrafo(caso))
    
    # # Cómo vrg se leen varias líneas en Python? aaaaaaaaaaaaa
    # Creo que yo sé B) 
    #
    # contents = sys.stdin.readlines()
    # loscasos = contents.split("\n")
    # numero = int(loscasos[0])

    # for i in range(numero - 1):
    #     arreglo = loscasos[i].split()
    #     print(componentesDelGrafo(arreglo))
