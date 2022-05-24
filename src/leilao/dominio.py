import sys


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        lance = Lance(self, valor)
        leilao.propoe(lance)
        self.__carteira -= valor

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    def propoe(self, lance: Lance):
        if not self.__lances or \
            self.__lances[-1].usuario != lance.usuario and \
                lance.valor > self.__lances[-1].valor:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor
            self.__lances.append(lance)
        else:
            raise ValueError('Erro ao propor lance')

    @property
    def lances(self):
        '''
            self.__lances[:] é uma cópia rasa.
            Cópia rasa:
                Quando utilizamos uma cópia rasa, apenas a referência da lista, 
                neste caso, é diferente. Todos os outros objetos dentro dessa lista 
                compartilham a mesma referência. Ou seja, apenas da lista de lances 
                ser uma cópia, os lances dentro da lista copiada são os mesmos lances do leilão.
                Para que os lances sejam diferentes, precisamos copiar a lista profundamente, 
                por isso os termos cópia rasa e cópia profunda.
        '''
        return self.__lances[:]
