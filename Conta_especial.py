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
    

    def transferir_saldo(self, conta_destino, valor):
        if (self.saldo + self.limite) <  valor:
            return f"Saldo atual + limite são insuficientes para essa transferencia.\n".upper()
        else:
            conta_destino.saldo_transferido(valor)
            self.saldo -= valor

            if self.saldo < 0:
                self.saldo = self.limite + self.saldo
            self.extrato.transacoes.append(["Transferencia de R$", valor, datetime.datetime.today().strftime("%d/%m/%Y %H:%M:%S")])
        return super().transferir_saldo(conta_destino, valor)


    def transferir_especial(self, conta_destino, valor):
        if (self.saldo + self.limite) <  valor:
            return f"Saldo atual + limite são insuficientes para essa transferencia.\n".upper()
        else:
            conta_destino.saldo_transferido(valor)
            self.saldo -= valor

            if self.saldo < 0:
                self.limite += self.saldo
                print("Você entrou no cheque especial.\n")
                print(f"Limite especial restante: R${self.limite}\n".upper())
        return f"Transferencia de R${valor} para {conta_destino.cliente} realizado com sucesso em {self.data_abertura}.\n"