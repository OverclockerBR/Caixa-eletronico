from Cliente import Cliente
from Conta_especial import Conta_especial
from Conta import Conta


############################## TESTE DA CLASSE CONTA ###############################

cliente1 = Cliente("João Silva", "123.456.789-00", "Rua A, 123")
cliente2 = Cliente("Maria Oliveira", "987.654.321-00", "Rua B, 456")
cliente3 = Cliente("Carlos Pereira", "456.789.123-00", "Rua C, 789")

conta1 = Conta(cliente1.nome, 67890, 5000)
conta2 = Conta(cliente2.nome, 54321, 15000)
conta3 = Conta_especial(cliente3.nome, 11223, 2000, 500)

"""print(f"\nNome do(a) cliente: {conta1.cliente}")
print(f"Numero da conta: {conta1.numero}")
print(f"Saldo atual: {conta1.saldo}")
print(f"Data de abertura da conta: {conta1.data_abertura}\n\n")


print(f"Nome do(a) cliente: {conta2.cliente}")
print(f"Numero da conta: {conta2.numero}")
print(f"Saldo atual: {conta2.saldo}")
print(f"Data de abertura da conta: {conta2.data_abertura}\n\n")"""

conta1.depositar(1000)

conta1.sacar(5000)

"""if conta1 == conta2:
    print("\nVocê não pode transferir para essa mesma conta.\n".upper())
else:
    print("\nTransferencia permitida.\n\n")"""

print(conta1.transferir_saldo(conta2, 1000))
print(conta3.transferir_saldo(conta1, 2100))

print(conta2.gerar_saldo())
print(conta1.gerar_saldo())
print(conta3.gerar_saldo())