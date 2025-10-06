from random import randint

class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nivel recomendado. Caixa atual: {}'.format(self.caixa))
        else:
            print('O valor de caixa esta ok. Caixa atual: {}'.format(self.caixa))


    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Emprestimo nao e possivel. Saldo nao disponivel em caixa. Saldo atual: {}'.format(self.caixa))

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))



class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 10000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor
        
    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor

class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1000, 9999))
        self.caixa = 1000000


class AgenciaVPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1000, 9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('Infelizmente voce nao possui patrimonio suficiente para esta agencia')


if __name__ == '__main__':
    agencia_virtual = AgenciaVirtual('wwww.agenciavirtual.com.br', 2222233333, 1234567893562)
    agencia_virtual.verificar_caixa()
    agencia_comum = AgenciaComum(3333366666, 456788981251)
    agencia_premium = AgenciaVPremium(3333366666, 456788981251)

    agencia_virtual.depositar_paypal(20000)
    print(agencia_virtual.caixa)
    print(agencia_virtual.caixa_paypal)

    agencia_premium.adicionar_cliente('Gilvan', 12357982186, 125000000)
    print(agencia_premium.clientes)

    agencia_comum.adicionar_cliente('Bruno', 45648623159, 152)
    print(agencia_comum.clientes)

















'''agencia1 = Agencia(6199888878, 3566666666, 4297)

agencia1.caixa = 12050000

agencia1.verificar_caixa()

agencia1.emprestar_dinheiro(100000, 42684623768, 0.03)
print(agencia1.emprestimos)

agencia1.adicionar_cliente('Gilvaz', 12345678922, 10000)
print(agencia1.clientes)'''