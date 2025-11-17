from classes.Extrato import Extrato
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
        print(f"\nDepósito de R${valor} realizado com sucesso.")
        print(f"Saldo atual é de: R${self.saldo}")

    
    def sacar(self, valor):
        if self.saldo < valor:
            print("\nSaldo insuficiente para esse valor\n".upper())     # Fazendo ficar em maiusculo a mensagem de saldo insuficiente
            print(f"O saldo atual da sua conta continua sendo de R${self.saldo}\n".upper())
            return False
        else:
            self.saldo -= valor
            print(f"\nSaque de R${valor} efetuado com sucesso.")
            print(f"Saldo atual é de: R${self.saldo}")
            print(f"\n{30*"="} RETIRE SEU DINHEIRO! {30*"="}\n")      # Mensagem estilizada para o caixa eletrônico
            return True


    def gerar_saldo(self):
        print(f"\n{32*"="} saldo da conta {32*"="}".upper())
        print(f"Cliente: {self.cliente}")
        print(f"Numero da conta: {self.numero}")
        print(f"saldo atual: R${self.saldo}\n")


    def transferir_saldo(self, conta_destino, valor):
        if self.saldo <  valor:
            return f"Saldo insuficiente para essa transferencia.\nO saldo atual da sua conta continua sendo de R${self.saldo}\n".upper()
        else:
            conta_destino.saldo_transferido(valor)
            self.saldo -= valor
            
            
    def saldo_transferido(self, valor):     # Metodo para receber o valor transferido
        self.saldo += valor        # ou poderia ser também self.saldo = self.saldo + valor
        return f"\nTransferencia de R${valor} para {self.cliente} realizado com sucesso."
        #print(f"Saldo atual é de: R${self.saldo}\n")



############################## TESTE DA CLASSE CONTA ###############################
conta1 = Conta("João Silva", 67890, 5000)
conta2 = Conta("Maria Oliveira", 54321, 15000)

print(f"\nNome do(a) cliente: {conta1.cliente}")
print(f"Numero da conta: {conta1.numero}")
print(f"Saldo atual: {conta1.saldo}")
print(f"Data de abertura da conta: {conta1.data_abertura}\n\n")


print(f"Nome do(a) cliente: {conta2.cliente}")
print(f"Numero da conta: {conta2.numero}")
print(f"Saldo atual: {conta2.saldo}")
print(f"Data de abertura da conta: {conta2.data_abertura}\n\n")

#c1.depositar(900)

#c1.sacar(5000)

#c1.gerar_saldo()

"""if conta1 == conta2:
    print("\nVocê não pode transferir para essa mesma conta.\n".upper())
else:
    print("\nTransferencia permitida.\n\n")"""

print(conta1.transferir_saldo(conta2, 200000))

print(conta2.gerar_saldo())
print(conta1.gerar_saldo())