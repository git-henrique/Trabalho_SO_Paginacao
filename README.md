# Simulador de Substituição de Páginas
_________________________
### O presente projeto implementa um __simulador de substutuição de páginas__ na gerência de memória de um sitema operacional com os algoritmos clássicos, sendo integralmente implementado em ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
_________________________
## Algoritmos do simulador:
- **FIFO** (Fist-In, First-Oout) ✅
- **LRU** (Least Recently Used) ✅
- **Ótimo** ✅
- **Clock** ✅
- **NRU** (Not Recently Used) 🔄
- **LFU** (Least Frequently Used) 🔄
- **MFU** (Most Frequently Used) 🔄

_________________________
## Descrição:
Você pode chamar o simulador a partir do ```shell``` indicando: 

1.  O algoritmo que você quer chmar;
2. A quantidade de frames da simulação;
3. O arquivo trace para ser lido pelo simulador;
4. Se deseja o ```verbose``` com a informações acerca dos frames e paginas finais;

_________________________
## Como utilizar o simulador:
Após baixar todos os arquivos do projeto, faça a seguinte chamada no terminal:

```./pager.py --algo <ALGO> --frames <N> --trace <arquivo> [--verbose] ```

Onde:
- "ALGO" pode ser: `('fifo', 'lru', 'optimal', 'clock', 'nru', 'lfu', 'mfu')`;
- "N" fica a sua escolha;
- "arquivo" deve ser **exatamente** o nome do arquivo trace que deve estar no mesmo diretório que `pager.py`;

**Obs:** Neste projeto há um trace padrão: `silberschatz2001.trace`.

## Exemplo:
```./pager.py --algo lru --frames 3 --trace silberschatz2001.trace --verbose```
_________________________
## Requisitos:
- Python 3.12+