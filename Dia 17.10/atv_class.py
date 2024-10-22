class Animal:
    def __init__(self, nome, nome_cientifico, nutricao, habitat):
        self.nome = nome
        self.nome_cientifico = nome_cientifico
        self.nutricao = nutricao
        self.habitat = habitat
        
    def alimentar(self):
        print(f"{self.nome} está comendo...")

    def movimentar(self):
        print(f"{self.nome} está se movendo...")
class Chordata(Animal):
    def __init__(self, nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto):
        super().__init__(nome, nome_cientifico, nutricao, habitat)
        self.nervoso_dorsal = nervoso_dorsal
        self.endoesqueleto = endoesqueleto

    def caracteristicas_filo(self):
        print("O filo Chordata é caracterizado pela presença de um nervoso dorsal, "
              "um endoesqueleto e estruturas relacionadas ao sistema nervoso.")

class Mamiferos(Chordata):
    def __init__(self, nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas):
        super().__init__(nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto)
        self.mamarias = mamarias
        self.endotermicos = endotermicos
        self.orelhas = orelhas

    def amamentar(self):
        print(f"{self.nome} está amamentando os filhotes.")

class Carnivora(Mamiferos):
    def __init__(self, nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas, caninos_molares, pelagem_peltada):
        super().__init__(nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas)
        self.caninos_molares = caninos_molares
        self.pelagem_peltada = pelagem_peltada

    def habilidade_caca(self):
        print(f"{self.nome} usa suas habilidades de caça para pegar presas.")

class Canideos(Carnivora):
    def __init__(self, nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas, caninos_molares, pelagem_peltada, territorialidade, org_jacobson):
        super().__init__(nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas, caninos_molares, pelagem_peltada)
        self.territorialidade = territorialidade
        self.org_jacobson = org_jacobson
    
    def marcar_territorio(self):
        print(f"{self.nome} está marcando seu território.")

class Leão(Canideos): 
    def __init__(self):
        super().__init__(
            nome="Leão",
            nome_cientifico="Panthera leo",
            nutricao="Carnívoro",
            habitat="Savana e florestas",
            nervoso_dorsal="Sim",
            endoesqueleto="Sim",
            mamarias="Sim",
            endotermicos="Sim",
            orelhas="Sim",
            caninos_molares="Sim",
            pelagem_peltada="Sim",
            territorialidade="Alfa",
            org_jacobson="Sim"
        )

    def rugir(self):
        print(f"{self.nome} está rugindo majestuosamente.")

class Ornitorrinco(Mamiferos):
    def __init__(self):
        super().__init__(
            nome="Ornitorrinco",
            nome_cientifico="Ornithorhynchus anatinus",
            nutricao="Onívoro",
            habitat="Água doce",
            nervoso_dorsal="Sim",
            endoesqueleto="Sim",
            mamarias="Sim",
            endotermicos="Sim",
            orelhas="Sim"
        )

    def botar_ovo(self):
        print(f"{self.nome} está botando ovos, mesmo sendo um mamífero.")

class Morcego(Mamiferos):
    def __init__(self):
        super().__init__(
            nome="Morcego",
            nome_cientifico="Chiroptera",
            nutricao="Insetívoro",
            habitat="Cavernas e florestas",
            nervoso_dorsal="Sim",
            endoesqueleto="Sim",
            mamarias="Sim",
            endotermicos="Sim",
            orelhas="Sim"
        )

    def voar(self):
        print(f"{self.nome} está voando de forma noturna.")
class Baleia(Mamiferos):
    def __init__(self):
        super().__init__(
            nome="Baleia",
            nome_cientifico="Balaenoptera musculus",
            nutricao="Plâncton",
            habitat="Oceanos",
            nervoso_dorsal="Sim",
            endoesqueleto="Sim",
            mamarias="Sim",
            endotermicos="Sim",
            orelhas="Sim"
        )

    def cantar(self):
        print(f"{self.nome} está cantando nas profundezas do oceano.")

leão = Leão()
ornitorrinco = Ornitorrinco()
morcego = Morcego()
baleia = Baleia()

def exibir_informacoes(animal):
    print(f""" 
<<<-------------------------------------------------------------->>>
| Nome: {animal.nome}                                              
| Nome Científico: {animal.nome_cientifico}
<<<-------------------------------------------------------------->>>
| Nutrição: {animal.nutricao}
| Habitat: {animal.habitat}
| Nervoso Dorsal: {animal.nervoso_dorsal}
| Endoesqueleto: {animal.endoesqueleto}
| Mamárias: {animal.mamarias}
| Endotérmicos: {animal.endotermicos}
| Orelhas: {animal.orelhas}""")
    if isinstance(animal, Canideos):
        print(f"""| Caninos/Molares: {animal.caninos_molares}
| Pelagem Peltada: {animal.pelagem_peltada}
| Territorialidade: {animal.territorialidade}
| Órgão de Jacobson: {animal.org_jacobson}
<<<-------------------------------------------------------------->>>
""")
    if isinstance(animal, Mamiferos) and not isinstance(animal, Canideos):
        print("""<<<-------------------------------------------------------------->>>
""")
        
while True:
    try:
        escolha = int(input(""" 
<<<==============================================================>>>
|   Escolha um animal para visualizar suas Informações e Métodos   |
<<<==============================================================>>>                         
| 1 | Leão             |
| 2 | Ornitorrinco     |
| 3 | Morcego          |
| 4 | Baleia           |
| 0 | Sair             |
<<<====================| Escolha: """))

    except ValueError:
        print('\nValor Inválido!')
        continue

    if escolha == 1:
        exibir_informacoes(leão)
        leão.alimentar()
        leão.movimentar()
        leão.caracteristicas_filo()
        leão.amamentar()
        leão.habilidade_caca()
        leão.marcar_territorio()
        leão.rugir()
        
    elif escolha == 2:
        exibir_informacoes(ornitorrinco)
        ornitorrinco.alimentar()
        ornitorrinco.movimentar()
        ornitorrinco.amamentar()
        ornitorrinco.botar_ovo()
        
    elif escolha == 3:
        exibir_informacoes(morcego)
        morcego.alimentar()
        morcego.movimentar()
        morcego.amamentar()
        morcego.voar()
        
    elif escolha == 4:
        exibir_informacoes(baleia)
        baleia.alimentar()
        baleia.movimentar()
        baleia.amamentar()
        baleia.cantar()
        
    elif escolha == 0:
        print("\nSaindo do sistema...\n")
        break
        
    else:
        print("\nEscolha inválida. Tente novamente.")
