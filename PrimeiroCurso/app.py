import time
import os

#Variáveis
restaurantes = [{'Nome': 'Bonaparte', 'Categoria': 'Geral', 'Ativo': False },
                {'Nome': 'Mc Donalds', 'Categoria': 'Fast Food', 'Ativo': True},
                {'Nome': 'Outback', 'Categoria': 'Geral', 'Ativo': False}]

#Funções - Modularização
def voltarMenuPrincipal():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcaoInvalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('# Opção Inválida! #\n')
    voltarMenuPrincipal()

def exibirSubTitulo(texto):
    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)


def cadastrarNovoRestaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibirSubTitulo('Cadastro de novos restaurantes')
    nomeRestaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoriaRestaurante = input('Digite a categoria do restaurante {}: '.format(nomeRestaurante))
    dadosRestaurante = {'Nome': nomeRestaurante, 'Categoria': categoriaRestaurante, 'Ativo': False}
    restaurantes.append(dadosRestaurante)
    print('O restaurante {} foi cadastrado com sucesso!'.format(nomeRestaurante))
    voltarMenuPrincipal()

def listarRestaurantes():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    exibirSubTitulo('Lista de Restaurantes')
    print('{}   {}   {}'.format('Nome restaurante'.ljust(20), 'Tipo do restaurante'.ljust(20), 'Estado'))
    for i in restaurantes:
        nomeRestaurante = i['Nome']
        categoriaRestaurante = i['Categoria']
        ativoRestaurante = i['Ativo']
        if(ativoRestaurante == True):
            ativoRestaurante = 'Ativado'
        else:
            ativoRestaurante = 'Desativado'
        print('- {} | {} | {}'.format(nomeRestaurante.ljust(20), categoriaRestaurante.ljust(20), ativoRestaurante))
    voltarMenuPrincipal()

def alternarEstadoRestaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    nomeRestaurante = input('Digite o nome do restaurante que se deseja mudar o estado: ')
    restauranteEncontrado = False
    for restaurante in restaurantes:
        if (nomeRestaurante == restaurante['Nome']):
            restauranteEncontrado = True
            restaurante['Ativo'] = not restaurante['Ativo'] #Independente do valor na chave 'Ativo' - o valor será invertido por conta do not
            if(restaurante['Ativo'] == True):
                print('Restaurante {} foi ativado com sucesso!'.format(nomeRestaurante))
            else:
                print('Restaurante {} foi desativado com sucesso!'.format(nomeRestaurante))
    if (restauranteEncontrado == False):
        print('O restaurante {} NÃO foi encontrado!'.format(nomeRestaurante))
    voltarMenuPrincipal()

def finalizarApp():
    ''' Exibe mensagem de finalização do aplicativo '''
    os.system('cls')
    print('Saindo do programa...\n')
    time.sleep(3)
    #exit()


def exibirNomePrograma():
    ''' Exibe o nome estilizado do programa na tela '''
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n''')

def exibirOpcoes():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def escolherOpcao():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao = int(input('Escolha uma opção: '))

        if(opcao == 1):
            # Cadastrar restaurante
            cadastrarNovoRestaurante()
        elif(opcao == 2):
            # Listar os restaurantes
            listarRestaurantes()
        elif(opcao == 3):
            #Ativar restaurante
            alternarEstadoRestaurante()
        elif(opcao == 4):
            finalizarApp()
        else:
            opcaoInvalida()
    except:
        opcaoInvalida()

def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibirNomePrograma()
    exibirOpcoes()
    escolherOpcao()

if(__name__ == '__main__'):
    main()