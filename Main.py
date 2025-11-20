from Cliente import Cliente
from Conta_especial import Conta_especial
from Conta import Conta



############################## TESTE DA CLASSE CONTA ###############################



cliente1 = Cliente("João Silva", "123.456.789-00", "Rua A, 123")
cliente2 = Cliente("Maria Oliveira", "987.654.321-00", "Rua B, 456")
cliente3 = Cliente("Carlos Pereira", "456.789.123-00", "Rua C, 789")

conta1 = Conta(cliente1.nome, 123, 5000)
conta2 = Conta(cliente2.nome, 456, 5000)
conta3 = Conta_especial(cliente3.nome, 789, 0, 500)

#print(conta2.depositar(5000))
print(conta3.depositar(1000))
print(conta3.depositar(4000))
print(conta3.transferir_saldo(conta1, 500))
print(conta1.transferir_saldo(conta3, 5000))
print(conta3.sacar(5500))
#print(conta2.transferir_saldo(conta1, 30))



print(f"\n{32 * "="} GERAR EXTRATO {32 * "="}\n".upper())
conta3.gerar_saldo()
conta3.extrato.gerar_extrato(conta3.numero)

#conta1.gerar_saldo()
#conta1.extrato.gerar_extrato(conta1.numero)