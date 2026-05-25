
# BancoSimples - Sistema de Simulação Bancária em Python

### Esse projeto é uma simulação de Back-End feita como método de estudo e treino.

## Funcionalidades

**Cadastro de Clientes:** Permite criar perfis com validação de dados básicos, 
sendo que cada cliente possui um vínculo direto e único com a sua conta bancária.

**Este projeto** conta com diferentes tipos de contas e operações, sendo elas:
**Conta Poupança (CP):**  o usuário só pode sacar
valores menores ou iguais ao seu saldo disponível;

 **Conta Corrente (CC):** o usuário pode sacar valores maiores do que o valor 
 atual na conta, desde que esteja dentro de um limite pré-estabelecido.


## Tecnologias Utilizadas

**Python 3.x** 

**Módulo Nativo *abc***

## Estrutura do projeto

```text
├── banco.py       # Classe central de orquestração e validação.
├── clientes.py    # Classes Pessoa e Cliente.
├── contas.py      # Classe abstrata Conta, ContaCorrente e ContaPoupanca.
