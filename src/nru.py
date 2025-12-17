def nru(trace, num_frames):
    frames = [None] * num_frames

    faltas = 0

    # bit de referencia para cada frame
    ref_bits = [0] * num_frames

    for pagina in trace:

        # HIT
        if pagina in frames:
            idx = frames.index(pagina)
            ref_bits[idx] = 1
            continue

        # FALTA DE PÁGINA
        faltas += 1

        # frame livre?
        if None in frames:
            idx = frames.index(None)
            frames[idx] = pagina
            ref_bits[idx] = 1
        else:
            # procura página não referenciada (R=0)
            vitima_idx = None

            for i in range(num_frames):
                if ref_bits[i] == 0:
                    vitima_idx = i
                    break

            # se todas foram referenciadas, pega a primeira
            if vitima_idx is None:
                vitima_idx = 0
                # reseta todos os bits
                ref_bits = [0] * num_frames

            frames[vitima_idx] = pagina
            ref_bits[vitima_idx] = 1

    eviccoes = faltas
    taxa_faltas = (faltas / len(trace)) * 100

    return {
        "faltas": faltas,
        "eviccoes": eviccoes,
        "taxa_faltas": taxa_faltas,
        "frame_ids": list(range(num_frames)),
        "memoria_final": frames
    }
