
candidatos=[["allan harlem",[5,10,8,8]],['michel farias',[10,7,7,8]],['thiago silva',[8,5,4,9]],['gabriel ramos',[2,2,2,1]],['dayane stefani',[10,10,8,9]]]
#candidatos:responsavel pelo nome é notas dos candidatos, as notas dos candidatos seguem a mesma ordem da quê sera listada na variavel 'categorias'.

categorias=['entrevista:','teste téorico','teste prático','avaliação de soft skills']
# categorias:Contém todas as categorias que foram usadas como parâmetros para a contratação do candidato

mensagemDeErro="\033[38;2;255;0;0m"+"nota digitada é invalida \n digite uma nota valida:"+"\033[0m"
#mensagemDeErro: mensagem de erro exibida ao usuario caso ele digite uma nota diferente de 0 a 10.  

textoBase="""base dos candidatos

descreva com notas entre 0 a 10 as notas mínimas para obtenção da vaga. """
#texto base do arquivo 


def recebedorDeNotas (mensagem='digite a nota:',notaMaxima=10):
    resposta=''
    while type(resposta) !=float or resposta>notaMaxima:
        try:
         resposta=(float(input(mensagem)))
        except:
           print('por favor digite somente valores númericos.')
        if resposta>notaMaxima:
            print('por favor digite uma nota entre 0 e {}'.format(notaMaxima))
    return resposta

# recebedorDeNotas: essa função possui dois parâmetros que são opcionais  a 'primeira' é a mensagem que é o valor quê será impresso no terminal para recebimento do valor escrito pelo cliente  é a segunda 'notaMaxima' que como o nome ja desreve é a maior nota que pode ser escrita pelo usuario. basicamente essa função e projetada para retornar um valor numerico no formato 'float'. 

   
 
