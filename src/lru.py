def lru(trace, num_frames):
    # frames físicos (ordem fixa)
    frames = [None] * num_frames

    # marca o último uso de cada página
    last_used = {}

    faltas = 0
    eviccoes = 0
    tempo = 0

    for pagina in trace:
        tempo += 1

        # HIT
        if pagina in frames:
            last_used[pagina] = tempo
            continue

        # PAGE FAULT
        faltas += 1

        # Frame livre?
        if None in frames:
            idx = frames.index(None)
            frames[idx] = pagina
            last_used[pagina] = tempo
        else:
            # escolher a página menos recentemente usada
            vitima = min(frames, key=lambda p: last_used[p])
            idx = frames.index(vitima)

            frames[idx] = pagina
            last_used.pop(vitima)

            last_used[pagina] = tempo

    eviccoes = faltas
    taxa_faltas = (faltas / len(trace)) * 100

    return {
        "faltas": faltas,
        "eviccoes": eviccoes,
        "taxa_faltas": taxa_faltas,
        "frame_ids": list(range(num_frames)),
        "memoria_final": frames
    }
