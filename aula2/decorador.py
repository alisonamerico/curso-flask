def header(f):
    def wrapper(nome):
        print("### Bem vindo ao meu site ###\n")
        return f(nome)
    return wrapper


def footer(f):
    def wrapper(nome):
        print("### Copyright - 2020 ###\n")
        return f(nome)
    return wrapper


@footer
@header
def produto(nome):
    print(f"Produto: {nome} - R$2K")


produto("Cadeira Gamer")
produto("Teclado Mecanico")

# funcionamento do decorator


def pao(f):
    def wrapper(recheio):
        print("salada")
        f(recheio)
    return wrapper


@pao
def lanche(recheio):
    print(f"{recheio}")
    print("hamburguer")


lanche()
