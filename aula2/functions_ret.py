"""
Funções sem o return são chamadas de funções void, ou procedures porque não retornam nada.
Ex.:
"""


# void = função sem retorno
def ola():
    print("Olá")
# A funcao acima executa o print e depois nao faz mais nada, nao tem um retorno.


ola()  # implicitamente retorna None


# funcao com retorno e anotações opcionais de tipos
def soma(a: int, b: int) -> int:
    resultado = a + b
    return resultado


result = soma(5, 5)  # atribuição
print(result)


# High-order functions


def mensagem(header, footer):
    header()
    print("Olá você está no CodeShow")
    footer()


def header():
    print("### inicio")


def footer():
    print("### fim")


mensagem(header=header, footer=footer)
