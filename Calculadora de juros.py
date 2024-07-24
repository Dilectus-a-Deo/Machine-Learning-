
# Inserindo variáveis

class Investimento:
    def __init__(self, saldo_inicial, taxa_juros_anual):
        """
        Construtor da classe Investimento.
        Args:
            saldo_inicial (float): Saldo inicial da conta.
            taxa_juros_anual (float): Taxa de juros anual (como decimal).
        """
        self.saldo = saldo_inicial
        self.taxa_juros_anual = taxa_juros_anual

    def adicione_juros(self):
        """
        Calcula e adiciona juros compostos à conta.
        Returns:
            float: Saldo final após adicionar os juros.
        """
        # Calcula o montante final usando a fórmula do juro composto
        montante_final = self.saldo * (1 + self.taxa_juros_anual)

        # Atualiza o saldo da conta
        self.saldo = montante_final

        return self.saldo

    def rendimento_mensal(self):
        """
        Calcula o rendimento mensal dos juros compostos.
        Returns:
            float: Rendimento mensal.
        """
        # Calcula o rendimento mensal usando a fórmula dos juros compostos
        rendimento_mensal = (1 + self.taxa_juros_anual) ** (1 / 12) - 1

        return rendimento_mensal


# Pedindo para que o usuário insira os valores

saldo_inicial = float(input("Digite o saldo inicial da conta: "))
taxa_juros_anual = float(input("Digite a taxa de juros anual (como decimal): "))

# Criar uma instância da classe Investimento

conta = Investimento(saldo_inicial, taxa_juros_anual)

# Adicionando os juros à conta

saldo_final = conta.adicione_juros()

# Calculando o rendimento mensal

rendimento_mensal = conta.rendimento_mensal()

# Imprimindo os resultados

print(f"O saldo final após adicionar os juros é ${saldo_final:.2f}")
print(f"O rendimento mensal dos juros compostos é {rendimento_mensal * 100:.2f}%")

# Inserindo variáveis

class Investimento:
    def __init__(self, saldo_inicial, taxa_juros_anual):
        """
        Construtor da classe Investimento.
        Args:
            saldo_inicial (float): Saldo inicial da conta.
            taxa_juros_anual (float): Taxa de juros anual (como decimal).
        """
        self.saldo = saldo_inicial
        self.taxa_juros_anual = taxa_juros_anual

    def adicione_juros(self):
        """
        Calcula e adiciona juros compostos à conta.
        Returns:
            float: Saldo final após adicionar os juros.
        """
        # Calcula o montante final usando a fórmula do juro composto
        montante_final = self.saldo * (1 + self.taxa_juros_anual)

        # Atualiza o saldo da conta
        self.saldo = montante_final

        return self.saldo

    def rendimento_mensal(self):
        """
        Calcula o rendimento mensal dos juros compostos.
        Returns:
            float: Rendimento mensal.
        """
        # Calcula o rendimento mensal usando a fórmula dos juros compostos
        rendimento_mensal = (1 + self.taxa_juros_anual) ** (1 / 12) - 1

        return rendimento_mensal


# Pedindo para que o usuário insira os valores

saldo_inicial = float(input("Digite o saldo inicial da conta: "))
taxa_juros_anual = float(input("Digite a taxa de juros anual (como decimal): "))

# Criar uma instância da classe Investimento

conta = Investimento(saldo_inicial, taxa_juros_anual)

# Adicionando os juros à conta

saldo_final = conta.adicione_juros()

# Calculando o rendimento mensal

rendimento_mensal = conta.rendimento_mensal()

# Imprimindo os resultados

print(f"O saldo final após adicionar os juros é ${saldo_final:.2f}")
print(f"O rendimento mensal dos juros compostos é {rendimento_mensal * 100:.2f}%")


