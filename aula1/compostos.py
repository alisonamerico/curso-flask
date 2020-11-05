# Listas - são mutáveis

# indices     0         1       2
cores = ["vermelho", "verde", "azul"]
numeros = [1, 2, 3]
mistura = [1, "alison", 4.5, True, cores, numeros, [1, 2, 3]]

cores.append("amArelo")
cores.insert(1, "branco")
cores.remove("azul")
print(cores)


# Tuplas - são imutáveis
#                0            0        2
identidade = ("Alison", "456789456-9", 15)

print(f"Nome: {identidade[0]}")
print(f"CPF: {identidade[1]}")
print(f"Idade: {identidade[2]}")

# desenpacotamento p/ tuplas
nome, cpf, idade = identidade
print(nome, cpf, idade)


# Dicionario - sao mutaveis
# em outras linguagens o dicionário é chamado de: Array, Assciativo, HashMap, Object

pessoa = {
    "nome": "Karla",
    "cpf": "698126741-8",
    "idade": 18,
    "cores_preferidas": cores,
    "numeros_preferidos": numeros
}

# inserir ou mudar um campo no dicionario
pessoa["idade"] = 19
pessoa["canal"] = "@KarlaMag"

print(f"Olá, a {pessoa['nome']}, tem {pessoa['idade']} anos.")

# Iteracao (pegar um elemento de cada vez)

for cor in cores:
    print(cor.upper())

for letra in "Gabriel":
    if letra == "i":
        continue
    print(letra)

# Comprehension (serve para lista, tupla e dicionario)

# List Comprehension
print([letra for letra in "Gabriel"])

# List Comprehension filtrada
print([letra for letra in "Gabriel" if letra != "i"])


for chave in pessoa:
    print(chave, ":", pessoa[chave])

# faz a mesma coisa do exemplo acima, só que melhor
for chave, valor in pessoa.items():
    print(chave, ":", valor)
