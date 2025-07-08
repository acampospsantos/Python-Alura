import os 

# Puxa o arquivo restaurante da pasta modelos --> Importa a classe Restaurante 
from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida


restaurante_praca = Restaurante('Praca', 'Gourmet')

bebida_suco = Bebida('Suco de melancia', 5.0, 'Grande')
prato_paozinho = Prato('Pão', 2.00, 'O melhor pão da cidade')
pratoBom = Prato('Tapioca', 10, 'Da menininha')
pratoBom.aplicar_desconto()
refrigerante = Bebida('Coca Cola', 5, 'Médio')
refrigerante.aplicar_desconto()

restaurante_praca.adicionarAoCardapio(bebida_suco)
restaurante_praca.adicionarAoCardapio(prato_paozinho)
restaurante_praca.adicionarAoCardapio(pratoBom)
restaurante_praca.adicionarAoCardapio(refrigerante)



def main():
    os.system('cls')
    restaurante_praca.listarCardapio()


if(__name__ == '__main__'):
    main()