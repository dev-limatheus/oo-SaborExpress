from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restautante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Abacaxi', 5.00, 'Grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
restautante_praca.adicionar_no_cardapio(bebida_suco)
restautante_praca.adicionar_no_cardapio(prato_paozinho)



def main():
    restautante_praca.exibir_cardapio

if __name__ == '__main__':
    main()