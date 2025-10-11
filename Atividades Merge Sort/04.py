import random
import time
import math


def merge_sort_recursivo(array):
    if len(array) <= 1:
        return array
    meio = len(array) // 2
    esquerda = merge_sort_recursivo(array[:meio])
    direita = merge_sort_recursivo(array[meio:])
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i, j = 0, 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado


def merge_sort_iterativo(array):

    n = len(array)
    tamanho_subvetor = 1

    while tamanho_subvetor < n:
        inicio = 0
        while inicio < n:
            meio = min(inicio + tamanho_subvetor - 1, n - 1)
            fim = min(inicio + 2 * tamanho_subvetor - 1, n - 1)
            
            intercalar_in_place(array, inicio, meio, fim)
            
            inicio += 2 * tamanho_subvetor
        tamanho_subvetor *= 2
    return array

def intercalar_in_place(v, inicio, meio, fim):

    esquerda = v[inicio : meio + 1]
    direita = v[meio + 1 : fim + 1]
    i, j, k = 0, 0, inicio
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            v[k] = esquerda[i]
            i += 1
        else:
            v[k] = direita[j]
            j += 1
        k += 1
    while i < len(esquerda):
        v[k] = esquerda[i]
        i += 1
        k += 1
    while j < len(direita):
        v[k] = direita[j]
        j += 1
        k += 1


tamanhos = [100, 1000, 5000, 10000, 25000, 50000]
resultados = []

print("Iniciando comparação entre Merge Sort Recursivo e Iterativo...")
    
for tamanho in tamanhos:

    vetor_original = [random.randint(0, tamanho) for _ in range(tamanho)]
        
    vetor_para_rec = vetor_original.copy()
    t_inicio_rec = time.perf_counter()
    vetor_ordenado_rec = merge_sort_recursivo(vetor_para_rec)
    t_fim_rec = time.perf_counter()
    tempo_rec = t_fim_rec - t_inicio_rec

    vetor_para_iter = vetor_original.copy()
    t_inicio_iter = time.perf_counter()
    vetor_ordenado_iter = merge_sort_iterativo(vetor_para_iter)
    t_fim_iter = time.perf_counter()
    tempo_iter = t_fim_iter - t_inicio_iter

    resultados.append((tamanho, tempo_rec, tempo_iter))
    print(f"Teste concluído para vetores de tamanho {tamanho}.")


print("\n" + "="*55)
print("||" + "Tabela de Resultados de Tempo de Execução".center(51) + "||")
print("="*55)
print(f"|| {'Tamanho do Vetor':<18} | {'Recursivo (s)':<15} | {'Iterativo (s)':<15} ||")
print("||" + "-"*51 + "||")
for tamanho, tempo_rec, tempo_iter in resultados:
    print(f"|| {tamanho:<18} | {tempo_rec:<15.6f} | {tempo_iter:<15.6f} ||")
    print("="*55)