class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Bistrô'
restaurante_praca.categoria = 'Italiana'

if restaurante_praca.ativo:
    print(f'Restaurante {restaurante_praca.nome} está inativo.')
else:
    print(f'Restaurante {restaurante_praca.nome} está ativo.')

categoria = Restaurante.categoria


restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

if restaurante_pizza.categoria == 'Fast Food':
    print(f'Categoria do {restaurante_pizza.nome} é "Fast Food".')
else:
    print(f'Categoria do {restaurante_pizza.nome} não é "Fast Food"')

restaurante_pizza.ativo = True

nome_do_restaurante = restaurante_praca.nome

restaurantes = [restaurante_praca, restaurante_pizza]

print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')