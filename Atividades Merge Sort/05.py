# Estrutura básica do nó da lista encadeada
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir_no_final(self, valor):
        """Insere um novo nó no final da lista."""
        novo_no = No(valor)
        if not self.cabeca:
            self.cabeca = novo_no
            return
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no

    def imprimir(self):
        """Imprime os valores da lista."""
        elementos = []
        atual = self.cabeca
        while atual:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        print(" -> ".join(elementos))

    # --------------------------------------------------------------------
    # ALGORITMO MERGE SORT PARA LISTA ENCADEADA
    # --------------------------------------------------------------------

    def sort(self):
        """Ponto de entrada público para iniciar a ordenação."""
        self.cabeca = self._merge_sort_recursivo(self.cabeca)

    def _merge_sort_recursivo(self, cabeca_atual):
        """
        Função principal que aplica a divisão e conquista.
        """
        # --- CASO BASE ---
        # Se a lista está vazia ou tem apenas um elemento, ela já está ordenada.
        if not cabeca_atual or not cabeca_atual.proximo:
            return cabeca_atual

        # --- 1. ETAPA DE DIVISÃO ---
        # Encontra o meio e divide a lista em duas metades.
        meio = self._get_meio(cabeca_atual)
        proximo_do_meio = meio.proximo
        
        # Corta a lista ao meio
        meio.proximo = None
        
        cabeca_esquerda = cabeca_atual
        cabeca_direita = proximo_do_meio

        # --- 2. ETAPA DE CONQUISTA ---
        # Chama recursivamente para ordenar cada metade.
        esquerda_ordenada = self._merge_sort_recursivo(cabeca_esquerda)
        direita_ordenada = self._merge_sort_recursivo(cabeca_direita)

        # --- 3. ETAPA DE COMBINAÇÃO ---
        # Combina (mescla) as duas metades ordenadas.
        return self._merge_listas(esquerda_ordenada, direita_ordenada)

    def _get_meio(self, cabeca_atual):
        """
        Encontra o nó do meio da lista usando a técnica do ponteiro lento e rápido.
        """
        if not cabeca_atual:
            return cabeca_atual

        lento = cabeca_atual
        rapido = cabeca_atual

        # Avança 'rapido' dois passos e 'lento' um passo.
        # Quando 'rapido' chegar ao fim, 'lento' estará no meio.
        while rapido.proximo and rapido.proximo.proximo:
            lento = lento.proximo
            rapido = rapido.proximo.proximo
            
        return lento

    def _merge_listas(self, l1, l2):
        """
        Mescla duas listas ordenadas (l1 e l2) em uma única lista ordenada,
        manipulando apenas os ponteiros.
        """
        # Cria um nó temporário para servir como início da lista mesclada.
        no_fantasma = No(0)
        ponteiro_atual = no_fantasma

        # Percorre as duas listas, adicionando o menor nó à lista mesclada.
        while l1 and l2:
            if l1.valor < l2.valor:
                ponteiro_atual.proximo = l1
                l1 = l1.proximo
            else:
                ponteiro_atual.proximo = l2
                l2 = l2.proximo
            ponteiro_atual = ponteiro_atual.proximo

        # Se uma das listas ainda tiver elementos, anexa o restante.
        if l1:
            ponteiro_atual.proximo = l1
        elif l2:
            ponteiro_atual.proximo = l2

        # A cabeça da lista mesclada é o próximo do nó fantasma.
        return no_fantasma.proximo

# --- Exemplo de Uso ---

lista = ListaEncadeada()
valores = [38, 27, 43, 3, 9, 82, 10]
for v in valores:
    lista.inserir_no_final(v)

print("Lista Original:")
lista.imprimir()

# Chama o método de ordenação
lista.sort()

print("\nLista Ordenada:")
lista.imprimir()