#Escreva uma versão recursiva do algoritmo de ordenação por inserção


def insertion_sort_recursive(array):
    
    def _insertion_sort(array, n):
        if n <= 1:
            return
        
        _insertion_sort(array, n-1)
        
        ultimo = array[n-1]
        j = n-2
        
        while j >= 0 and array[j] > ultimo:
            array[j+1] = array[j]
            j -= 1
        
        array[j+1] = ultimo
    
    _insertion_sort(array, len(array))
    
arr1 = [5, 4, 3, 2, 1]
insertion_sort_recursive(arr1)
print(f"Teste 1: {arr1}")    