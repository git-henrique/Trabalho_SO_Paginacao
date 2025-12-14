def lru(trace, num_frames):
    # agora a lista guarda de acordo com o uso, inicio tem a menos recente
    # e o fim da lista é a mais recente usada
    lista_uso = []
    memoria = set()

    faltas = 0
    eviccoes = 0
    total_referencias = 0

    for pagina in trace:
        total_referencias += 1

        # HIT
        if pagina in memoria:
            lista_uso.remove(pagina)
            lista_uso.append(pagina)
            continue

        #contagem de faltas
        faltas += 1

        if len(lista_uso) < num_frames:
            lista_uso.append(pagina)
            memoria.add(pagina)
        else:
            # removendo a menos recente usada
            vitima = lista_uso.pop(0)
            memoria.remove(vitima)
            eviccoes += 1

            lista_uso.append(pagina)
            memoria.add(pagina)

    taxa_faltas = (faltas/total_referencias) * 100

    return {
        "faltas": faltas,
        "eviccoes": eviccoes,
        "taxa_faltas": taxa_faltas,
        "memoria_final": lista_uso
    }

        