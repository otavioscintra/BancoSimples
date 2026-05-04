from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, num_conta: int, banco: str) -> None:
        self.agencia = agencia
        self._num_conta = num_conta
        self.saldo = 0
        self.banco = banco

    def depositar(self, valor: float) -> float:
        if not isinstance(valor, (int, float)):
            raise TypeError('Você não inseriu um valor para ser depositado.')
        if valor <= 0:
            raise ValueError('o valor deve ser positivo.')
        self.saldo += valor
        return self.saldo

    @abstractmethod
    def sacar(self, valor) -> float:
        ...


class ContaCorrente(Conta):
    def __init__(self, agencia: int, num_conta: int,
                 banco: str, limite: float) -> None:
        super().__init__(agencia, num_conta, banco)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        if not isinstance(valor, (int, float)):
            raise TypeError('Não foi possível efetuar o saque.')
        if valor <= 0:
            raise ValueError('Não foi possível efetuar o saque.')
        if valor > self.saldo + self.limite:
            raise ValueError('Não foi possível efetuar o saque.')
        print('saque autorizado.')
        self.saldo -= valor
        return self.saldo


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        if not isinstance(valor, (int, float)):
            raise TypeError('Não foi possível efetuar o saque.')
        if valor <= 0:
            raise ValueError('Não foi possível efetuar o saque.')
        if valor > self.saldo:
            raise ValueError('Não foi possível efetuar o saque.')
        print('saque autorizado.')
        self.saldo -= valor
        return self.saldo
