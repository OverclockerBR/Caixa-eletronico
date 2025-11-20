from Cliente import Cliente
from Conta_especial import Conta_especial
from Conta import Conta


############################## TESTE DA CLASSE CONTA ###############################



cliente1 = Cliente("João Silva", "123.456.789-00", "Rua A, 123")
cliente2 = Cliente("Maria Oliveira", "987.654.321-00", "Rua B, 456")
cliente3 = Cliente("Carlos Pereira", "456.789.123-00", "Rua C, 789")

conta1 = Conta(cliente1.nome, cliente1.cpf, 5000)
conta2 = Conta(cliente2.nome, cliente2.cpf, 15000)
conta3 = Conta_especial(cliente3.nome, cliente3.cpf, 2000, 500)


conta1.depositar(1000)

conta1.sacar(5000)


print(conta1.transferir_saldo(conta2, 1000))
print(conta3.transferir_especial(conta1, 2200))

print(conta2.gerar_saldo())
print(conta1.gerar_saldo())
print(conta3.gerar_saldo())