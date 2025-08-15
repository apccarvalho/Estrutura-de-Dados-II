vetor = [10,20,15,30,5,1,100]

print("Antes do Selectionsort:")
for i in range(len(vetor)):
    print(vetor[i])
    
print("--------------")

print("Ordenando o vetor.....")


for i in range(len(vetor)-1):
    menor = vetor[i]
    posicao = i
    for j in range(i+1, len(vetor)):
        if(vetor[j] < menor):
            menor = vetor[j] 
            posicao = j;    
    if posicao != i:
        vetor[posicao], vetor[i] = vetor[i], menor  

print("Apos o Selectionsort:")
for i in range(len(vetor)):
    print(vetor[i])

print("--------------")