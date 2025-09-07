#Escreva uma versão recursiva do algoritmo de ordenação por seleção.

def selection_sort_recursive(array):

    def _selection_sort(arr, start_index):
       
        if start_index >= len(arr) - 1:
            return
        
        min_index = start_index
        for i in range(start_index + 1, len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i
        
        arr[start_index], arr[min_index] = arr[min_index], arr[start_index]
        
        _selection_sort(arr, start_index + 1)
    
    _selection_sort(array, 0)