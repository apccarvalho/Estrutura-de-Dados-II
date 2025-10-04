"""
   Ordena um array utilizando o algoritmo Merge Sort.

    Args:
        array: Uma lista de elementos comparáveis (ex: números).

    Returns:
        Uma nova lista contendo os elementos ordenados.
"""
    # Caso base da recursão: se a lista tem 1 ou 0 elementos,
    # ela já está ordenada.
def merge_sort(array):
    if len(array) <= 1:
        return array
    # 1. Etapa de DIVISÃO
    meio = len(array) // 2
    esquerda = array[:meio]
    direita = array[meio:]
    # Chamada recursiva para ordenar cada metade
    esquerda_ordenada = merge_sort(esquerda)
    direita_ordenada = merge_sort(direita)
    # 2. Etapa de COMBINAÇÃO (Merge)
    return merge(esquerda_ordenada, direita_ordenada)

def merge(esquerda, direita):
    """
    Função auxiliar que combina duas listas já ordenadas em uma única
    lista ordenada.
    """
    resultado = []
    i = 0  # Ponteiro para a lista da esquerda
    j = 0  # Ponteiro para a lista da direita
    # Compara os elementos das duas listas e adiciona o menor ao resultado
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[i]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    # Ao final do loop, uma das listas pode ainda ter elementos restantes.
    # Adiciona todos os elementos restantes da lista esquerda (se houver).
    resultado.extend(esquerda[i:])
    # Adiciona todos os elementos restantes da lista direita (se houver).
    resultado.extend(direita[j:])
    
    return resultado

lista_desordenada = [38, 27, 43, 3, 9, 82, 10]
print(f"Lista Original: {lista_desordenada}")

lista_ordenada = merge_sort(lista_desordenada)
print(f"Lista Ordenada: {lista_ordenada}")