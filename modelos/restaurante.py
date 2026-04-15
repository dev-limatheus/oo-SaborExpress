from modelos.avaliacao import Avaliacao
from modelos.cardpio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):  #transformar o endereço de memoria em texto
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls): 
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Visibilidade'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante._ativo}')

    
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    def alternar_visibilidade(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)


    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        else:
            soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
            quantidade = len(self._avaliacao)
            media = round(soma / quantidade, 1)
            return media

    # def adicionar_bebida(self,bebida):
    #     self._cardapio.append(bebida)
    
    # def adicionar_prato(self,prato):
    #     self._cardapio.append(prato)

    def adicionar_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)