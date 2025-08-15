import random
import time

def bubblesort(novoVetor): 
    """
    Função do bubblesort, onde recebe como parâmetro o vetor que será ordenado.
    """
    flag = True
    menor = novoVetor[0]
    while flag:
        flag = False
        for i in range(len(novoVetor)):
            if i < len(novoVetor) - 1:
                if novoVetor[i] > novoVetor[i+1]:
                    menor = novoVetor[i+1]
                    novoVetor[i+1] = novoVetor[i]
                    novoVetor[i] = menor
                    flag = True    
    return novoVetor

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

print("Antes do Bubblesort com numeros ja ordenados:")
vetor = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(vetor)
print("_________________________________________________________________________")

print("Ordenando o vetor.....")
inicio = time.perf_counter()
bubblesort(vetor)
fim = time.perf_counter()
tempoExecucao = fim-inicio

print("Apos o Bubblesort:")
print(vetor)
print(f"Tempo de execucao: {tempoExecucao:.6f} segundos")
print("_________________________________________________________________________")

print("Nova interacao:")
print("Antes do Bubblesort com numeros nao ordenados:")
vetor = definirVetor(20)
print(vetor)
print("_________________________________________________________________________")

print("Ordenando o vetor.....")
inicio = time.perf_counter()
bubblesort(vetor)
fim = time.perf_counter()
tempoExecucao = fim-inicio

print("Apos o Bubblesort:")
print(vetor)
print(f"Tempo de execucao: {tempoExecucao:.6f} segundos")
print("_________________________________________________________________________")


