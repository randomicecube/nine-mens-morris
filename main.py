# Diogo Gaspar - 99207

################################################################################
# 2.1.1 - TAD posicao
################################################################################
# Representacao do TAD posicao: R[c, l] = c + l
# Assinatura do TAD posicao:
# cria_posicao: str x str -> posicao
# cria_copia_posicao: posicao -> posicao
# obter_pos_c: posicao -> str
# obter_pos_l: posicao -> str
# eh_posicao: universal -> booleano
# posicoes_iguais: posicao x posicao -> booleano
# posicao_para_str: posicao -> str

def cria_posicao(c, l):
    #cria_posicao: str x str -> posicao
    '''cria_posicao(c,l) recebe duas cadeias de carateres correspondentes a
    coluna c e a linha l de uma posicao e devolve a posicao correspondente. O
    construtor verifica a validade dos seus argumentos, gerando um ValueError
    com a mensagem 'cria_posicao: argumentos invalidos' caso os seus argumentos
    nao sejam validos.'''
    if type(c) != str or type(l) != str \
       or c not in ('a', 'b', 'c') or l not in ('1', '2', '3'):
        raise ValueError ('cria_posicao: argumentos invalidos')
    return c + l

def cria_copia_posicao(p):
    #cria_copia_posicao: posicao -> posicao
    '''cria_copia_posicao(p) recebe uma posicao e devolve uma copia nova da
    posicao.'''
    return p[0] + p[1] if eh_posicao(p) else False

def obter_pos_c(p):
    #obter_pos_c: posicao -> str
    '''obter_pos_c(p) devolve a componente coluna c da posicao p.'''
    return p[0]

def obter_pos_l(p):
    #obter_pos_l: posicao -> str
    '''obter_pos_l(p) devolve a componente linha l da posicao p.'''
    return p[1]

def eh_posicao(arg):
    #eh_posicao: universal -> booleano
    '''eh_posicao(arg) devolve true caso o seu argumento seja um TAD posicao e
    False caso contrario.'''
    return type(arg) == str and len(arg) == 2 \
           and obter_pos_c(arg) in ('a', 'b', 'c') \
           and obter_pos_l(arg) in ('1', '2', '3')


def posicoes_iguais(p1, p2):
    #posicoes_iguais: posicao x posicao -> booleano
    '''posicoes_iguais(p1, p2) devolve True apenas se p1 e p2 sao posicoes e sao
    iguais.'''
    return eh_posicao(p1) and eh_posicao(p2) \
           and obter_pos_c(p1) == obter_pos_c(p2) \
           and obter_pos_l(p1) == obter_pos_l(p2)

def posicao_para_str(p):
    #posicao_para_str: posicao -> str
    '''posicao_para_str(p) devolve a cadeia de carateres 'cl' que representa o
    seu argumento, sendo os valores c e l as componentes coluna e linha de p.'''
    return obter_pos_c(p) + obter_pos_l(p)

def obter_posicoes_adjacentes(p):
    #obter_posicoes_adjacentes: posicao -> tuplo de posicoes
    '''obter_posicoes_adjacentes(p) devolve um tuplo com as posicoes adjacentes
    a posicao p de acordo com a ordem de leitura do tabuleiro.'''
    adj_list = {
        posicao_para_str(cria_posicao('a', '1')): \
        (cria_posicao('b', '1'),cria_posicao('a', '2'),cria_posicao('b', '2')),\
        posicao_para_str(cria_posicao('b', '1')): \
        (cria_posicao('a', '1'),cria_posicao('c', '1'),cria_posicao('b', '2')),\
        posicao_para_str(cria_posicao('c', '1')): \
        (cria_posicao('b', '1'),cria_posicao('b', '2'),cria_posicao('c', '2')),\
        posicao_para_str(cria_posicao('a', '2')): \
        (cria_posicao('a', '1'),cria_posicao('b', '2'),cria_posicao('a', '3')),\
        posicao_para_str(cria_posicao('b', '2')): \
        (cria_posicao('a', '1'),cria_posicao('b', '1'),cria_posicao('c', '1'), \
         cria_posicao('a', '2'),cria_posicao('c', '2'),cria_posicao('a', '3'), \
         cria_posicao('b', '3'),cria_posicao('c', '3')), \
        posicao_para_str(cria_posicao('c', '2')): \
        (cria_posicao('c', '1'),cria_posicao('b', '2'),cria_posicao('c', '3')),\
        posicao_para_str(cria_posicao('a', '3')): \
        (cria_posicao('a', '2'),cria_posicao('b', '2'),cria_posicao('b', '3')),\
        posicao_para_str(cria_posicao('b', '3')): \
        (cria_posicao('b', '2'),cria_posicao('a', '3'),cria_posicao('c', '3')),\
        posicao_para_str(cria_posicao('c', '3')): \
        (cria_posicao('b', '2'),cria_posicao('c', '2'),cria_posicao('b', '3'))}
    return adj_list[posicao_para_str(p)]

################################################################################
# 2.1.2 - TAD peca
################################################################################
# Representacao do TAD peca: R[s] = [s]
# Assinatura do TAD peca:
# cria_peca: str -> peca
# cria_copia_peca: peca -> peca
# eh_peca: universal -> booleano
# pecas_iguais: peca x peca -> booleano
# peca_para_str: peca -> str

def cria_peca(s):
    #cria_peca: str -> peca
    '''cria_peca(s) recebe uma cadeia de carateres correspondente ao identifica-
    dor de um dos dois jogadores ('X' ou 'O') ou a uma peca livre (' ') e devol-
    ve a peca correspondente. O construtor verifica a validade dos seus argumen-
    tos, gerando um ValueError com a mensagem 'cria_peca: argumento invalido'
    caso o seu argumento nao seja valido.'''
    if type(s) != str or s not in ('X', 'O', ' '):
        raise ValueError ('cria_peca: argumento invalido')
    return [s]

def cria_copia_peca(j):
    #cria_copia_peca: peca -> peca
    '''cria_copia_peca(j) recebe uma peca e devolve uma copia nova da peca.'''
    return [j[0]] if eh_peca(j) else False

def eh_peca(arg):
    #eh_peca: universal -> booleano
    '''eh_peca(arg) devolve true caso o seu argumento seja um TAD peca e False
    caso contrario.'''
    return type(arg) == list and len(arg) == 1 and arg[0] in ('X', 'O', ' ')

def pecas_iguais(p1, p2):
    #pecas_iguais: peca x peca -> booleano
    '''pecas_iguais(j1, j2) devolve True apenas se p1 e p2 sao pecas e sao
    iguais.'''
    return eh_peca(p1) and eh_peca(p2) and p1 == p2

def peca_para_str(j):
    #peca_para_str: peca -> str
    '''peca_para_str(j) devolve a cadeia de carateres que representa o jogador
    dono da peca, isto e, '[X]', '[O]' ou '[]'.'''
    return '[X]' if pecas_iguais(j, ['X']) \
           else '[O]' if pecas_iguais(j, ['O']) else '[ ]'

def peca_para_inteiro(j):
    #peca_para_inteiro: peca -> N
    '''peca_para_inteiro(j) devolve um inteiro valor 1, -1 ou 0, dependendo se a
    peca e do jogador 'X', 'O' ou livre, respetivamente.'''
    return 1 if peca_para_str(j) == '[X]' else \
           (-1 if peca_para_str(j) == '[O]' else 0)

################################################################################
# 2.1.3 - TAD tabuleiro
################################################################################
# Representacao interna do TAD tabuleiro: Lista com 9 sublistas, contendo cada 
# uma delas um par posicao (em representacao externa) - peca.
# R[tab] = [[posicao_para_str(pos), peca], [posicao_para_str(pos), peca], \
#           [posicao_para_str(pos), peca], [posicao_para_str(pos), peca], \
#           [posicao_para_str(pos), peca], [posicao_para_str(pos), peca], \
#           [posicao_para_str(pos), peca], [posicao_para_str(pos), peca], \
#           [posicao_para_str(pos), peca]]
# Assinatura do TAD tabuleiro:
# cria_tabuleiro: {} -> tabuleiro
# cria_copia_tabuleiro: tabuleiro -> tabuleiro
# obter_peca: tabuleiro x posicao -> peca
# obter_vetor: tabuleiro x str -> tuplo de pecas
# coloca_peca: tabuleiro x peca x posicao -> tabuleiro
# remove_peca: tabuleiro x posicao -> tabuleiro
# move_peca: tabuleiro x posicao x posicao -> tabuleiro
# eh_tabuleiro: universal -> booleano
# eh_posicao_livre: tabuleiro x posicao -> booleano
# tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
# tabuleiro_para_str: tabuleiro -> str
# tuplo_para_tabuleiro: tuplo -> tabuleiro

def cria_tabuleiro():
    #cria_tabuleiro: {} -> tabuleiro
    '''cria_tabuleiro() devolve um tabuleiro de jogo do moinho de 3x3 sem posi-
    coes ocupadas por pecas de jogador.'''
    return [[posicao_para_str(i), cria_peca(' ')] for i in positions('t')]

def cria_copia_tabuleiro(t):
    #cria_copia_tabuleiro: tabuleiro -> tabuleiro
    '''cria_copia_tabuleiro(t) recebe um tabuleiro e devolve uma copia nova do
    tabuleiro.'''
    return [[pos, pec] for pos, pec in t] if eh_tabuleiro(t) else False

def obter_peca(t, p):
    #obter_peca: tabuleiro x posicao -> peca
    '''obter_peca(t, p) devolve a peca na posicao p do tabuleiro. Se a posicao
    nao estiver ocupada, devolve uma peca livre.'''
    return next(i[1] for i in t if posicoes_iguais(str_para_pos(i[0]), p))

def obter_vetor(t, s):
    #obter_vetor: tabuleiro x str -> tuplo de pecas
    '''obter_vetor(t, s) devolve todas as pecas da linha ou coluna especificada
    pelo seu argumento.'''
    return tuple(obter_peca(t, str_para_pos(i[0])) for i in t if s in i[0])

def coloca_peca(t, j, p):
    #coloca_peca: tabuleiro x peca x posicao -> tabuleiro
    '''coloca_peca(t, j, p) modifica destrutivamente o tabuleiro t colocando a
    peca j na posicao p, e devolve o proprio tabuleiro.'''
    if (eh_posicao_livre(t, p)):
        for i in t:
            if posicoes_iguais(p, str_para_pos(i[0])):
                i[1] = j
                break
    return t

def remove_peca(t, p):
    #remove_peca: tabuleiro x posicao -> tabuleiro
    '''remove_peca(t, p) modifica destrutivamente o tabuleiro t removendo a peca
    da posicao p, e devolve o proprio tabuleiro.'''
    if not eh_posicao_livre(t, p):
        for i in t:
            if posicoes_iguais(p, str_para_pos(i[0])):
                i[1] = cria_peca(' ')
                break
    return t

def move_peca(t, p1, p2):
    #move_peca: tabuleiro x posicao x posicao -> tabuleiro
    '''move_peca(t, p1, p2) modifica destrutivamente o tabuleiro t movendo a
    peca que se encontra na posicao p1 para a posicao p2, e devolve o proprio
    tabuleiro.'''
    peca1 = obter_peca(t, p1)
    if any(posicoes_iguais(p1, k) for k in \
           obter_posicoes_jogador(t, peca1)):
        if not posicoes_iguais(p1, p2):
            remove_peca(t, p1), coloca_peca(t, peca1, p2)
    return t

def eh_tabuleiro(arg):
    #eh_tabuleiro: universal -> booleano
    '''eh_tabuleiro(arg) devolve True caso o seu argumento seja um TAD tabuleiro
    e False caso contrario. Um tabuleiro valido pode ter um maximo de 3 pecas de
    cada jogador, nao pode conter mais de 1 peca a mais de um jogador que do
    contrario, e apenas pode haver um ganhador em simultaneo.'''
    return type(arg) == list and len(arg) == 9 and \
           all(type(i) == list for i in arg) and \
           all(len(i) == 2 for i in arg) and \
           all([eh_posicao(str_para_pos(i[0])),eh_peca(i[1])] for i in arg) and\
           len(obter_posicoes_jogador(arg, cria_peca('X'))) <= 3 and \
           len(obter_posicoes_jogador(arg, cria_peca('O'))) <= 3 and \
           abs(len(obter_posicoes_jogador(arg, cria_peca('X'))) - \
               len(obter_posicoes_jogador(arg, cria_peca('O')))) <= 1 and \
           ganhador_counter(arg)

def eh_posicao_livre(t, p):
    #eh_posicao_livre: tabuleiro x posicao -> booleano
    '''eh_posicao_livre(t, p) devolve True apenas no caso da posicao p do tabu-
    leiro corresponder a uma posicao livre.'''
    return eh_posicao(p) and peca_para_inteiro(obter_peca(t, p)) == 0

def tabuleiros_iguais(t1, t2):
    #tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
    '''tabuleiros_iguais(t1, t2) devolve True apenas se t1 e t2 sao tabuleiros e
    sao iguais.'''
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and \
           all(pecas_iguais(t1[i][1], t2[i][1]) for i in range(len(t1)))

def tabuleiro_para_str(t):
    #tabuleiro_para_str: tabuleiro -> str
    '''tabuleiro_para_str(t) devolve a cadeia de carateres que representa o ta-
    buleiro como requerido no enunciado.'''
    return '   a   b   c\n1 ' + \
           peca_para_str(obter_peca(t, cria_posicao('a', '1'))) + \
           '-' + peca_para_str(obter_peca(t, cria_posicao('b', '1'))) + '-' + \
           peca_para_str(obter_peca(t, cria_posicao('c', '1'))) + '\n   ' + \
           '| \ | / |\n2 ' + \
           peca_para_str(obter_peca(t, cria_posicao('a', '2'))) + \
           '-' + peca_para_str(obter_peca(t, cria_posicao('b', '2'))) + '-' + \
           peca_para_str(obter_peca(t, cria_posicao('c', '2'))) + '\n   ' + \
           '| / | \ |\n3 ' + \
           peca_para_str(obter_peca(t, cria_posicao('a', '3'))) + \
           '-' + peca_para_str(obter_peca(t, cria_posicao('b', '3'))) + '-' + \
           peca_para_str(obter_peca(t, cria_posicao('c', '3')))

def tuplo_para_tabuleiro(t):
    #tuplo_para_tabuleiro: tuplo -> tabuleiro
    '''tuplo_para_tabuleiro(t) devolve o tabuleiro que e representado pelo tuplo
    t com 3 tuplos, cada um deles contendo 3 valores inteiros iguais a 1, -1 ou
    0, tal como no primeiro projeto.'''
    tab, t_aux = cria_tabuleiro(), [ii for i in t for ii in i]
    for n in range(len(t_aux)):
        coloca_peca(tab, inteiro_para_peca(t_aux[n]), str_para_pos(tab[n][0]))
    return tab

def obter_ganhador(t):
    #obter_ganhador: tabuleiro -> peca
    '''obter_ganhador(t) devolve uma peca do jogador que tenha as suas 3 pecas
    em linha na vertical ou na horizontal no tabuleiro. Se nao existir nenhum
    ganhador, devolve uma peca livre.'''
    void = cria_peca(' ')
    for i in ('a', 'b', 'c', '1', '2', '3'):
        vetor = obter_vetor(t, i)
        if all(pecas_iguais(peca, vetor[0]) for peca in vetor) \
           and not pecas_iguais(vetor[0], void):
            return vetor[0]
    return void

def obter_posicoes_livres(t):
    #obter_posicoes_livres: tabuleiro -> tuplo de posicoes
    '''obter_posicoes_livres(t) devolve um tuplo com as posicoes nao ocupadas
    pelas pecas de qualquer um dos dois jogadores na ordem de leitura do tabu-
    leiro.'''
    return compativeis(t, positions('t'))

def obter_posicoes_jogador(t, j):
    #obter_posicoes_jogador: tabuleiro x peca -> tuplo de posicoes
    '''obter_posicoes_jogador(t, j) devolve um tuplo com as posicoes ocupadas 
    pelas pecas j de um dos dois jogadores na ordem de leitura do tabuleiro.'''
    return tuple(i for i in positions('t') if pecas_iguais(obter_peca(t, i), j))

################################################################################
# 2.2.1 - obter_movimento_manual
################################################################################

def obter_movimento_manual(t, j):
    #obter_movimento_manual: tabuleiro x peca -> tuplo de posicoes
    '''obter_movimento_manual(t, j) e uma funcao auxiliar que recebe um tabulei-
    ro e uma peca de um jogador e devolve um tuplo com uma ou duas posicoes, re-
    presentando uma posicao ou movimento introduzido manualmente pelo jogador.
    Em caso de colocacao, o tuplo contem a posicao de destino da peca; em caso 
    de movimento, contem a posicao de origem e a de destino. O jogador pode pas-
    sar a jogada, fazendo um movimento com posicao de origem e destino iguais, 
    caso todos movimentos estejam bloqueados. Deve gerar um erro com a mensagem
    'obter_movimento_manual: escolha invalida' caso o input nao corresponder a 
    colocacao ou movimento valido. Deve apresentar a mensagem 'Turno do jogador.
    Escolha uma posicao: ' ou 'Turno do jogador. Escolha um movimento: ' caso se
    trate de colocacao ou movimento, respetivamente.'''
    if col_mov(t, j):
        m = str(input('Turno do jogador. Escolha uma posicao: '))
        if type(m) == str and len(m) == 2 and \
           m[0] in ('a', 'b', 'c') and m[1] in ('1', '2', '3'):
            m1 = cria_posicao(m[0], m[1])
        else:
            raise ValueError ('obter_movimento_manual: escolha invalida')
        if not eh_posicao_livre(t, m1):
            raise ValueError ('obter_movimento_manual: escolha invalida')
        return (m1, )
    else:
        m = str(input('Turno do jogador. Escolha um movimento: '))
        if type(m) == str and len(m) == 4 and \
           m[0] in ('a', 'b', 'c') and m[1] in ('1', '2', '3') and \
           m[2] in ('a', 'b', 'c') and m[3] in ('1', '2', '3'):
            m1, m2 = cria_posicao(m[0], m[1]), cria_posicao(m[2], m[3])
            adj = obter_posicoes_adjacentes(m1)
        else:
            raise ValueError ('obter_movimento_manual: escolha invalida')
        if not pecas_iguais(obter_peca(t, m1), j) or \
           peca_para_inteiro(obter_peca(t, m2)) == -peca_para_inteiro(j) or \
           (not posicoes_iguais(m1, m2) if \
            all(not eh_posicao_livre(t, pos) for pos in adj) else \
            (not any(posicoes_iguais(m2, k) for k in adj) or \
             not eh_posicao_livre(t, m2))):           
            raise ValueError ('obter_movimento_manual: escolha invalida')
        return (m1, m2)

################################################################################
# 2.2.2 - obter_movimento_auto
################################################################################

def obter_movimento_auto(t, j, dif):
    #obter_movimento_auto: tabuleiro x peca x str -> tuplo de posicoes
    '''obter_movimento_auto(t, j, dif) e uma funcao auxiliar que recebe um tabu-
    leiro, uma peca de jogador e uma cadeia de carateres (representando a difi-
    culdade do jogo), devolvendo um tuplo com uma ou duas posicoes, que repre-
    sentam a colocacao ou movimento, respetivamente, da peca do jogador. A 
    estrategia de jogo seguida pode ser 'facil', 'normal', ou 'dificil'. A fase
    de colocacao segue a estrategia de jogo descrita no ponto 1.3.1 do enunciado
    enquanto que o movimento pode ser:
    1) a peca a movimentar e sempre a que ocupa a primeira posicao em ordem de 
    leitura do tabuleiro que tenha uma adjacente livre - a de destino e a pri-
    meira adjacente livre.
    2) seguir o algoritmo minimax, com variados niveis de profundidade.
    A estrategia 'facil' segue 1); a 'normal' segue 2) caso seja possivel chegar
    a uma vitoria com profundidade = 1, caso contrario segue 1); a 'dificil' 
    segue 2) com profundidade = 5.'''
    if col_mov(t, j):
        return col(t, j)
    f = facil(t, j)
    if dif == 'facil':
        return f
    elif dif ==  'normal':
        m1 = minimax(t, j, 1, ())
        return (m1[1][0], m1[1][1] ) if not \
               pecas_iguais(cria_peca(' '), inteiro_para_peca(m1[0])) else f
    m5 = minimax(t, j, 5, ())
    return (m5[1][0], m5[1][1])

################################################################################
# 2.2.3 - moinho
################################################################################

def moinho(j, dif):
    #moinho: str x str -> str
    '''moinho(t, j) e a funcao principal, permite jogar um jogo completo do jogo
    do moinho de um jogador contra o computador. Recebe duas cadeias de carate-
    res, a primeira correspondendo a representacao externa da peca com que dese-
    ja jogar o jogador humano, a segunda a dificuldade do jogo. Devolve uma ca-
    deia de carateres correspondente a representacao externa da peca do jogador
    que ganhou. Se algum argumento for invalido, deve ser gerado um erro com a
    mensagem 'moinho: argumentos invalidos'. Deve apresentar a mensagem 'Turno 
    do computador (<nivel>):', em que <nivel> corresponde a cadeia de carateres
    passada como segundo argumento, quando for o turno do computador.'''
    if dif not in ('facil','normal','dificil') or not eh_peca(str_para_peca(j)):
        raise ValueError ('moinho: argumentos invalidos')
    t = cria_tabuleiro()
    print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade ' + dif + \
          '.\n' + tabuleiro_para_str(t))
    x, o, void = cria_peca('X'), cria_peca('O'), cria_peca(' ')
    j, j_aux = str_para_peca(j), x
    ganha = void
    jog = x if pecas_iguais(j, x) else o
    while pecas_iguais(ganha, void):
        atual = col_mov(t, j_aux)
        if pecas_iguais(j_aux, jog):
            mov = obter_movimento_manual(t, j_aux)
        else:
            mov = obter_movimento_auto(t, j_aux, dif)
            print('Turno do computador (' + str(dif) + '):')
        print(tabuleiro_para_str(coloca_peca(t, j_aux, mov[0]))) if atual \
        else print(tabuleiro_para_str(move_peca(t, mov[0], mov[1])))
        j_aux = o if pecas_iguais(j_aux, x) else x
        ganha = obter_ganhador(t)
    return peca_para_str(ganha)

################################################################################
# Funcoes auxiliares utilizadas em obter_movimento_manual e obter_movimento_auto
################################################################################

def col_mov(t, j):
    #col_mov: tabuleiro x peca -> booleano
    '''col_mov(t, j) devolve False se a acao a decorrer for um movimento, True 
    se for uma colocacao.'''
    return len(obter_posicoes_livres(t)) > 3 and \
               len(obter_posicoes_jogador(t, j)) < 3
    
def col(t, j):
    #col: tabuleiro x pesa -> posicao
    '''col(t, j) devolve a posicao correspondente a colocacao que mais faz sen-
    tido segundo a estrategia descrita na seccao 1.3.1 do enunciado, em relacao
    a peca j.'''
    vit_bloq, centro = vitoria_bloqueio(t, j), cria_posicao('b', '2')
    if len(vit_bloq) != 0:
        return vit_bloq
    elif eh_posicao_livre(t, centro):
        return (centro, )
    canto_sim, lateral_sim = compativeis(t, positions('c')), \
        compativeis(t, positions('l'))
    return (canto_sim[0], ) if canto_sim != () else (lateral_sim[0], )

def vitoria_bloqueio(t, j):
    #vitoria_bloqueio: tabuleiro x peca -> tuplo
    '''vitoria_bloqueio(t, j) recebe um tabuleiro e peca validos e devolve um
    tuplo contendo a posicao correspondente a aplicacao dos criterios vitoria
    e bloqueio do enunciado (por essa ordem), ou um tuplo vazio caso nenhum se 
    possa aplicar.'''
    empty_opponent = ()
    for i in ('1', '2', '3', 'a', 'b', 'c'):
        counter = counter_player = counter_opponent = 0
        empty = ()
        for k in obter_vetor(t, i):
            if pecas_iguais(k, j):
                counter_player += 1
            elif peca_para_inteiro(k) == -peca_para_inteiro(j) != 0:
                counter_opponent += 1
            else:
                if ord(i) >= 97:
                    #ord(i) devolve um valor inteiro associado a um caracter
                    empty += (cria_posicao(i, str(counter + 1)), )
                else:
                    empty += (cria_posicao(str(chr(counter + 97)), i), )
            counter += 1
        if counter_player == 2 and counter_opponent == 0:
            return empty
        if counter_opponent == 2 and counter_player == 0:
            empty_opponent += (empty[0], )
    return (empty_opponent[0], ) if len(empty_opponent) != 0 else ()    

def facil(t, j):
    #facil: tabuleiro x peca -> tuplo
    '''facil(t, j) recebe um tabuleiro valido e uma peca e devolve a sequencia
    de movimentos correspondente a aplicacao da estrategia "facil" do enunciado.
    '''
    return next((i, n) for i in obter_posicoes_jogador(t, j) \
                for n in obter_posicoes_adjacentes(i) if eh_posicao_livre(t, n))

def minimax(t, j, prof, seq_mov):
    #minimax: tabuleiro x peca x N x tuplo -> tuplo
    '''minimax(t, j, prof, seq_mov) recebe um tabuleiro valido, uma peca, um in-
    teiro (correspondendo a profundidade da recursao) e uma sequencia de movi-
    mentos inicial e devolve a aplicacao do algoritmo minimax ao tabuleiro e pe-
    ca em questao.'''
    ganhador = obter_ganhador(t)
    if not pecas_iguais(ganhador, cria_peca(' ')) or prof == 0:
        return (peca_para_inteiro(ganhador), seq_mov)
    else:
        inteiro, melh_seq_mov = peca_para_inteiro(j), ()
        melh_res, opp = -inteiro, inteiro_para_peca(-inteiro)
        for i in obter_posicoes_jogador(t, j):
            for n in obter_posicoes_adjacentes(i):
                if eh_posicao_livre(t, n):
                    novo_tab = move_peca(cria_copia_tabuleiro(t), i, n)
                    (novo_res, nova_seq_mov) = minimax\
                        (novo_tab, opp, prof - 1, seq_mov + (i, n))
                    if melh_seq_mov == () or \
                       (inteiro == 1 and novo_res > melh_res) or \
                       (inteiro == -1 and novo_res < melh_res):
                        melh_res, melh_seq_mov = novo_res, nova_seq_mov
            if melh_res == inteiro:
                break
        return (melh_res, melh_seq_mov)    
    
################################################################################
# Funcoes auxiliares utilizadas em varias partes do programa
################################################################################

def inteiro_para_peca(j):
    #inteiro_para_peca: N -> peca
    '''inteiro_para_peca(j) recebe um inteiro, -1, 0 ou 1, e devolve a peca cor-
    respondente. Caso o inteiro nao seja um desses, devolve False.'''
    return cria_peca('X') if j == 1 else cria_peca('O') if j == -1 else \
           cria_peca(' ') if j == 0 else False

def str_para_pos(str_pos):
    #str_para_pos: str -> posicao
    '''str_para_pos(str_pos) recebe uma posicao na sua representacao externa e 
    devolve-a sob a sua representacao interna.'''
    return cria_posicao(str_pos[0], str_pos[1])

def str_para_peca(str_pec):
    #str_para_peca: str -> peca
    '''str_para_peca(str_pec) recebe uma peca na sua representacao externa e 
    devolve-a sob a sua representacao interna.'''    
    return cria_peca(str_pec[1])

def compativeis(t, tup):
    #compativeis: tabuleiro x tuplo -> tuplo
    '''compativeis(t, tup) recebe um tabuleiro e um tuplo de posicoes e devolve
    todos os elementos desse tuplo que forem posicoes livres no tabuleiro.'''
    return tuple(i for i in tup if eh_posicao_livre(t, i))

def positions(string):
    #positions: str -> tuplo
    '''positions(string) recebe uma string e devolve um tuplo contendo as posi-
    coes de um TAD tabuleiro - todas, cantos ou laterais, dependendo do argumen-
    to introduzido.'''
    t = (cria_posicao('a', '1'), cria_posicao('b', '1'), \
         cria_posicao('c', '1'), cria_posicao('a', '2'), \
         cria_posicao('b', '2'), cria_posicao('c', '2'), \
         cria_posicao('a', '3'), cria_posicao('b', '3'), \
         cria_posicao('c', '3'))
    return t if string == 't' else \
           tuple(t[i] for i in range(len(t)) if (i%2==0 and i!=4)) \
           if string == 'c' else tuple(t[i] for i in range(len(t)) if (i%2!=0))

def ganhador_counter(t):
    #ganhador_counter: tabuleiro -> booleano
    '''ganhador_counter(t) recebe um tabuleiro valido e devolve True se houver 1
    ou menos ganhadores, False caso contrario.'''
    counter = 0
    for i in ('a', 'b', 'c', '1', '2', '3'):
        vetor = obter_vetor(t, i)
        if all(pecas_iguais(peca, vetor[0]) for peca in vetor) \
           and not pecas_iguais(vetor[0], cria_peca(' ')):
            counter += 1
    return counter <= 1