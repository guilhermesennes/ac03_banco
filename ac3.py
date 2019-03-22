__alunos__ = ["guilherme.domingues@aluno.faculdadeimpacta.com.br", "thiago.brito@aluno.faculdadeimpacta.com.br"]


class Cliente():
    """
    A classe Cliente deve ter os atributos: nome, telefone e email, que
    serão passados em sua construção.
    Não é necessário implementar nenhum método para esta classe.
    """
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email


class Banco():
    """
    A classe Banco deverá receber um nome em sua construção e deverá
    implementar os métodos:
    abre_contas(clientes e saldo inicial): abre uma nova conta
    e lista_contas(): apresenta um resumo de todas as contas do banco
    DICA: mantenha uma variável interna qe armazene todas as contas do banco
    DICA2: utilze a variável acima para gerar automaticamente o número das
    contas do banco
    """
    def __init__ (self, nome):
        self.nome = nome
        self.contas = []
            
    def abre_contas(self, cliente, saldo_inicial):
        pass
    
    def lista_contas(self):
        pass


class Conta():
    """
    A Classe conta deverá receber em sua construção os atributos:
    clientes (uma lista de Clientes), número da conta e um saldo inicial.
    Ela deverá implementar os métodos:
    saque(valor): diminui o saldo em valor
    deposito(valor): aumenta o saldo em valor
    extrato: exibe todas as transações da conta e o saldo após cada transação
    resumo():  imprime um resumo da conta (nome dos clientes, numero da conta
    e saldo)
    DICA: Para fazer a função extrato faça uma variável interna que que
    armazene todas as operações de saque e deposito e seus valores.
    """
    def __init__(self, clientes_lista, numero_conta, saldo_inicial):
        self.clientes_lista = clientes_lista
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial
        self.extrato = []
        self.extrato.append({"deposito": self.saldo})

    def saque(self, valor):
        self.saldo -= valor
        self.extrato.append({"saque": valor})
        self.extrato.append({"saldo total": self.saldo})

    def deposito(self, valor):
        self.saldo += valor
        self.extrato.append({"deposito": valor})
        self.extrato.append({"saldo total": self.saldo})
    
    def resumo(self):
       for cli in self.clientes_lista:
            print(f"Nome: {cli.nome}, Conta: {self.numero_conta}, Saldo: {self.saldo}")                        
        

    def extrato_cliente(self):
        for item in self.extrato:
            print(item)
        

        


guilherme = Cliente("Guilherme", "987117762", "xxxxxxxxx@uuuuuuuu.qqq.bb")
thiago = Cliente("Thiago", "123456789", "thiago@uuuuuuuu.qqq.bb")
maria = Cliente("Maria", "123456789", "maria@uuuuuuuu.qqq.bb")
lista_clientes = [guilherme, thiago, maria]
conta_guilherme = Conta(lista_clientes, 123, 1000)
conta_guilherme.deposito(20)
conta_guilherme.deposito(50)
conta_guilherme.saque(30)
conta_guilherme.resumo()
conta_guilherme.extrato_cliente()
