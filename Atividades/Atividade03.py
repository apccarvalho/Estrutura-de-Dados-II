import time

print("Selectionsort com numeros ordenados:")
vetor = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("Antes do Selectionsort:")
print(vetor)
    
print("--------------")

print("Ordenando o vetor.....")

inicio = time.perf_counter()
for i in range(len(vetor)-1):
    menor = vetor[i]
    posicao = i
    for j in range(i+1, len(vetor)):
        if(vetor[j] < menor):
            menor = vetor[j] 
            posicao = j;    
    if posicao != i:
        vetor[posicao], vetor[i] = vetor[i], menor  
fim = time.perf_counter()
tempoExecucao = fim-inicio

print("Apos o Selectionsort:")
print(vetor)
print(f"Tempo de execucao: {tempoExecucao:.6f} segundos")
print("--------------")

print("Selectionsort com numeros nao ordenados:")
vetor = [10,20,15,30,5,1,100,40,86,201,4,106,31,9,16,199,500,3,47,55]
print("Antes do Selectionsort:")
print(vetor)
    
print("--------------")

print("Ordenando o vetor.....")

inicio = time.perf_counter()
for i in range(len(vetor)-1):
    menor = vetor[i]
    posicao = i
    for j in range(i+1, len(vetor)):
        if(vetor[j] < menor):
            menor = vetor[j] 
            posicao = j;    
    if posicao != i:
        vetor[posicao], vetor[i] = vetor[i], menor  
fim = time.perf_counter()
tempoExecucao = fim-inicio

print("Apos o Selectionsort:")
print(vetor)
print(f"Tempo de execucao: {tempoExecucao:.6f} segundos")
print("--------------")