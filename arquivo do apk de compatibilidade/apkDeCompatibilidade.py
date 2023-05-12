def recebedorDeNotas (mensagem='digite a nota:',notaMaxima=10):
    resposta=''
    while type(resposta) !=float or resposta>notaMaxima:
        try:
         resposta=(float(input(mensagem)))
         if resposta>notaMaxima:
            print(f'escreva um valor numerico entre 0 e {notaMaxima}')
        except:
           print('por favor digite um valor numerico')
    return resposta
# recebedorDeNotas: essa função possui dois parâmetros que são opcionais  a 'primeira' é a mensagem que é o valor quê será impresso no terminal para recebimento do valor escrito pelo cliente  é a segunda 'notaMaxima' que como o nome ja desreve é a maior nota que pode ser escrita pelo usuario. basicamente essa função e projetada para retornar um valor numerico no formato 'float'. 

def padraoMinimo(textoBase,categorias):
    print(textoBase)
    padrao=[]
    for categoria in categorias:
        padrao.append(recebedorDeNotas(categoria))
    return padrao

#padraoMinimo: responsavel por escrever o texto base é armazenar a nota dada a diferentes categorias de dados, recebe texto base que funciona como um cabeçalho e categorias quê deve ser uma lista que sera iterada afim de que o usuario possa dar a nota como base o item especifico da lista, a função armazena uma nova lista com o nome de padrao que será o retorno dado pela função

def testeaprovacao(lista0,lista1):
    contador=0
    for item0,item1 in zip(lista0,lista1):
     if item0>=item1:
        contador+=1
    if contador==len(lista0):
       return True
    else:
       return False

#testeaprovacao: essa função verifica se todos os itens da lista 0 são maiores ou iguais ao da lista 

def testeDelista(emTexte,modelo):
   aprovado=[]
   for indice in range(len(emTexte)):
        if testeaprovacao(emTexte[indice][1],modelo)==True:
            aprovado.append(emTexte[indice])
   return aprovado

#função testeDeLista essa função faz uma iteração de listas recebida no parametro 'emtexte' e mede se os itens contidos nestas listas são todos maiores ou iguais aos quê estão na lista 'modelo', se todos os itens da lista forem maiores ou iguais a lista que contém a lista testada e devolvida  pela lista 'aprovado' na função return. 

def listaDeaprovado(aprovados):
   if len(aprovados)>0:
      print("""os candidatos aptos para a vaga são:""")
      for i in aprovados:
         print('\nnome:{}\n pontuação:\nentrevista:{} teste téorico:{} teste prático:{} avaliação de soft skills:{}'.format(i[0],i[1][0],i[1][1],i[1][2],i[1][3]))
   else:
       print('não ha candidatos aptos')

# recebe uma lista, se a lista conter uma ou mais listas sera escrito a lista com os candidatos aprovados caso não a mensagem 'não ha candidatos aptos'

def tramento(notas):
    listnotas=[]
    for i in notas:
        if i.isnumeric():
            listnotas.append(int(i))
    return listnotas

# recebe uma string, separa os numeros da string  e retorna os numeros no formato de lista

def cadastro():
    nome=input('menu de cadastro\ndigite o nome do candidato:')
    notas=tramento(input('informe as notas do texte no formato "eX_tX_pX_sX" sendo x o valor da nota\ndigite:'))
    return [nome,notas]

# cria uma lsta contendo um nome é uma lista com as notas do candidato

def simOuNao(mensagem):
    resposta=input(mensagem)
    if resposta=='1':
        return True
    if resposta=='0':
        return False
    else:
        print('digite 1 ou 0')
        return simOuNao()

# cria um looping caso o cliente digite algo diferente de 1 e 0 se for escrito 1 retorna True caso 0 retorna False

def menu(texto=''):
    print(texto)
    resposta=input('digite:')
    if resposta=='0':
        return False,False,False
    elif resposta =='1':
        return True,True,False
    elif resposta=='2':
        return True,False,True
    else:
        print('digite um número entre um e três')
        return menu()

# imprime um texto na tela e recebe um input() que devera ser um número entre 0 e 2 que retorna uma sequência de true e false true especifica para cada resposta. caso não for entra em looping atê que seja adcionada uma resposta valida.

candidatos=[]
#candidatos:responsavel pelo nome é notas dos candidatos, as notas dos candidatos seguem a mesma ordem da quê sera listada na variavel 'categorias'.

categorias=['entrevista:','teste téorico:','teste prático:','avaliação de soft skills:']
# categorias:Contém todas as categorias que foram usadas como parâmetros para a contratação do candidato
  

textoBase="""filtro de candidatos

descreva com notas entre 0 a 10 o padrão minimo para obtenção da vaga"""
# texto base do filtro dos funcionarios

textoMenu=""" 
cadastro e compatibilidade
menu inicial
1-cadastrar funcionarios
2-verificar compatibilidade
0-sair
"""
#texto do menu


loop0=True
while loop0==True:
    loop0,loop1,loop2=menu(textoMenu)

    # inicia um while  responsavel por iniciar o funcionamento do programa, na linha 120 as variaveis responsaveis pelos loopings do codigo recebe uma lista contendo Trues e falses que vão definir qual função deve ser chamada seja a de cadastro ou a de listaDeaprovado 

    while loop1==True:
        candidatos.append(cadastro())
        loop1= simOuNao('\n1-novo cadastro\n0-retornar\ndigite:')

        #cadastra os usuarios a partir da função cadastro, verifica se um novo candidato deve ou não ser cadastro ,retorna ao inicio do looping principal. 
    
    while loop2==True:
        listaDeaprovado(testeDelista(candidatos,padraoMinimo(textoBase,categorias)))
        loop2=simOuNao('\n1-nova consulta\n0-retornar\ndigite:')

    # cria uma lista com padrões minimos para os candidatos, compara com as listas presentes na lista candidatos, imprime os candidatos aptos caso eles existam  