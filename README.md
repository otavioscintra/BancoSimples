# BancoSimples
Um sistema de banco simples feito em Python.
# BancoSimples - Sistema de Simulação Bancária em Python

### Esse projeto é uma simulação de Back-End feita como metôdo de estudo e treino.

## Funcionalidades

**Cadastro de Clientes:** Permite criar perfis com validação de dados básicos, 
sendo que cada cliente possui um vínculo direto e único com a sua conta bancaria.

**Este projeto** conta com diferentes tipos de contas e operações, sendo elas
**Conta Poupança (CP)**, **Conta Corrente (CC)** e o usuário só pode sacar
valores menores ou iguais ao seu saldo disponível.

## Tecnologias Utilizadas

**Python 3.14.0** 
**Módulo Nativo *abc***

## Estrutura do projeto

### ├── banco.py       # Classe central de orquestração e validação.
### ├── clientes.py    # Classes Pessoa e Cliente.
### ├── contas.py      # Classe abstrata Conta, ContaCorrente e ContaPoupanca.
