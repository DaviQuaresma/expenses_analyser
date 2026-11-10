# Analisador de Despesas em Python

Aplicação de linha de comando (CLI) desenvolvida em Python para leitura, validação e análise de despesas financeiras armazenadas em arquivos CSV.

O projeto recebe um arquivo CSV, valida seus registros, realiza cálculos estatísticos e apresenta um relatório consolidado das despesas no terminal.

Este projeto faz parte de uma trilha prática de estudos (*Build to Learn*), com foco no desenvolvimento da lógica de programação e na aplicação dos recursos nativos do Python, sem utilização de frameworks ou bibliotecas externas.

## Funcionalidades

- **Leitura de CSV:** importa transações financeiras utilizando o módulo `csv`.
- **Validação de dados:** verifica campos obrigatórios, formatos de data e valores monetários.
- **Tratamento de registros inválidos:** identifica registros inconsistentes e registra informações sobre os erros encontrados.
- **Conversão de dados:** transforma datas em objetos `date` e valores monetários em `Decimal`.
- **Análise de despesas:** calcula o total, a média e os valores agrupados por categoria.
- **Identificação de maior valor:** identifica a categoria com o maior volume acumulado de despesas.
- **Relatório no terminal:** apresenta estatísticas, categorias e registros inválidos.
- **Testes automatizados:** utiliza `unittest` para verificar funções de análise e validação.

## Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python 3.10+ | Linguagem principal |
| `csv` | Leitura de arquivos CSV |
| `datetime` | Conversão e validação de datas |
| `decimal` | Operações com valores monetários |
| `pathlib` | Manipulação de caminhos de arquivos |
| `argparse` | Argumentos de linha de comando |
| `unittest` | Testes automatizados |
| Git | Controle de versão |

O projeto utiliza exclusivamente módulos da biblioteca padrão do Python, sem dependências externas.

## Estrutura do projeto

```text
expenses_analyser/
│
├── data/
│   └── despesas.csv
│
├── src/
│   ├── __init__.py
│   ├── analyser.py
│   ├── main.py
│   ├── reader.py
│   ├── report.py
│   └── validator.py
│
├── tests/
│   ├── __init__.py
│   ├── test_analyser.py
│   └── test_validator.py
│
├── .gitignore
├── Makefile
├── requirements.txt
└── README.md
```

### Organização dos módulos

| Arquivo | Responsabilidade |
|---|---|
| `reader.py` | Localiza e realiza a leitura do arquivo CSV. |
| `validator.py` | Valida os registros, converte os dados e identifica inconsistências. |
| `analyser.py` | Agrupa despesas por categoria e calcula estatísticas. |
| `report.py` | Apresenta os resultados e os erros no terminal. |
| `main.py` | Coordena o fluxo de execução da aplicação. |
| `test_analyser.py` | Testa as funcionalidades de análise. |
| `test_validator.py` | Testa as funções de validação. |

## Formato do arquivo CSV

A aplicação espera um arquivo CSV contendo as seguintes colunas:

```csv
data,descricao,categoria,valor
2026-10-01,Supermercado,Alimentacao,250.90
2026-10-02,Combustivel,Transporte,180.00
2026-10-03,Internet,Moradia,120.00
2026-10-04,Restaurante,Alimentacao,75.50
2026-10-05,Aplicativo de transporte,Transporte,32.00
2026-10-06,Farmacia,Saude,48.90
```

**Regras de entrada:**

- `data`: formato `AAAA-MM-DD`.
- `descricao`: descrição não vazia.
- `categoria`: categoria não vazia.
- `valor`: valor monetário convertido para `Decimal`, aceitando vírgula ou ponto como separador decimal.

## Instalação e execução

### 1. Clonar o repositório

```bash
git clone https://github.com/DaviQuaresma/expenses_analyser
cd expenses_analyser
```

### 2. Criar ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual

**Linux / macOS:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Executar a aplicação

A aplicação recebe o caminho do arquivo CSV como argumento obrigatório.

```bash
python -m src.main data/despesas.csv
or
make run
```

O caminho do arquivo é relativo ao diretório em que o comando é executado.

## Exemplo de relatório

Considerando o arquivo CSV de exemplo, a aplicação apresenta um relatório semelhante a este:

```text
==============================================
           RELATORIO DE DESPESAS
==============================================

Transacoes válidas: 6
Transacoes inválidas: 0

Total de despesas: R$ 707.30
Media por transacao: R$ 117.88
Maior despesa: R$ 326.40

----------------------------------
DESPESAS POR CATEGORIA
----------------------------------
Alimentacao => R$ 326.40
Transporte => R$ 212.00
Moradia => R$ 120.00
Saude => R$ 48.90

----------------------------------
ERROS
----------------------------------

==============================================
```

Os valores são exemplos ilustrativos. A maior despesa representa o maior total acumulado entre as categorias.

## Executando os testes

O projeto utiliza o módulo `unittest` para executar testes automatizados.

Na raiz do projeto, execute:

```bash
python -m unittest discover -s tests -ve
or
make test
```

Os testes verificam funções relacionadas à conversão de datas, interpretação de valores monetários e identificação do maior valor entre as categorias.

## Conceitos praticados

Durante o desenvolvimento deste projeto, foram aplicados conceitos fundamentais de Python:

- Manipulação de listas e dicionários.
- Estruturas de repetição e condicionais.
- Funções e separação de responsabilidades.
- Manipulação e conversão de tipos de dados.
- Tratamento de exceções.
- Manipulação de arquivos CSV.
- Manipulação de datas.
- Precisão em operações monetárias com `Decimal`.
- Argumentos de linha de comando.
- Organização de módulos e pacotes.
- Testes automatizados com `unittest`.

---

**Projeto prático**

Desenvolvido com foco em aprendizado, prática de programação, estruturas de dados e consolidação dos fundamentos da linguagem Python.