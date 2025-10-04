#Questão 01
def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
                
def inserir_ordenado(array, x):
    array.append(x)
    n =len(array)
    bubble_sort(array)

#Questão 02    
def selection_sort_inverso(array):
    listaDesordenada = list(array)
    n=len(listaDesordenada)
    listaOrdenada = []
    for i in range(n):
        maiorElemento = max(listaDesordenada)
        listaDesordenada.remove(maiorElemento)
        listaOrdenada.append(maiorElemento)
    return listaOrdenada

#Questão 04

def insertion_sort(array):
    n = len(array)
    for i in range (1,n):
        chave = array[i]
        j = i - 1
        while j >= 0 and len(array[j]) > len(chave):
            array[j+1] = array[j]
            j -= 1
        array[j+1] = chave

array = [4,11,30,57,2]
print(array)
novo_array = selection_sort_inverso(array)
print(novo_array)

arrayNomes = ['Ana', 'Roberto', 'Beatriz', 'Daiana', 'Junio', 'Joao', 'Lu']
print(arrayNomes)
insertion_sort(arrayNomes)
print(arrayNomes)