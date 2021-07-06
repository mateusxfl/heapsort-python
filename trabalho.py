
# Programa Python para implementação de heap Sort
 
# Para heapificar a subárvore enraizada no índice i.
# n é o total de números da pilha

def heapify(numeros, total_de_numeros, i):
    
    maior = i # Inicializa o nó pai como raiz.

    # Define a posição do filho esquerdo (e) e direito (d), tendo em vista que estamos representando a árvore como um array.
    e = 2 * i + 1
    d = 2 * i + 2 
 
    # Verifica se o filho esquerdo da raiz existe e é maior que a raiz.
    if e < total_de_numeros and numeros[maior] < numeros[e]:
        maior = e
 
    # Verifica se o filho direito da raiz existe e é maior que a raiz.
    if d < total_de_numeros and numeros[maior] < numeros[d]:
        maior = d
 
    # Mude a raiz, se necessário ( entra aqui caso tenha entrado em uma das condições anteriores ).
    if maior != i:
        numeros[i], numeros[maior] = numeros[maior], numeros[i]  # Faz a troca.
 
        # Empilhe a raiz.
        heapify(numeros, total_de_numeros, maior)
 
# Função principal que chama heapify
def heapSort(numeros, total_de_numeros):

    # Constrói um maxheap, executando heapify apenas para os nós que possuem filhos ( começando pelo mais distante da raiz ).
    for i in range(total_de_numeros//2 - 1, -1, -1):
        heapify(numeros, total_de_numeros, i)
 
    # Um por um extraia um elemento da pilha
    for i in range(total_de_numeros-1, 0, -1):
        numeros[i], numeros[0] = numeros[0], numeros[i]  # Faz a troca
        heapify(numeros, i, 0)
 
 
# Main

numeros = list() # Array que irei preencher com os números a serem ordenados.

entrada = open('entrada.txt','r') # Lê uma entrada TXT que contém o total de números na linha 1, e nas demais: os números a serem ordenados.

total_de_numeros = int(entrada.readlines(1)[0]) # Total de números a serem ordenados.

for linha in entrada: # Preenche o vetor de números a serem ordenados.
    numeros.append(int(linha))

entrada.close()

heapSort(numeros, total_de_numeros) # Ordena os números.

arquivo = open("saida.txt", "w") # Escreve a saída (resposta).

linhas = list()

linhas.append(str(total_de_numeros) + '\n') # Adiciona o total de números na primeira linha, assim como é solicitado o retorno.

for i in range(total_de_numeros): # Adiciona os demais números ordenados nas demais linhas.
    linhas.append(str(numeros[i]) + '\n')

arquivo.writelines(linhas) 

arquivo.close()

for i in range(total_de_numeros//2 - 1, -1, -1):
    print(i)