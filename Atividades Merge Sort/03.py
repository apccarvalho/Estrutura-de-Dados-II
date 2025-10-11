# A função de intercalação não muda, então a definimos uma vez.
def intercalar_decrescente(v, inicio, meio, fim):
    esquerda = v[inicio : meio + 1]
    direita = v[meio + 1 : fim + 1]
    i, j, k = 0, 0, inicio
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] >= direita[j]:
            v[k] = esquerda[i]
            i += 1
        else:
            v[k] = direita[j]
            j += 1
        k += 1
    while i < len(esquerda):
        v[k] = esquerda[i]
        i += 1
        k += 1
    while j < len(direita):
        v[k] = direita[j]
        j += 1
        k += 1

# --- Versão Padrão ---
def mergesort_padrao(v, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim) // 2
        mergesort_padrao(v, inicio, meio)
        mergesort_padrao(v, meio + 1, fim)
        intercalar_decrescente(v, inicio, meio, fim)

# --- Variação 1 ---
def mergesort_variacao1(v, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim - 1) // 2
        mergesort_variacao1(v, inicio, meio)
        mergesort_variacao1(v, meio + 1, fim)
        intercalar_decrescente(v, inicio, meio, fim)

# --- Variação 2 ---
def mergesort_variacao2(v, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim + 1) // 2
        mergesort_variacao2(v, inicio, meio)
        mergesort_variacao2(v, meio + 1, fim)
        intercalar_decrescente(v, inicio, meio, fim)

# --- Bloco de Teste ---
if __name__ == "__main__":
    vetor_original = [38, 27, 43, 3, 9, 82, 10, 55]
    print(f"Vetor Original: {vetor_original}\n")

    # Testando a versão padrão
    v_padrao = vetor_original.copy()
    mergesort_padrao(v_padrao, 0, len(v_padrao) - 1)
    print(f"Resultado Padrão (inicio + fim) // 2:             {v_padrao}")

    # Testando a Variação 1
    v_var1 = vetor_original.copy()
    mergesort_variacao1(v_var1, 0, len(v_var1) - 1)
    print(f"Resultado Variação 1 (inicio + fim - 1) // 2:    {v_var1}")

    # Testando a Variação 2
    v_var2 = vetor_original.copy()
    print("Testando Variação 2 (inicio + fim + 1) // 2...")
    try:
        mergesort_variacao2(v_var2, 0, len(v_var2) - 1)
        print(f"Resultado Variação 2:    {v_var2}")
    except RecursionError as e:
        print(f"Resultado Variação 2:    FALHOU! Erro de recursão: {e}")