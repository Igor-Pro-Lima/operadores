idade: int
salario: float
nome: str
sexo: str

idade = 24
salario = 5000.55
nome = "Igor Lima"
sexo = "M"

print(f"O funcionário {nome}, sexo {sexo}, ganha {salario}, e tem {idade} anos")

# Segunda opção colocando os placeholders
print("O funcionario {:s}, sexo {:s}, ganha {:.2f}, e tem {:d} anos".format(nome, sexo, salario, idade ))