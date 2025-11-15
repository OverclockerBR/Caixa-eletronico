import datetime

class Conta:

    def __init__(self, cliente, numero, saldo):     # Parametros para o Construtor da classe
        self.cliente = cliente      # atribuir Nome ao cliente
        self.numero = numero        # atribuir Numero da conta
        self.saldo = saldo      # atribuir Saldo inicial da conta
        self.data_abertura = datetime.datetime.today().strftime("%d/%m/%Y %H:%M:%S")        # Data e hora de abertura da conta


    def depositar(self, valor):
        self.saldo += valor        # ou poderia ser também self.saldo = self.saldo + valor
        print(f"\nDepósito de R${valor} realizado com sucesso.")
        print(f"Saldo atual é de: R${self.saldo}")


    def sacar(self, valor):
        if self.saldo < valor:
            print("\nSaldo insuficiente para esse valor\n".upper())     # Fazendo ficar em maiusculo a mensagem de saldo insuficiente
            print(f"O saldo atual continua sendo de R${self.saldo}\n".upper())
        else:
            self.saldo -= valor
            print(f"\nSaque de R${valor} efetuado com sucesso.")
            print(f"Saldo atual é de: R${self.saldo}")
            print(f"\n{30*"="} RETIRE SEU DINHEIRO! {30*"="}\n")      # Mensagem estilizada para o caixa eletrônico


    def gerar_extrato(self):
        print(f"\n{32*"="} Extrato da conta {32*"="}".upper())
        print(f"Cliente: {self.cliente}")
        print(f"Numero da conta: {self.numero}")
        print(f"saldo atual: R${self.saldo}\n\n")


    def transferir_saldo(self, conta_destino, valor):
        pass





############################## TESTE DA CLASSE CONTA ###############################
"""c1 = Conta("Ana Maria", 12345, 10000)
print(f"Nome do(a) cliente: {c1.cliente}")
print(f"Numero da conta: {c1.numero}")
print(f"Saldo atual: {c1.saldo}")
print(f"Data de abertura da conta: {c1.data_abertura}")

c1.depositar(900)

c1.sacar(5000)

c1.gerar_extrato()"""

conta1 = Conta("João Silva", 67890, 5000)
conta2 = Conta("Maria Oliveira", 54321, 15000)

if conta1 == conta2:
    print("\nVocê não pode transferir para essa mesma conta.\n".upper())
else:
    print("\nTransferencia permitida.\n")