#Escreva uma função que permute os elementos de um vetor inteiro v[0..n-1] de modo que
#eles fiquem em ordem decrescente. Inspire-se no algoritmo Selectionsort.

def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        max_index = i 
        for j in range(i + 1, n):
            if array[j] > array[max_index]:
                max_index = j
        if max_index != i:
            array[i], array[max_index] = array[max_index], array[i] 

lista = [11,4,30,22,7,26]
selection_sort(lista)
print(lista)  