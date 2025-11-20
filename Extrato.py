class Extrato:

    def __init__(self):
        self.transacoes = []  # Lista para armazenar as transações


    def gerar_extrato(self, conta):
        #print(f"\nExtrato da Conta {conta}.\n")

        for transacao in self.transacoes:
            print(f"{transacao[0]:16s} {transacao[1]:10.2f} {transacao[2].strftime('   %d/%b/%Y')}")

        print("\n")

        
