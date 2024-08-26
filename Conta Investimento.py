#Definindo Variáveis

class Conta_Investimento:
   def __init__(self,saldo__inicial,taxa__juros):
      self.saldo = saldo__inicial
      self.taxa__juros = taxa__juros

   def adicione_juros(self):
      self.saldo += self.saldo *(self.taxa__juros / 100)

#Exemplo de uso

conta = Conta_Investimento(1000,10)

#Aplicando o método adicione juros conco vezes

for _ in range(5):
   conta.adicione_juros()

#Imprimindo o valor do saldo final 

print(f'Saldo final: R${conta.saldo:.2f}')   