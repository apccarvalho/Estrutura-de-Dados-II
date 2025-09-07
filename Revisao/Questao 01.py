#Escreva uma função que verifique se um vetor v[0..n-1] está em ordem crescente.

def verificaCrescente(vetor):
    tamanho = len(vetor)
    for i in range(tamanho-1):
        if vetor[i] > vetor[i+1]:
            return False
    return True

vetor1 = [1,2,3,4,5,6]

vetor2 = [1,2,1,3,5,4]    

if verificaCrescente(vetor1):
    print("Ordenado em ordem crescente")
else:
    print("Desordenado")
    
if verificaCrescente(vetor2):
    print("Ordenado em ordem crescente")
else:
    print("Desordenado")
    
       