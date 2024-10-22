class Livro():
    def __init__(self, titulo, autor, cod_livro):
        self.titulo = titulo
        self.autor = autor
        self.status = 'Disponivel'
        self.cod_livro = cod_livro
        self.usuario = None

    def emprest_livro(self, usuario):
        if self.status != 'Disponivel':
            return
        
        self.usuario = usuario
        self.status = 'Emprestado'

    def devolv_livro(self):
        if self.status != 'Emprestado':
            return
        
        self.usuario = None
        self.status = 'Disponivel'

class Usuario:
    max_emprestimo = 3

    def __init__(self, nome_user, cpf, telefone):
        self.nome_user = nome_user
        self.cpf = cpf
        self.telefone = telefone
        self.lista_livros = []

    def pegar_emprestado(self, livro):
        if len(self.lista_livros) >= self.max_emprestimo:
            print(f'{self.nome_user} não pode pegar mais livros. Limite de {self.max_emprestimo} atingido.')
            return False
        
        if livro.emprest_livro(self):
            self.lista_livros.append(livro.titulo)
            return True
        return False

    def devolver_livro(self, livro):
        if livro.titulo in self.lista_livros:
            if livro.devolv_livro():
                self.lista_livros.remove(livro.titulo)
                return True
        else:
            print(f'{self.nome_user} não possui o livro "{livro.titulo}".')
            return False