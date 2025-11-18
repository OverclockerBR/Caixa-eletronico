from Extrato import Extrato
import datetime

class Conta:

    def __init__(self, cliente, numero, saldo):     # Parametros para o Construtor da classe Conta
        self.cliente = cliente      # atribuir Nome ao cliente
        self.numero = numero        # atribuir Numero da conta
        self.saldo = saldo      # atribuir Saldo inicial da conta
        self.data_abertura = datetime.datetime.today().strftime("%d/%m/%Y %H:%M:%S")        # Data e hora de abertura da conta
        self.extrato = Extrato()    # Composição: criando um objeto da classe Extrato dentro da classe Conta


    def depositar(self, valor):
        self.saldo += valor        # ou poderia ser também self.saldo = self.saldo + valor
        print(f"\nDepósito de R${valor} realizado com sucesso em {self.data_abertura}.")
        print(f"Saldo atual é de: R${self.saldo}")

    
    def sacar(self, valor):
        if self.saldo < valor:
            print("\nSaldo insuficiente para esse valor\n".upper())     # Fazendo ficar em maiusculo a mensagem de saldo insuficiente
            print(f"O saldo atual da sua conta continua sendo de R${self.saldo}\n".upper())
            return False
        else:
            self.saldo -= valor
            print(f"\nSaque de R${valor} efetuado com sucesso em {self.data_abertura}.")
            print(f"Saldo atual é de: R${self.saldo}")
            print(f"\n{30*"="} RETIRE SEU DINHEIRO! {30*"="}\n")      # Mensagem estilizada para o caixa eletrônico
            return True


    def gerar_saldo(self):
        print(f"{32*"="} saldo da conta {32*"="}".upper())
        print(f"Cliente: {self.cliente}")
        print(f"Numero da conta: {self.numero}")
        print(f"saldo atual: R${self.saldo}")
        return "\n"


    def transferir_saldo(self, conta_destino, valor):
        if self.saldo <  valor:
            return f"Saldo insuficiente para essa transferencia.\nO saldo atual da sua conta continua sendo de R${self.saldo}\n".upper()
        else:
            conta_destino.saldo_transferido(valor)
            self.saldo -= valor
        return f"Transferencia de R${valor} para {conta_destino.cliente} realizado com sucesso em {self.data_abertura}.\n"
            
            
    def saldo_transferido(self, valor):     # Metodo para receber o valor transferido
        self.saldo += valor        # ou poderia ser também self.saldo = self.saldo + valor   
        #print(f"Saldo atual é de: R${self.saldo}\n")

