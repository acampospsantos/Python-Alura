from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    #Atributos (encapsulados)
    _tamanho = ''

    #Método Construtor
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    #Método toString
    def __str__(self):
        return super().__str__() + ', tamanho = {}'.format(self._tamanho)
    
    #Metodo Acessor
    def getTamanho(self):
        return self._tamanho
    
    #Desenvolvimento do método abstrato da classe mãe
    def aplicar_desconto(self):
        self._preco = self._preco - (self._preco * 0.05)