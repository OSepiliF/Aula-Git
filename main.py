class Carro:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

fusca = Carro('VolksWagen','Fusca','Preto','1967')

print(fusca.ano)
