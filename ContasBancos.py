from datetime import datetime
import pytz
import sys
from random import randint

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
        agencia: Agencia responsável pela conta do cliente
        num_conta: Número da conta corrente do cliente
        saldo: Saldo disponível a conta do cliente
        limite: Limite de cheque especial daquele cliente
        transacoes: Histórico de transações do cliente

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
        self.cartoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é de R$ {:,.2f}'.format(self._saldo))

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora())) # append aceita apenas 1 valor, e como temos 3 valores, é necessário usar uma tupla, que é o outro parêntese abraçando tudo

    def _limite_conta(self): # método não público
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Você não tem _saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequeespecial(self):
        print('Seu limite de cheque especial é de R${:,.2f}'.format(self._limite_conta( )))

    def consultar_historico_transacoes(self):
        print('Histórico de Transações:')
        print('Valor, _Saldo, Data e Hora')
        for transacao in self._transacoes:
            print(transacao)

    def transferir (self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


class CartaoCredito:


    @staticmethod # Método auxiliar para o que está acontecendo dentro da classe
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR
    


    def __init__(self, titular, conta_corrente):
        self.numero = randint(10000000000000000, 99999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)    
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self.limite = None
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)


    @property
    def senha(self):
            return self._senha
        
    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
                self._senha = valor
        else:
            print("Senha inválida!")


  
#programa
