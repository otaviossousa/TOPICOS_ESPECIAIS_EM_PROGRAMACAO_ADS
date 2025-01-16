"""
Faça um programa que gere uma série de tarefas aleatórias a serem realizadas por um usuário ao longo de uma semana.
A cada tarefa, o programa verifica o tempo que o usuário leva para completá-la e calcula o tempo total gasto ao longo da semana,
além de gerar um relatório estatístico que inclui a média de tempo gasto por tarefa, a maior e a menor duração,
utilizando funções dos módulos datetime, random e math.

tarefas = [
 "Ler um capítulo de livro",
 "Fazer exercício físico",
 "Estudar um novo tópico",
 "Cozinhar uma refeição",
 "Meditar por 30 minutos",
 "Organizar a casa",
 "Assistir a um documentário"

]

Saída:

Iniciando a tarefa: 'Organizar a casa' em 14:32:46

Tempo estimado: 54 minutos...

Tarefa 'Organizar a casa' concluída em 15:22:46

..............................................................................

Iniciando a tarefa: 'Fazer exercício físico' em 14:32:40

Tempo estimado: 49 minutos...

Tarefa 'Fazer exercício físico' concluída em 15:21:40

"""
import datetime as dt
import random as r
import math as m

tarefas = [
    "Ler um capítulo de livro",
    "Fazer exercício físico",
    "Estudar um novo tópico",
    "Cozinhar uma refeição",
    "Meditar por 30 minutos",
    "Organizar a casa",
    "Assistir a um documentário"
]


def gerar_tarefas_semanais(tarefas):
    tarefas_semanais = []
    for _ in range(7):
        tarefa = r.choice(tarefas)
        tempo_estimado = r.randint(30, 60)
        tarefas_semanais.append((tarefa, tempo_estimado))
    return tarefas_semanais


def executar_tarefas(tarefas_semanais):
    tempos_gastos = []
    for tarefa, tempo_estimado in tarefas_semanais:
        hora_inicio = dt.datetime.now()
        print(f"Iniciando a tarefa: '{tarefa}' em {hora_inicio.strftime('%H:%M:%S')}")
        print(f"Tempo estimado: {tempo_estimado} minutos...")


        tempo_gasto = tempo_estimado + r.randint(-5, 5)
        hora_fim = hora_inicio + dt.timedelta(minutes=tempo_gasto)
        print(f"Tarefa '{tarefa}' concluída em {hora_fim.strftime('%H:%M:%S')}")
        print("..............................................................................")

        tempos_gastos.append(tempo_gasto)
    return tempos_gastos


def gerar_relatorio(tempos_gastos):
    total_tempo = sum(tempos_gastos)
    media_tempo = m.fsum(tempos_gastos) / len(tempos_gastos)
    maior_tempo = max(tempos_gastos)
    menor_tempo = min(tempos_gastos)

    print("\nRelatório Estatístico:")
    print(f"Tempo total gasto: {total_tempo} minutos")
    print(f"Média de tempo gasto por tarefa: {media_tempo:.2f} minutos")
    print(f"Maior tempo gasto em uma tarefa: {maior_tempo} minutos")
    print(f"Menor tempo gasto em uma tarefa: {menor_tempo} minutos")


def main():
    tarefas_semanais = gerar_tarefas_semanais(tarefas)
    tempos_gastos = executar_tarefas(tarefas_semanais)
    gerar_relatorio(tempos_gastos)


if __name__ == '__main__':
    main()
