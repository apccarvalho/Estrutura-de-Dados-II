#Invente um algoritmo de ordenação que seja mais rápido que o de inserção e o de seleção.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr


def intercalar(esq, dir):
    i, j = 0, 0
    resultado = []

    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1

    
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado


def sort_parcial(arr):
    
    if len(arr) <= 10:
        return insertion_sort(arr)

    meio = len(arr) // 2
    esquerda = sort_parcial(arr[:meio])
    direita = sort_parcial(arr[meio:])

    return intercalar(esquerda, direita)


valores = [8, 3, 5, 1, 7, 2, 9, 6, 4]
print("Original:", valores)
ordenado = sort_parcial(valores)
print("Ordenado:", ordenado)
