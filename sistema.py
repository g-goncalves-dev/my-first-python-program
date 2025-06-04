from DESAFIO_115.LIB.INTERFACE import *
from DESAFIO_115.LIB.arquivo import *
from MUNDO_03.desafio_115 import menu, cabecalho, leia_int
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu (['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        ## opção de listar o centeudo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m!')
        print()
        sleep(2)

