# Implementação do Algoritmo Merge Sort em Python

O Merge Sort é um algoritmo eficiente, estável e um exemplo clássico da estratégia "dividir para conquistar", e aqui contém sua implementação em Python.

### Como Funciona

O algoritmo opera em duas fases principais, que são aplicadas recursivamente:

**Divisão (Divide):** A lista é dividida continuamente ao meio até que cada sub-lista contenha apenas um elemento. Uma lista com um único elemento é, por definição, considerada ordenada.

**Combinação (Merge):** As sub-listas (agora com um elemento e, portanto, ordenadas) são combinadas (mescladas) duas a duas. A mesclagem é feita de forma ordenada, criando listas maiores que também estão ordenadas. Esse processo continua até que a lista inteira seja reconstruída em sua forma final e ordenada.

### Estrutura do Código

O código fornecido é composto por duas funções principais:

**merge_sort(array):** A função principal que implementa a lógica recursiva de divisão. Ela divide o array ao meio e chama a si mesma para cada metade, até que o caso base (um array de tamanho ≤ 1) seja atingido.

**merge(esquerda, direita):** Uma função auxiliar que realiza a etapa de combinação. Ela recebe duas sub-listas já ordenadas (esquerda e direita) e as mescla em uma única lista, mantendo a ordem.
