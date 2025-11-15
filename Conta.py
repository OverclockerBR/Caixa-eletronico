import datetime

class Conta:

    def __init__(self, cliente, numero, saldo):
        self.cliente = cliente
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today().strftime("%d/%m/%Y %H:%M:%S")


c1 = Conta("Ana Maria", 12345, 10000)
print(f"Nome do(a) cliente: {c1.cliente}")
print(f"Numero da conta: {c1.numero}")
print(f"Saldo atual: {c1.saldo}")
print(f"Data de abertura da conta: {c1.data_abertura}")