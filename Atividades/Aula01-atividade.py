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

def bubblesort(novoVetor): 
    """
    Função do bubblesort, onde recebe como parâmetro o vetor que será ordenado.
    """
    menor = novoVetor[0]
    for i in range(len(novoVetor)):
        for j in range(len(novoVetor)-1):
            if i < len(novoVetor) - 1:
                if novoVetor[j] > novoVetor[j+1]:
                    menor = novoVetor[j+1]
                    novoVetor[j+1] = novoVetor[j]
                    novoVetor[j] = menor
  
    return novoVetor


vetor = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
menor = vetor[0]

print("Antes do bubblesort com numeros ja ordenados:")
print(vetor)
    
print("--------------")

print("Ordenando o vetor.....")
inicio = time.perf_counter()

bubblesort(vetor)

fim = time.perf_counter()
tempoExecucao = fim-inicio

print("Apos o bubblesort:")
print(vetor)
print(f"Tempo de execucao: {tempoExecucao:.6f} segundos")
print("--------------")

print("Nova interacao:")
vetor = definirVetor(20)
menor = vetor[0]
print("Antes do bubblesort com numeros nao ordenados:")
print(vetor)
    
print("--------------")

print("Ordenando o vetor.....")

inicio = time.perf_counter()
bubblesort(vetor)

fim = time.perf_counter()
tempoExecucao = fim-inicio

print("Apos o buble sorte:")
print(vetor)
print(f"Tempo de execucao: {tempoExecucao:.6f} segundos")
print("--------------")