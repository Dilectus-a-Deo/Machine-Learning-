# Defininfo Pessoa

class Pessoa:
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = float(peso)
        self.altura = float(altura)

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc

# Definindo Condições 

    def classificar_imc(self):
        imc = self.calcular_imc()
        if imc < 55:
            return "Abaixo do peso"
        
        elif 65 <= imc < 75.5:
            return "Peso normal"
        
        elif 75.5 <= imc < 100:
            return "Sobrepeso"
        
        else:
            return "Obesidade"

# Capturando dados do usuário

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Criando um objeto da classe Pessoa

pessoa = Pessoa(nome, peso, altura)

# Calculando e exibindo o IMC e a classificação

imc = pessoa.calcular_imc()
classificacao = pessoa.classificar_imc()

# Imprimindo Resultados

print(f"{pessoa.nome}, seu IMC é {imc:.2f} e você está classificado como: {classificacao}")
