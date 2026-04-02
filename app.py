from modelos.restaurante import Restaurante

restautante_praca = Restaurante('praça', 'Gourmet')
# restaurante_mexicano = Restaurante('Mexican food', 'Mexicana')
# restaurante_japones = Restaurante('Japa', 'japonesa')

restautante_praca.alternar_visibilidade()
restautante_praca.receber_avaliacao('Mat', 8)
restautante_praca.receber_avaliacao('Rage', 10)
restautante_praca.receber_avaliacao('Lima', 2)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()