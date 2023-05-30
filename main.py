import copy

def FIFO(paginas, quadros, table, seq2):
    faltas = 0
    i = 0

    if (paginas >= quadros):
        
        while (len(seq2) > 0):
            while(i < quadros):  
                
                if(not(seq2[0] in table)):
                   
                    faltas += 1
                    table[i] = seq2[0]
                   
                    seq2.remove(seq2[0])
                    
                    if (len(seq2) == 0):
                        
                        return faltas
                else:
                   
                    seq2.remove(seq2[0])
                   
                    if(len(seq2) == 0):
                       
                        return faltas
                    else:
                        i -= 1
                i += 1
            i = 0
    else:
        faltas = paginas  # custo da inserção das novas paginas na tabela de quadros
    
    return (faltas)


def procura(seq, direcao, table, quadros, historico, seq_original, count_pos):
    
    aux = [0]*quadros
    j = 0
    nada = 0
    indice = 0
    melhor_op = -1
    historico = []
   
    
    # Esta função serve tanto para o OTM qnt para o LRU
    # Sua funcionalidade eh a seguinte, dado um indice (posicao de determinado elemento no vetor)
    # Ela procura com base na direcao (direita ou esquerda) qual eh o elemento que mais demora a
    # aparecer e TEM que retornar a posicao deste elemento na tabela de quadros

    # count = posição do valor a a entrar na tabela
    # valor a entrar = pag a ser inserida na tabela
    # direcao pode assumir 2 valores: 0 -> OTM: analisa a partir do count [count, paginas]
    #                                1 -> LRU: analisa a partir 0 até o count  [0, count]
    if(direcao == 0):  # OTM
        for l in range(0, quadros):
            for i in range(0, len(seq)):
                if(not(table[l] in seq)):
                    
                    nada += 1
                else:
                    aux[l] += 1
        for l in range(0, quadros):
            if(aux[l] == 0):
               
                return(l)
        for i in range(0, len(seq)):
            
            if((seq[i] in table) & (len(seq) > 2)):
               
                if(not(seq[i]in historico)):  
                    melhor_op = seq[i]
                  
                   
                else:
                    
                    nada += 1
                historico.append(seq[i])
                
            if((i == len(seq)-1)):  
                if(melhor_op == -1):
                    if(j == quadros-1):
                        j = 0
                        indice = j
                        melhor_op = table[j]
                      
                    else:
                        indice = j
                        melhor_op = table[j]
                       
                    j += 1
                   
                else:
                    for k in range(0, quadros):
                        if(table[k] == melhor_op):
                            indice = k
               
        return(indice)
    ideal = 0
    if(direcao == 1):
        pag = [-1]*len(seq_original)
        for i in range(count_pos-1, -1, -1):
            #print("Percorrendo o array ao ocntrario ")
            #print("sequencia", seq_original)
            
            if(seq_original[i] in table):  # Se a pagina da sequencia ainda estiver na tabela
                # Se a pagina n tiver sido indexada no pag
                # print("Pagina", seq_original[i],
                #      "esta na tabela, Pode ser retirada")
                if(not(seq_original[i] in pag)):
                    pag[i] = seq_original[i]
                    
            else:
                pass
       
       
        for i in range(0, len(seq_original)):
            if(pag[i] != -1):  # Pega o numero da pagina que esta na posição mais baixa do array
                ideal = pag[i]
                for k in range(0, quadros):
                    if(table[k] == ideal):
                        indice = k
                        #print("A pag a ser retirada da tabela sera", ideal)
                        #print("O indice da pagina sera", indice)
                        return(indice)

        # print("----------------------------------------------------------------")
    return(indice)
# Como o preenchimento dos primeiros valores da tabela de quadros eh igual
# ou seja so há alteração quando há a substituição de paginas, o LRU vai ser preenchido inicialmente
# igual ao OTM, para isso foi criada uma variavel FLAG que vai indicar se o algoritmo do OTM continua a
# preencher a tabela de quadros ou se ele retorna a tabela e a sequencia com os valores iniciais


def OTM(paginas, quadros, table, seq3):
    faltas = 0
    i = 0
    indice = 0
    historico = []
   
    if (paginas >= quadros):
        
        while (-1 in table):
            while (i < quadros):  
                if (not (seq3[0] in table)):
                    # print("movendo:", seq3[0], "para a tabela")
                    faltas += 1
                    
                    table[i] = seq3[0]
                    
                    seq3.remove(seq3[0])
                    
                    if (len(seq3) == 0):
                       
                        i = quadros+1
                else:
                    seq3.remove(seq3[0])
                   
                    if (len(seq3) == 0):
                        
                        i = quadros+1
                    else:
                        i -= 1
                i += 1
            i = 0
        else:
            i = 0
           
            while (len(seq3) > 0):
                i = 0
                while(i < quadros):
                   
                    if(seq3[i] in table):
                       
                        seq3.remove(seq3[i])
                       
                        if (len(seq3) == 0):
                            i = quadros+1
                        else:
                            i -= 1
                    else:
                        
                        indice = procura(
                            seq3, 0, table, quadros, historico, 0, 0)
                        
                        table[indice] = seq3[i]
                        seq3.remove(seq3[i])
                        
                        faltas += 1
                        
                        if (len(seq3) == 0):
                            i = quadros+1
                        else:
                            i -= 1
                    i += 1
                i = 0
    else:
        faltas = paginas  # custo da inserção das novas paginas na tabela de quadros
    
    return (faltas)


def LRU(paginas, quadros, table, seq4, seq_original):
    
    count_pos = 0
    faltas = 0
    i = 0
    historico = []
    if (paginas >= quadros):
        
        while (-1 in table):
            while (i < quadros):  # tipo um for
                if (not (seq4[0] in table)):  # Pagina ainda nao esta na tabela
                   
                    faltas += 1
                    count_pos += 1
                    
                    table[i] = seq4[0]
                    
                    seq4.remove(seq4[0])
                    
                    if (len(seq4) == 0):
                       
                        i = quadros + 1
                else:  # Remove a pagina da fila e nao faz alteracao na tabela
                    seq4.remove(seq4[0])
                    count_pos += 1  # Incrementa o indice para o array da sequencia original
                    
                    if (len(seq4) == 0):
                      
                        i = quadros + 1
                    else:
                        i -= 1
                i += 1
            i = 0
        else:
            
            for i in range(0, quadros):
                historico.append(table[i])
            
            i = 0
           
            while (len(seq4) > 0):
                i = 0
                while (i < quadros):
                    
                    if (seq4[i] in table):
                        
                        seq4.remove(seq4[i])
                        count_pos += 1
                        
                        if (len(seq4) == 0):
                            i = quadros + 1
                        else:
                            i -= 1
                    else:
                        
                        indice = procura(seq4, 1, table, quadros, historico,
                                         seq_original, count_pos)
                        
                        table[indice] = seq4[i]
                        seq4.remove(seq4[i])
                        
                        faltas += 1
                        count_pos += 1
                        
                        if (len(seq4) == 0):
                            i = quadros + 1
                        else:
                            i -= 1
                    i += 1
                i = 0
    else:
        faltas = paginas  # custo da inserção das novas paginas na tabela de quadros
    
    return (faltas)

  
def main():
    texto = []
    with open('subsPagInput.txt') as arq:
        texto = arq.read()

    texto = texto.split()  # quebra os dados de acordo com os espaços
    seq = list(map(int, texto))  # Converte os numeros de string para inteiro
    quadros = seq[0]
    paginas = int(len(seq)-1)  # calcula o numero de paginas
    table = [-1]*quadros

    seq.remove(seq[0])
    seq2 = copy.deepcopy(seq)
    seq3 = copy.deepcopy(seq)
    seq4 = copy.deepcopy(seq)

    faltas_fifo = 0
    faltas_otimo = 0
    faltas_lru = 0

    faltas_fifo = FIFO(paginas, quadros, table, seq2)

    table = [-1] * quadros  # Zera a tabela que foi preenchida pelo FIFO
    faltas_otimo = OTM(paginas, quadros, table, seq3)

    table = [-1] * quadros  # Zera a tabela que foi preenchida pelo OTM
    faltas_lru = LRU(paginas, quadros, table, seq4, seq)

    print("FIFO", faltas_fifo)
    print("OTM", faltas_otimo)
    print("LRU", faltas_lru)


    with open('SubstituicaoOutput.txt', 'w') as arquivo:
        arquivo.write("FIFO " + str(faltas_fifo) + "\n")
        arquivo.write("OTM " + str(faltas_otimo) + "\n")
        arquivo.write("LRU " + str(faltas_lru) + "\n")
        
main()