# Puxa o arquivo restaurante da pasta modelos --> Importa a classe Restaurante 
from modelos.restaurante import Restaurante


restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternarEstado()

restaurante_mexicano.receberAvaliacao('João', 8)
restaurante_mexicano.receberAvaliacao('Luísa', 10)

def main():
    Restaurante.listarRestaurantes()


if(__name__ == '__main__'):
    main()