class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):  #transformar o endereço de memoria em texto
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Bistrô', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Place', 'Italiano')

Restaurante.listar_restaurantes()