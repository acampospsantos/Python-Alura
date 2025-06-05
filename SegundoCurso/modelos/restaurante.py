from modelos.avaliacao import Avaliacao

class Restaurante:
    #Atributos
    restaurantes = []
    #Esse é o método construtor do Python
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
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
            soma = soma + i.nota
        media = soma/len(self._avaliacao)
        media = round(media/2 , 1)
        return media
        #print('Média do filme {} = {}'.format(self._nome, media))
        

    def listarAvaliacoes(self):
        pass