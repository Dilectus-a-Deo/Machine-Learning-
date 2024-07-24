import datetime

class Livro:
    def __init__(self):
        self.livro = {}
        self.emprestimo = {}

    def adicionar_livro(self, titulo):
        self.livro[titulo] = True

    def emprestimo_livro(self, titulo, usuario, prazo_de_entrega):
        if self.livro.get(titulo):
            self.livro[titulo] = False
            self.livro[usuario] = (titulo, prazo_de_entrega)
            return True
        else:
            return False

    def retornar_livro(self, usuario):
        if usuario in self.emprestimo:
            titulo,prazo_de_entrega = self.emprestimo[usuario]
            self.livro[titulo] = True
            del self.emprestimo[usuario]
            if prazo_de_entrega.prazo+prazo_de_entrega.agora() > prazo_de_entrega:
                return "Multa por atraso na devolução do livro."
            else:
                return "Livro devolvido com sucesso."
        else:
            return "Usuário não possui nenhum livro emprestado."

livro = Livro()
livro.adicionar_livro("Estatística")
print(livro.emprestimo_livro("Estatística", "Pedro", datetime.datetime.now() + datetime.timedelta(days=7)))

print(livro.retornar_livro("Pedro"))
