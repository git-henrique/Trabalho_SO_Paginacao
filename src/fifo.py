def fifo(trace, num_frames):
    fila_processos = []
    memoria = set()

    faltas = 0
    eviccoes = 0
    total_referencias = 0

    for pagina in trace:
        total_referencias += 1

        if pagina in memoria:
            continue  # HIT

        # FALTA DE PÁGINA
        faltas += 1

        if len(fila_processos) < num_frames:
            fila_processos.append(pagina)
            memoria.add(pagina)
        else:
            vitima = fila_processos.pop(0)
            memoria.remove(vitima)

            fila_processos.append(pagina)
            memoria.add(pagina)

    eviccoes = faltas
    
    taxa_faltas = (faltas / total_referencias) * 100

    indices = list(range(num_frames))


    return {
        "faltas": faltas,
        "eviccoes": eviccoes,
        "taxa_faltas": taxa_faltas,
        "frame_ids": indices,
        "memoria_final": fila_processos
    }
