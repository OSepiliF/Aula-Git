# Criar um sistema de classificação de animais vertebrados usando programação orientada a objetos (POO) em Python,
#  representando subdivisões até chegar a classes específicas como Ornitorrinco, Morcego e Baleia.

class Animais:
    def __init__(self, nome, nome_cientifico, alimentacao, habtat):
        self.nome = nome
        self.nome_cientifico = nome_cientifico
        self.alimentacao = alimentacao
        self.habtat = habtat
