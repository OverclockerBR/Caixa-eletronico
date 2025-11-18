from Conta import Conta
import datetime


class Conta_especial(Conta):

    def __init__(self, cliente, numero, saldo, limite):
        super().__init__(cliente, numero, saldo)
        self.limite = limite  # Atributo adicional para Conta Especial


    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            return f"\nSaldo atual + limite especial insuficiente para esse saque.\n".upper()
        else:
            self.saldo -= valor
            if self.saldo < 0:
                self.limite += valor
            self.extrato.transacoes.append(["Saque de R$", valor, datetime.datetime.today().strftime("%d/%m/%Y %H:%M:%S")])
            return super().sacar(valor)
    

    def saldo_transferido(self, valor):
        if (self.saldo + self.limite) < valor:
            return f"\nSaldo atual + limite especial insuficiente para essa transferencia.\n".upper()
        else:
            self.saldo += valor
            if self.saldo < 0:
                self.limite += valor
            self.extrato.transacoes.append(["Transferencia de R$", valor, datetime.datetime.today().strftime("%d/%m/%Y %H:%M:%S")])
        return super().saldo_transferido(valor)