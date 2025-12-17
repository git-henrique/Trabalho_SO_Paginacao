# Simulador de Substituição de Páginas
_________________________
### O presente projeto implementa um __simulador de substutuição de páginas__ na gerência de memória de um sitema operacional com os algoritmos clássicos, sendo integralmente implementado em ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
_________________________
## Algoritmos do simulador:
- **FIFO** (First-In, First-Oout) ✅
- **LRU** (Least Recently Used) ✅
- **Ótimo** ✅
- **Clock** ✅
- **NRU** (Not Recently Used) ✅
- **LFU** (Least Frequently Used) ✅
- **MFU** (Most Frequently Used) ✅

_________________________
## Estrutura do projeto

```text
.
├── pager.py
├── README.md
├── silberschatz2001.trace
└── src/
    ├── fifo.py     
    ├── lru.py       
    ├── otimo.py     
    ├── clock.py     
    ├── nru.py      
    ├── lfu.py       
    └── mfu.py       
```
- `pager.py`: programa principal, responsável pela interface de linha de comando e pela seleção do algoritmo.

- `src/`: diretório que contém a implementação de cada algoritmo de substituição de páginas.

- `silberschatz2001.trace`: arquivo de trace utilizado nos testes e validações.

- `README.md`: documentação do projeto.
_________________________
## Como utilizar o simulador:
Após baixar todos os arquivos do projeto, faça a seguinte chamada no terminal:

```bash
./pager.py --algo <ALGO> --frames <N> --trace <arquivo> [--verbose]
```

Onde:
- "ALGO" pode ser: `('fifo', 'lru', 'optimal', 'clock', 'nru', 'lfu', 'mfu')`;
- "N" fica a sua escolha;
- "arquivo" deve ser **exatamente** o nome do arquivo trace que deve estar no mesmo diretório que `pager.py`;
- `--verbose` (opcional) exibe o conjunto residente final

**Obs:** Neste projeto há um trace padrão: `silberschatz2001.trace`.
__________________________
## Exemplo:
```bash
./pager.py --algo lru --frames 3 --trace silberschatz2001.trace --verbose 
```
### Exemplo de saída:

```text
Algoritmo: LRU
Frames: 3
Referências: 20
Faltas de página: 12
Taxa de faltas: 60.00%
Evicções: 12
Conjunto residente final:
frame_ids: 0 1 2
page_ids: 1 0 7
```
_________________________
## Requisitos:
- Python 3.12+