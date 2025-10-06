from ContasBancos import CartaoCredito, ContaCorrente



conta_Gilvaz = ContaCorrente('Gilvan', '047.153.971-25', 1234, 34062)

cartao_Gilvaz = CartaoCredito('Gilvan', conta_Gilvaz)

cartao_Gilvaz.senha = '2354'
print(cartao_Gilvaz.senha)


print(conta_Gilvaz.__dict__)
print(cartao_Gilvaz.__dict__)



'''
print(cartao_Gilvaz.conta_corrente._num_conta)

print(cartao_Gilvaz.numero)

print(cartao_Gilvaz.cod_seguranca)
 
print(cartao_Gilvaz.validade)


#depositando dinheiro
conta_Gilvaz.depositar(10000)
conta_Gilvaz.consultar_saldo()


#sacando dinheiro
#conta_Gilvaz.sacar_dinheiro(10500)

print('_Saldo Final')
conta_Gilvaz.consultar_saldo()
conta_Gilvaz.consultar_limite_chequeespecial()

print('-' * 20)
conta_Gilvaz.consultar_historico_transacoes()

print('-' * 20)
conta_Mila = ContaCorrente('Mila', '000.555.123-45', 4321 , 78561)
conta_Gilvaz.transferir(1000, conta_Mila)

conta_Gilvaz.consultar_saldo()
conta_Mila.consultar_saldo()

conta_Gilvaz.consultar_historico_transacoes()
conta_Mila.consultar_historico_transacoes()


help(ContaCorrente)
'''