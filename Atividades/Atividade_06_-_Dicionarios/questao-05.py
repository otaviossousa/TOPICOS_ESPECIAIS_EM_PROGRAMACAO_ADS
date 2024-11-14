def signo(dia, mes):
    signos = {
        'Capricórnio': ((12, 22), (1, 20)),
        'Aquário': ((1, 21), (2, 18)),
        'Peixes': ((2, 19), (3, 20)),
        'Áries': ((3, 21), (4, 20)),
        'Touro': ((4, 21), (5, 20)),
        'Gêmeos': ((5, 21), (6, 20)),
        'Câncer': ((6, 21), (7, 22)),
        'Leão': ((7, 23), (8, 22)),
        'Virgem': ((8, 23), (9, 22)),
        'Libra': ((9, 23), (10, 22)),
        'Escorpião': ((10, 23), (11, 21)),
        'Sagitário': ((11, 22), (12, 21)),
    }

    for signo, ((mes_inicio, dia_inicio), (mes_fim, dia_fim)) in signos.items():
        if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fim and dia <= dia_fim):
            return signo


print(signo(28, 10))
