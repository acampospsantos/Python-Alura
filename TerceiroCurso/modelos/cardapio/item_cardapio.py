from abc import ABC, abstractmethod #Esse import significa que a classe é Abstrata

class ItemCardapio(ABC):
    #Atributos (encapsulados)
    _nome = ''
    _preco = float

    #Método Construtor
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    #Método toString
    def __str__(self):
        return 'Nome = {}, Preço = R${}'.format(self._nome, self._preco)
    
    #Métodos Acessores e Modificadores(getters e setters)
    def setNome(self, nome):
        self._nome = nome
    
    def getNome(self):
        return self._nome
    
    def setPreco(self, preco):
        self._preco = preco

    def getPreco(self):
        return self._preco
    
    #As classes herdadas precisam implementar esse método
    @abstractmethod
    def aplicar_desconto(self):
        pass