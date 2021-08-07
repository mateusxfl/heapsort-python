# Heapifica a subárvore com raiz no índice posicaoRaiz.
def heapify(numeros, totalDeNumerosNaPilha, posicaoRaiz):
    
    posicaoRaizAuxiliar = posicaoRaiz # Inicializa o número contido na posicaoRaiz como raiz da subárvore a ser heapificada.

    # Define a posição do filho esquerdo (e) e direito (d), tendo em vista que estamos representando a árvore como um array.
    e = 2 * posicaoRaiz + 1
    d = 2 * posicaoRaiz + 2 
 
    # Verifica se o filho esquerdo existe e é maior que a raiz.
    if e < totalDeNumerosNaPilha and numeros[posicaoRaizAuxiliar] < numeros[e]:
        posicaoRaizAuxiliar = e
 
    # Verifica se o filho direito existe e é maior que a raiz.
    if d < totalDeNumerosNaPilha and numeros[posicaoRaizAuxiliar] < numeros[d]:
        posicaoRaizAuxiliar = d
 
    # Mude a raiz, se necessário ( entra aqui caso tenha entrado em uma das duas condições anteriores ).
    if posicaoRaizAuxiliar != posicaoRaiz:
        numeros[posicaoRaiz], numeros[posicaoRaizAuxiliar] = numeros[posicaoRaizAuxiliar], numeros[posicaoRaiz]  # Faz a troca da raiz pelo maior de seus filhos.
 
        # Empilhe a raiz.
        heapify(numeros, totalDeNumerosNaPilha, posicaoRaizAuxiliar)

numeros = list() # Array que irei preencher com os números a serem ordenados.

entrada = open('entrada.txt','r') # Lê uma entrada TXT que contém o total de números na linha 1, e nas demais linhas: os números a serem ordenados.

totalDeNumerosNaPilha = int(entrada.readlines(1)[0]) # Total de números a serem ordenados.

for linha in entrada: # Preenche o vetor de números a serem ordenados.
    numeros.append(int(linha))

entrada.close()

# print(numeros) # Números a serem ordenados -----------------------------------

# Ordena os números. ~> Constrói um maxheap, executando heapify apenas para os nós que possuem filhos ( começando pelo mais distante da raiz ).
for i in range(totalDeNumerosNaPilha//2 - 1, -1, -1):
    heapify(numeros, totalDeNumerosNaPilha, i)

# Um por um extraia um elemento da pilha
for i in range(totalDeNumerosNaPilha-1, 0, -1):
    numeros[i], numeros[0] = numeros[0], numeros[i]  # Faz a troca
    heapify(numeros, i, 0)

# print(numeros) # Números já ordenados ---------------------------------------- 

arquivo = open("saida.txt", "w") # Escreve a saída (resposta).

linhas = list()

linhas.append(str(totalDeNumerosNaPilha) + '\n') # Adiciona o total de números na primeira linha, assim como é solicitado o retorno.
print(str(totalDeNumerosNaPilha))

for i in range(totalDeNumerosNaPilha): # Adiciona os demais números ordenados nas demais linhas.
    linhas.append(str(numeros[i]) + '\n')
    print(str(numeros[i]))

arquivo.writelines(linhas) 

arquivo.close()