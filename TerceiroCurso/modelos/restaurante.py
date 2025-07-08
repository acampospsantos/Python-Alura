from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

class Restaurante:
    #Atributos
    restaurantes = []
    #Esse é o método construtor do Python
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    #Funciona como o método toString em Java - para não recebermos na impressão o endereço de memória do objeto
    def __str__(self):
        return '{} | {}'.format(self.nome, self.categoria)
    
    @classmethod
    def listarRestaurantes(cls):
        print('Nome do restaurante'.ljust(25) + ' | ' + 'Categoria '.ljust(25) + ' | ' + 'Avaliação '.ljust(25) + ' | Status')
        for i in cls.restaurantes:
            print('{} | {} | {} | {}'.format(i._nome.ljust(25), i._categoria.ljust(25), str(i.mediaAvaliacoes).ljust(25), i.ativo))
    
    @property #Modifica como o atributo é lido
    def ativo(self):
        if(self._ativo == True):
            return 'Verdadeiro'
        else:
            return 'Falso'
    
    def alternarEstado(self):
        self._ativo = not self._ativo #Inverte o valor booleano

    def receberAvaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property
    def mediaAvaliacoes(self):
        if len(self._avaliacao) == 0:
            return '-'
        soma = 0
        for i in self._avaliacao:
            soma = soma + i._nota
        media = soma/len(self._avaliacao)
        media = round(media/2 , 1)
        return media
        #print('Média do filme {} = {}'.format(self._nome, media))
        

    def listarAvaliacoes(self):
        for i in self._avaliacao:
            print('{} - {}'.format(i._cliente, i._nota))


    ##def adicionarBebidaCardapio(self, bebida):
    ##    self._cardapio.append(bebida)
    
    ##def adicionarPratoCardapio(self, prato):
    ##    self._cardapio.append(prato)

    #Essa classe foi criada pra otimizar o código(em relação as duas classes acima)
    def adicionarAoCardapio(self, item):
        if isinstance(item, ItemCardapio): #Checa se o parâmetro é uma instância/derivada da classe itemCardapio
            self._cardapio.append(item)


    def listarCardapio(self):
        if(len(self._cardapio) > 0):
            print('----- CARDÁPIO DO RESTAURANTE {} -----'.format(self._nome))
            for i in range(len(self._cardapio)):
                mensagem = ('{}. Nome: {} | Preço: R${}'.format(i+1, self._cardapio[i]._nome, self._cardapio[i]._preco))
                if isinstance(self._cardapio[i], Prato):
                    print(mensagem + ' | Descrição = {}'.format(self._cardapio[i]._descricao))
                elif isinstance(self._cardapio[i], Bebida):
                    print(mensagem + ' | Tamanho = {}'.format(self._cardapio[i].getTamanho()))
            print('--------------------------------------')
        else:
            print('##Restaurante sem cardápio##')