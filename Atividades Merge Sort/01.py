def mergesort_decrescente(v, inicio, fim):

    if inicio < fim:
        # Encontra o meio para dividir o vetor em dois subvetores
        meio = (inicio + fim) // 2
        
        mergesort_decrescente(v, inicio, meio) #primeira metade
        mergesort_decrescente(v, meio + 1, fim)#segunda metade

        # Cria listas temporárias para as duas metades ordenadas
        esquerda = v[inicio : meio + 1]
        direita = v[meio + 1 : fim + 1]

        i = 0  # Ponteiro para a lista da esquerda
        j = 0  # Ponteiro para a lista da direita
        k = inicio  # Ponteiro para o subvetor original v[inicio...fim]

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] >= direita[j]:
                v[k] = esquerda[i]
                i += 1
            else:
                v[k] = direita[j]
                j += 1
            k += 1

        # Copia os elementos restantes da lista esquerda, se houver
        while i < len(esquerda):
            v[k] = esquerda[i]
            i += 1
            k += 1

        # Copia os elementos restantes da lista direita, se houver
        while j < len(direita):
            v[k] = direita[j]
            j += 1
            k += 1

vetor_exemplo = [38, 27, 43, 3, 9, 82, 10]
print(f"Vetor Original: {vetor_exemplo}")

mergesort_decrescente(vetor_exemplo, 0, len(vetor_exemplo) - 1)

print(f"Vetor Ordenado (Decrescente): {vetor_exemplo}")