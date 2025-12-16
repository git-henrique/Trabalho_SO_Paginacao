def clock(trace, num_frames):
    frames = [None] * num_frames

    faltas = 0

    ref_bits = [0] * num_frames
    ponteiro = 0

    for pagina in trace:

        if pagina in frames:
            idx = frames.index(pagina)
            ref_bits[idx] = 1
            continue

        # falta de pagina
        faltas += 1

        if None in frames:
            idx =  frames.index(None)
            frames[idx] = pagina
            ref_bits[idx] = 1
        else:
            #clock
            while ref_bits[ponteiro] == 1:
                ref_bits[ponteiro] = 0
                ponteiro = (ponteiro + 1) % num_frames

            # substituicao
            frames[ponteiro] = pagina
            ref_bits[ponteiro] = 1
            ponteiro = (ponteiro +1) % num_frames

    
    taxa_faltas = (faltas/len(trace)) * 100

    eviccoes = faltas

    return {
        "faltas": faltas,
        "eviccoes": eviccoes,
        "taxa_faltas": taxa_faltas,
        "frame_ids": list(range(num_frames)),
        "memoria_final": frames
    }
