#Definindo Variáveis

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo = 10000):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

# Exemplo de uso

conta = ContaCorrente(12345, "João Silva")
conta.deposito(1000)
conta.saque(500)
conta.alterarNome("João Souza")
print(conta.nome_correntista)

#Imprimindo valores

print(conta.nome_correntista)  
print(conta.saldo) 
