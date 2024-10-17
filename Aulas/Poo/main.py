class Carro:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def acelerar(self):
        print(f'O carro {self.modelo} da marca {self.marca} acelerou. ')

class Moto:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
    def acelerar(self):
        print(f'A moto {self.modelo} da marca {self.marca} acelerou. ')

fusca = Carro('VolksWagen','Fusca','Preto',1967)
civic = Carro('Honda',"Civic","Vermelho",1945)
harley = Moto('Harley Davidson','FatBoy','Azul',2019)


print("\n======== Carros ========")
print(vars(fusca))
print(vars(civic))


print("\n======== Motos ========")
for key, value in vars(harley).items():
    print(f"{key}: {value}")
