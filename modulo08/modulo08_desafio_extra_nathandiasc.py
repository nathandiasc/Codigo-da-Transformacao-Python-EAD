# Representa um livro individual no sistema.
# Agrupa as características essenciais (título e autor)
# e controla se a obra está disponível para empréstimo.
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' por {self.autor} [{status}]"

# Representa o sistema gerenciador da biblioteca.
# Armazena a coleção de livros em seu acervo e realiza
# as operações do sistema (adicionar, emprestar e listar).

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado ao acervo.")

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"Sucesso: O livro '{livro.titulo}' foi emprestado.")
                    return
                else:
                    print(f"Aviso: O livro '{livro.titulo}' já está emprestado.")
                    return
        print(f"Erro: Livro '{titulo}' não encontrado na biblioteca.")

    def listar_livros(self):
        print("\n--- ACERVO DA BIBLIOTECA ---")
        for livro in self.livros:
            print(livro)


bib = Biblioteca()

livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("1984", "George Orwell")

bib.adicionar_livro(livro1)
bib.adicionar_livro(livro2)

bib.listar_livros()

bib.emprestar_livro("1984")
bib.listar_livros()