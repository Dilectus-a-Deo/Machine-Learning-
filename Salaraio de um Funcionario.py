#Definindo Variáveis 

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario

# Exemplo de uso

funcionario = Funcionario("Maria", 5000.00)

#Imprimindo Valores

print(f"Nome: {funcionario.get_nome()}")
print(f"Salário: R${funcionario.get_salario():.2f}")
