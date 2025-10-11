import random

def merge_sort(array):

    if len(array) <= 1:
        return array

    meio = len(array) // 2
    esquerda = array[:meio]
    direita = array[meio:]

    esquerda_ordenada = merge_sort(esquerda)
    direita_ordenada = merge_sort(direita)

    return merge(esquerda_ordenada, direita_ordenada)

def merge(esquerda, direita):

    resultado = []
    i = 0  
    j = 0  

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

def gerar_vetor_aleatorio(tamanho, valor_min=0, valor_max=10000):

    return [random.randint(valor_min, valor_max) for _ in range(tamanho)]


def verificar_ordenacao(array):

    for i in range(len(array) - 1):

        if array[i] > array[i+1]:
            return False

    return True


print("--- Iniciando Testes Experimentais do Merge Sort ---")


tamanhos_para_testar = [10, 100, 1000, 5000, 10000]

for tamanho in tamanhos_para_testar:
    print(f"\n[TESTE] Gerando vetor com {tamanho} elementos...")

    vetor_original = gerar_vetor_aleatorio(tamanho)

    if tamanho <= 10:
        print(f"  -> Vetor Original: {vetor_original}")


    vetor_ordenado = merge_sort(vetor_original)
    if tamanho <= 10:
        print(f"  -> Vetor Ordenado: {vetor_ordenado}")


    esta_correto = verificar_ordenacao(vetor_ordenado)

    if esta_correto:
        print(f"Resultado para {tamanho} elementos: CORRETO (O vetor está ordenado)")
    else:
        print(f"Resultado para {tamanho} elementos: FALHOU (O vetor NÃO está ordenado)")

print("\n--- Testes Concluídos ---")