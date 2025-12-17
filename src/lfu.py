def lfu(trace, num_frames):
    frames = [None] * num_frames

    # contador de frequencia de uso
    freq = {}

    faltas = 0

    for pagina in trace:

        # HIT
        if pagina in frames:
            freq[pagina] += 1
            continue

        # PAGE FAULT
        faltas += 1

        # frame livre?
        if None in frames:
            idx = frames.index(None)
            frames[idx] = pagina
            freq[pagina] = 1
        else:
            # escolhe página com menor frequencia
            vitima = min(frames, key=lambda p: freq[p])
            idx = frames.index(vitima)

            freq.pop(vitima)

            frames[idx] = pagina
            freq[pagina] = 1

    eviccoes = faltas
    taxa_faltas = (faltas / len(trace)) * 100

    return {
        "faltas": faltas,
        "eviccoes": eviccoes,
        "taxa_faltas": taxa_faltas,
        "frame_ids": list(range(num_frames)),
        "memoria_final": frames
    }
