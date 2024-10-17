class Carro:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

fusca = Carro('VolksWagen','Fusca','Preto',1967)
civic = Carro('Honda',"Civic","Vermelho",1945)

class Moto:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

harley = Moto('Harley Davidson','FatBoy','Azul',2019)

print(vars(fusca))
print(vars(civic))
print("")

for key, value in vars(harley).items():
    print(f"{key}: {value}")




