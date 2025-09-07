#Escreva uma função que receba um inteiro x e um vetor v[0..n-1] de inteiros em ordem 
#crescente e insira x no vetor de modo a manter a ordem crescente.

def insereNaOrdem(vetor, numero):
    tamanho = len(vetor)
    for i in range(tamanho-1):
        if vetor[i] > numero:
            vetor.insert(i, numero)
            return vetor
    vetor.append(numero)
    
    return vetor
    
vetor = [1,3,4,5,6,7]

print(vetor)

numero = 8

print(insereNaOrdem(vetor, numero))

