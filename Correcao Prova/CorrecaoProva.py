#Questão 01

def verifica(lista):
    n=len(lista)
    for i in range (1,n):
        if lista[i-1] > lista[i]:
            return False
        return True
    

#Questão 02
def bubble_sort(array):
    n=len(array)
    for i in range(n-1):
        flag = False
        for j in range (n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = True
        if not flag:
            break
    
#Questão 06
def insertion_sort(array):
    n = len(array)
    for i in range(1,n):
        chave = array[i]
        j = i-1
        while j >=0 and array[j] > chave:
            array[j + 1] = array[j]
            j -= 1
        array[j+1] = chave

#Questão 7
def insertion_sort_rec(array, n=None):
    if n is None:
        n = len(array)

    if n <= 1:
        return

    insertion_sort_rec(array, n-1)

    chave = array[n-1]
    j = n-2
    while j >= 0 and array[j] > chave:
        array[j+1] = array[j]
        j -= 1
    array[j+1] = chave
    