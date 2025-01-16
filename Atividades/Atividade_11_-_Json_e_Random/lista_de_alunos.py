"""
Cenário
Criaremos um sistema que simula uma lista de alunos com notas geradas aleatoriamente e, com base na média,
classifica os alunos em "Aprovado" ou "Reprovado". O sistema também registra a data de avaliação.

Passo a Passo
Crie o dicionário base com os dados dos alunos.
Transforme Dicionário em Json
Use o random para gerar as notas.
Calcule a média com math.
Registre a data da avaliação usando datetime.
Classifique os alunos com base na média.
"""

import json
import datetime as dt
import random as r

alunos = {
    "Joao": {"notas": [], "media": 0, "situacao": ""},
    "Maria": {"notas": [], "media": 0, "situacao": ""},
    "Jose": {"notas": [], "media": 0, "situacao": ""},
    "Ana": {"notas": [], "media": 0, "situacao": ""},
    "Carlos": {"notas": [], "media": 0, "situacao": ""}
}

for aluno in alunos:
    for i in range(4):
        alunos[aluno]["notas"].append(r.randint(0, 10))
        
    alunos[aluno]["media"] = sum(alunos[aluno]["notas"]) / 4

    if alunos[aluno]["media"] >= 6:
        alunos[aluno]["situacao"] = "Aprovado"
    else:
        alunos[aluno]["situacao"] = "Reprovado"

data = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


with open("alunos.json", "w") as file:
    json.dump(alunos, file, indent=4)


print(f"Data da avaliação: {data}")

for aluno in alunos:
    print(f"Aluno: {aluno}")
    print(f"Notas: {alunos[aluno]['notas']}")
    print(f"Média: {alunos[aluno]['media']}")
    print(f"Situacao: {alunos[aluno]['situacao']}\n")

