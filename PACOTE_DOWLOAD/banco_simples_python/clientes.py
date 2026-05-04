from contas import Conta


class Pessoa:
    def __init__(self) -> None:
        self._nome = None
        self._idade = None

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        self._nome = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor: int):
        if not isinstance(valor, int):
            raise TypeError('Não é uma idade válida.')
        if valor < 0:
            raise ValueError('Não é uma idade válida.')
        self._idade = valor


class Cliente(Pessoa):
    def __init__(self, banco: str) -> None:
        super().__init__()
        self.conta = None
        self.banco = banco

    def adicionar_conta(self, conta: Conta):
        if not isinstance(conta, Conta):
            raise TypeError('A conta deve ser do tipo Conta.')
        self.conta = conta
