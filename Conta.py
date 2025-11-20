from Extrato import Extrato
import datetime

class Conta:

    def __init__(self, cliente, numero, saldo):     # Parametros para o Construtor da classe Conta
        self.cliente = cliente      # atribuir Nome ao cliente
        self.numero = numero        # atribuir Numero da conta
        self.saldo = saldo      # atribuir Saldo inicial da conta
        self.data_abertura = datetime.datetime.today().strftime('%d/%m/%Y %H:%M:%S')        # Data e hora de abertura da conta
        self.extrato = Extrato()    # Composição: criando um objeto da classe Extrato dentro da classe Conta


    def depositar(self, valor):
        self.saldo += valor        # ou poderia ser também self.saldo = self.saldo + valor
        self.extrato.transacoes.append(["Deposito", valor, datetime.datetime.today()])
        print(f"\nDepósito de R${valor} realizado com sucesso.")
        print(f"Saldo atual é de: R${self.saldo}")
        return "\n"

    
    def sacar(self, valor):
        if self.saldo < valor:
            print("\nSaldo insuficiente para esse valor\n".upper())     # Fazendo ficar em maiusculo a mensagem de saldo insuficiente
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["Saque", valor, datetime.datetime.today()])
            print(f"\nSaque de R${valor} efetuado com sucesso.")
            print(f"\n{30*"="} RETIRE SEU DINHEIRO! {30*"="}\n")      # Mensagem estilizada para o caixa eletrônico
            return True


    def gerar_saldo(self):
        print(f"Cliente: {self.cliente}\n")
        print(f"Numero da conta: {self.numero}\n")
        print(f"saldo atual: R${self.saldo}\n")


    def transferir_saldo(self, conta_destino, valor):
        if self.saldo < valor:
            return f"Saldo insuficiente para essa transferencia.\n".upper()
        else:
            conta_destino.saldo_transferido(valor)
            self.extrato.transacoes.append(["Transf. Enviada", valor, datetime.datetime.today()])
            self.saldo -= valor
        return f"Transferencia de R${valor} para {conta_destino.cliente} realizado com sucesso.\n"
            
            
    def saldo_transferido(self, valor):     # Metodo para receber o valor transferido
        self.saldo += valor        # ou poderia ser também self.saldo = self.saldo + valor
        self.extrato.transacoes.append(["Transf. Recebida", valor, datetime.datetime.today()])
        #print(f"Saldo atual é de: R${self.saldo}\n")

