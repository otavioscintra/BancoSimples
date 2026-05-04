from clientes import Cliente
from contas import Conta


class Banco:
    def __init__(self, agencia: int, banco: str):
        self.agencia = agencia
        self.banco = banco
        self._clientes = []
        self._contas = []

    def adicionar_cliente(self, cliente: Cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError('o cliente deve ser do tipo cliente.')
        self._clientes.append(cliente)

    def adicionar_conta(self, conta: Conta):
        if not isinstance(conta, Conta):
            raise TypeError('A conta deve ser do tipo conta.')
        self._contas.append(conta)

    def verificar(self, cliente: Cliente, conta: Conta):
        if conta.agencia != self.agencia:
            raise ValueError('A agencia não é desse banco.')

        if cliente not in self._clientes:
            raise ValueError('o cliente não é desse banco')

        if conta not in self._contas:
            raise ValueError('A conta não é desse banco.')

        if conta.banco != self.banco:
            raise ValueError('A conta não é desse banco.')

        if conta != cliente.conta:
            raise ValueError('A conta não é desse cliente.')

    def sacar(self, cliente: Cliente, conta: Conta, valor: float):
        self.verificar(cliente, conta)
        conta.sacar(valor)
