
candidatos=[["allan harlem",[5,10,8,8]],['michel farias',[10,7,7,8]],['thiago silva',[8,5,4,9]],['gabriel ramos',[2,2,2,1]],['dayane stefani',[10,10,8,9]]]
#candidatos:responsavel pelo nome é notas dos candidatos, as notas dos candidatos seguem a mesma ordem da quê sera listada na variavel 'categorias'.

categorias=['entrevista:','teste téorico:','teste prático:','avaliação de soft skills:']
# categorias:Contém todas as categorias que foram usadas como parâmetros para a contratação do candidato

mensagemDeErro="\033[38;2;255;0;0m"+"nota digitada é invalida \n digite uma nota valida:"+"\033[0m"
#mensagemDeErro: mensagem de erro exibida ao usuario caso ele digite uma nota diferente de 0 a 10.  

textoBase="""filtro de candidatos

descreva com notas entre 0 a 10 o padrão minimo para obtenção da vaga"""


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

#testeaprovacao: essa função verifica se todos os itens da lista 0 são maiores ou iguais ao da lista 1


