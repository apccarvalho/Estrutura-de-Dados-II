import time
import random

def definirVetor(tamanho):
    """
    Função que preenche o vetor com número aleatórios, que recebe como parâmetro o tamanho que será o vetor.
    """
    tamanhoVetor = tamanho
    vetor = []
    limiteInferior = 1
    limiteSuperior = 200

    for i in range(tamanhoVetor):
        numero = random.randint(limiteInferior,limiteSuperior)
        vetor.append(numero)
    return vetor

def insertionSort(novoVetor):
    """
    Função do insertion sort, onde recebe como parâmetro o vetor que será ordenado.
    """
    n = len(novoVetor)
    
    for i in range(1, n):
        chave = novoVetor[i]  
        j = i - 1

        while j >= 0 and novoVetor[j] > chave:
            novoVetor[j + 1] = novoVetor[j]
            j -= 1

        novoVetor[j + 1] = chave
    
    return novoVetor

vetor = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print("Antes do insertionSort com numeros ja ordenados:")
print(vetor)
    
print("----------------------------------------------------------")

print("Ordenando o vetor.....")
inicio = time.perf_counter()

insertionSort(vetor)

fim = time.perf_counter()
tempoExecucao = fim-inicio

print("Apos o insertionSort:")
print(vetor)
print(f"Tempo de execucao: {tempoExecucao:.6f} segundos")
print("----------------------------------------------------------")

print("Nova interacao:")
vetor = definirVetor(20)

print("Antes do insertionSort com numeros nao ordenados:")
print(vetor)
    
print("-----------------------------------------------------------")

print("Ordenando o vetor.....")

inicio = time.perf_counter()
insertionSort(vetor)

fim = time.perf_counter()
tempoExecucao = fim-inicio

print("Apos o insertion sort:")
print(vetor)
print(f"Tempo de execucao: {tempoExecucao:.6f} segundos")
print("-----------------------------------------------------------")