from CorrecaoProva import *

array = [5, 3, 8, 4, 2]

verifica(array)

if verifica:
    print("Desordenada")
else:
    print("Ordenada")

bubble_sort(array)
print("BubbleSort: ", array)

array = [95,1,0,82,500]
insertion_sort(array)
print("InsertionSort: ", array)

array = [0,58,1,3,45]
insertion_sort_rec(array)
print("InsertionSort Recursivo: ", array)