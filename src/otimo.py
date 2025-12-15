def otimo(trace, num_frames):
    fila_processos = []
    memoria = set()

    faltas = 0
    eviccoes = 0

    # guarda i para olhar pro futuro
    for i, pagina in enumerate(trace):

        if pagina in memoria:
            continue # aqui é HIT

        faltas += 1

        if len(fila_processos) < num_frames:
            fila_processos.append(pagina)
            memoria.add(pagina)
            continue

        futuro = trace[i+1:]

        pagina_vitima = None
        uso_mais_distante = -1

        # escolha do processo p mais longe ou que não será mais usado
        for p in fila_processos:
            if p not in futuro:
                pagina_vitima = p
                break
            else:
                proximo_uso = futuro.index(p)
                if proximo_uso > uso_mais_distante:
                    uso_mais_distante = proximo_uso
                    pagina_vitima = p

        fila_processos.remove(pagina_vitima)
        memoria.remove(pagina_vitima)

        fila_processos.append(pagina)
        memoria.add(pagina)

    eviccoes = faltas

    taxa_faltas = (faltas/len(trace)) * 100

    indices = list(range(num_frames))

    return {
        "faltas": faltas,
        "eviccoes": eviccoes,
        "taxa_faltas": taxa_faltas,
        "frame_ids": indices,
        "memoria_final": fila_processos
    }