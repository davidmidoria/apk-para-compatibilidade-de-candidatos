# inputsNumericos: recebe duas variaves um do conteudo do input() é o segundo do maior número que se quer ser recebido
# retorna um número de ponto flutuante
def inputsNumericos (mensagem='digite:',maiorInputPossivel=10):
        try:
         resposta=(float(input(mensagem)))
        except:resposta=maiorInputPossivel+1
        if  resposta<=maiorInputPossivel:
            return resposta
        else:
            print('digite um valor numerico entre 0 e {}'.format(maiorInputPossivel))
            inputsNumericos(maiorInputPossivel=maiorInputPossivel)

# valorItem recebe um texto para exibir no terminal é uma lista de itens, retorna uma lista com um valor para cada item 
def valorItem(texto,itens):
    print(texto)
    valosDosItens=[]
    for categoria in itens:
        valosDosItens.append(inputsNumericos(categoria))
    return valosDosItens

#comparaLista: faz uma comparação entre duas listas, retorna o número de vezes que os itens da lista0 foram maiores que o da lista1
def comparaLista(lista0,lista1):
    contador=0
    for item0,item1 in zip(lista0,lista1):
     if item0>=item1:
        contador+=1
    return contador

#comparadorDeListas: recebe uma lista aninhada é uma segunda lista modelo, retorna uma lista com as listas em que todos os itens são maiores
#que na lista modelo
def comparadorDeListas(listasaninhada,listamodelo):
   maioresQueModelo=[]
   for indice in range(len(listasaninhada)):
        if comparaLista(listasaninhada[indice][1],listamodelo)==len(listamodelo):
            maioresQueModelo.append(listasaninhada[indice])
   return maioresQueModelo

#listaDeaprovado recebe uma listas que deve conter uma ou mais listas em um formato especifico que vai imprimir uma mensagem com nome é as 
# notas dos aprovados
def listaDeaprovado(aprovados):
   if len(aprovados)>0:
      print("""os candidatos aptos para a vaga são:""")
      for i in aprovados:
         print('\nnome:{}\n pontuação:\nentrevista:{} teste téorico:{} teste prático:{} avaliação de soft skills:{}'.format(i[0],i[1][0],i[1][1],i[1][2],i[1][3]))
   else:
       print('não ha candidatos aptos')

#inputPadrao: recebe um texto que sera impresso, uma estrutura padrao e um maior número para o retorno, retorna 
# uma lista com números de ponto flutuante com valor maximo igual ao parametro maior numero
def inputPadrao(texto,estruturaPadrao,maiorNumero=10):
    listnotas=[]
    estrutura=[]
    notas=input(texto).strip().lower().replace('_',' ').split()
    for i in notas:
        try:
            if float(i[1:])<=maiorNumero:
                listnotas.append(float(i[1:]))
                estrutura.append(i[:1])
        except:
            estrutura=[]
    if estruturaPadrao==estrutura:
        return listnotas
    else:
        return inputPadrao(texto,estruturaPadrao)

# cadastro recebe uma lista contendo uma serie de informaçoes como estrutura padrão, txtnome, txtnotas retorna uma string é uma sequencia
#númerica
def cadastro(txtcadastro):
    estruturapadrao,txtnome,txtnotas=txtcadastro
    nome=input(txtnome)
    notas=inputPadrao(txtnotas,estruturapadrao)
    return [nome,notas]

candidatos=[]# local onde se armazena as informações do candidato 

categorias=['entrevista:','teste téorico:','teste prático:','avaliação de soft skills:']# categorias do teste

textoBase="filtro de candidatos\n\ndescreva com notas entre 0 a 10 o padrão minimo para obtenção da vaga"# texto base do filtro de candidatos

textoMenu=" cadastro e compatibilidade\nmenu inicial\n1-cadastrar funcionarios\n2-verificar compatibilidade\n0-sair\ndigite:"#texto do menu

txtcadastro=[['e','t','p','s'],'menu de cadastro\ndigite o nome do candidato:','informe as notas do'
              'teste no formato "eX_tX_pX_sX" sendo x o valor da nota, que não deve ser maior que 10\ndigite:' ]#uma lista que contém as
#informações necessarias para o cadastro

loop=None
while loop!=0:
    loop=inputsNumericos(textoMenu,2)#menu

    while loop==1:
        candidatos.append(cadastro(txtcadastro))
        loop= ( None if inputsNumericos('\n1-novo cadastro\n0-retornar\ndigite:',1)==0 else 1)#cadastro

    while loop==2:
        listaDeaprovado(comparadorDeListas(candidatos,valorItem(textoBase,categorias)))# parte que verifica a compatibilidade de um candidato.
        loop=(2 if inputsNumericos('\n1-nova consulta\n0-retornar\ndigite:',1)==1 else None)