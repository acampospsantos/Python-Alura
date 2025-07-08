from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    #Atributos (encapsulados)
    _descricao = ''

    #Método Construtor
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    #Método toString
    def __str__(self):
        return super().__str__() + ' , Descrição = {}'.format(self._descricao)
    
    def getDescricao(self):
        return self._descricao
    
    def aplicar_desconto(self):
        self._preco = self._preco - (self._preco * 0.08)