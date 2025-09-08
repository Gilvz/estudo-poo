from datetime import datetime
import pytz
import sys

# Reconfigurar a saída para UTF-8
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')
#
# 2 enters de espaço entre classe e imports, método de organização
class ContaCorrente:
    '''
    Pesquisar PEP257 - Para estudar padrões de criações de Docstring

    Cria um objeto ContaCorrente para gerenciar as contas dos clientes

    Atributos:
        nome (str): Nome do cliente
        cpf (str): CPF do Cliente. Deve ser inserido com pontos e traços
        agencia:
        num_conta:
        saldo:
        limite:

    '''
    @staticmethod # Método auxiliar para o que está acontecendo dentro da classe
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y  %H:%M:%S')


    def __init__(self, nome, cpf, agencia, num_conta): # informações da instância são as que começam com 'self.'
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []

    def consultar__saldo(self):
        print('Seu _saldo atual é de R$ {:,.2f}'.format(self._saldo))

    def depositar(self, valor):
        self._saldo += valor
        self._.append((valor, self._saldo, ContaCorrente._data_hora())) # append aceita apenas 1 valor, e como temos 3 valores, é necessário usar uma tupla, que é o outro parêntese abraçando tudo

    def ___conta(self): # método não público
        self._ = -1000
        return self._

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self.___conta():
            print('Você não tem _saldo suficiente para sacar esse valor')
            self.consultar__saldo()
        else:
            self._saldo -= valor
            self._.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar___chequeespecial(self):
        print('Seu _ de cheque especial é de R${:,.2f}'.format(self.___conta( )))

    def consultar_historico__(self):
        print('Histórico de Transações:')
        print('Valor, _Saldo, Data e Hora')
        for transacao in self._:
            print(transacao)

    def transferir (self, valor, conta_destino):
        self._saldo -= valor
        self._.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


#programa
conta_Gilvaz = ContaCorrente('Gilvan', '047.153.971-25', 1234, 34062)
conta_Gilvaz.consultar__saldo()

#depositando dinheiro
conta_Gilvaz.depositar(10000)
conta_Gilvaz.consultar__saldo()


#sacando dinheiro
#conta_Gilvaz.sacar_dinheiro(10500)

print('_Saldo Final')
conta_Gilvaz.consultar__saldo()
conta_Gilvaz.consultar___chequeespecial()

print('-' * 20)
conta_Gilvaz.consultar_historico__()

print('-' * 20)
conta_Mila = ContaCorrente('Mila', '000.555.123-45', 4321 , 78561)
conta_Gilvaz.transferir(1000, conta_Mila)

conta_Gilvaz.consultar__saldo()
conta_Mila.consultar__saldo()

conta_Gilvaz.consultar_historico__()
conta_Mila.consultar_historico__()


