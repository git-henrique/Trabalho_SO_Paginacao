#!/usr/bin/env python3

import argparse

from src.fifo import fifo
from src.lru import lru
from src.otimo import otimo
from src.clock import clock

def load_trace(filename):
    trace = []
    with open(filename) as f:
        for line in f:
            trace.append(int(line.strip()))
    return trace


def main():
    #configuração da chamada no terminal
    parser = argparse.ArgumentParser(
        description="Simulador de algoritmos de substituição de páginas"
    )

    parser.add_argument("--algo", required=True,
                        choices=["fifo", "lru", "optimal", "clock", "second", "nru", "lfu", "mfu"],
                        help="Algoritmo de substituição")

    parser.add_argument("--frames", required=True, type=int,
                        help="Número de molduras de página")

    parser.add_argument("--trace", required=True,
                        help="Arquivo de trace")

    parser.add_argument("--verbose", action="store_true",
                        help="Modo verboso")

    args = parser.parse_args()

    trace = load_trace(args.trace)

    if args.algo == "fifo":
        result = fifo(trace, args.frames)

    elif args.algo == "lru":
        result = lru(trace, args.frames)

    elif args.algo == "optimal":
        result = otimo(trace, args.frames)

    elif args.algo == "clock":
        result = clock(trace, args.frames)


    else:
        print("Algoritmo ainda não implementado.")
        return

    print(f"Algoritmo: {args.algo.upper()}")
    print(f"Frames: {args.frames}")
    print(f"Referências: {len(trace)}")
    print(f"Faltas de página: {result['faltas']}")
    print(f"Taxa de faltas: {result['taxa_faltas']:.2f}%")
    print(f"Evicções: {result['eviccoes']}")

    if args.verbose:
        print("Conjunto residente final:")
        print("frame_ids:", " ".join(map(str, result["frame_ids"])))
        print("Page_ids:", " ".join(map(str, result["memoria_final"])))


if __name__ == "__main__":
    main()
