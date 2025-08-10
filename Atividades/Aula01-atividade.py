vetor = [10,20,15,30,5,1,100]
menor = vetor[0]
flag = True

print("Antes do buble sorte:")
for i in range(len(vetor)):
    print(vetor[i])
    
print("--------------")

print("Ordenando o vetor.....")

while flag:
    flag = False
    for i in range(len(vetor)):
        if i < len(vetor) - 1:
            if vetor[i] > vetor[i+1]:
                menor = vetor[i+1]
                vetor[i+1] = vetor[i]
                vetor[i] = menor
                flag = True

print("Apos o buble sorte:")
for i in range(len(vetor)):
    print(vetor[i])

print("--------------")