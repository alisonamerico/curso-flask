def ola(nome, cpf, idade=0, maiusculo=False):
    if maiusculo:
        msg = f"Olá, {nome}".upper()
    else:
        msg = f"Olá, {nome}, {cpf}, idade: {idade}"

    print(msg)


pessoa = ['Karla', '987756432-12', 18]  # banco de dados

ola(*pessoa)

pessoa = {
    'nome': 'karla',
    'cpf': '987654324-89',
    'idade': 18
}

ola(**pessoa)

ola("Grad", "987654324-89")
ola("Karla", "987654324-89")
ola("Lysandro", "987654324-89")
