# 📊 Desafio 4 — Limpeza e Análise de Dados de Clientes Bancários

Este projeto foi desenvolvido como parte da Trilha 2B e tem como objetivo aplicar técnicas de **limpeza de dados**, **análise exploratória** e **estatística descritiva** sobre uma base de clientes de um banco que atua em estados do Nordeste brasileiro.

📁 Repositório: [matheusvazdata/desafio-4-trilhas-2b](https://github.com/matheusvazdata/desafio-4-trilhas-2b)

## 🧰 Tecnologias Utilizadas

- Python 3.10+
- Pandas e NumPy
- Seaborn e Matplotlib
- Jupyter Notebook
- Docker (ambiente isolado)
- VSCode (com WSL)

## 📁 Estrutura do Projeto

```

├── data/
│   └── clientes\_banco.csv      # Arquivo bruto de entrada
├── notebooks/
│   └── analise\_dados.ipynb     # Notebook principal com todo o pipeline
├── relatorio/                   
    └── relatorio_final.md       # Relatório final
├── src/
│   ├── limpeza.py               # Funções de tratamento e padronização
│   ├── estatisticas.py          # Funções para cálculo de médias, medianas, perfis
│   └── visualizacoes.py         # Funções para geração de gráficos
├── .gitignore
├── Dockerfile                   # Imagem com ambiente de execução
├── requirements.txt             # Bibliotecas e versões utilizadas
└── README.md                    # Documentação principal

````

## ⚙️ Como Executar

### ✅ Usando Docker (recomendado)

```bash
docker build -t desafio4 .
docker run -p 8888:8888 desafio4
````

### ✅ Manualmente (ambiente local)

1. Clone o repositório:

```bash
git clone https://github.com/matheusvazdata/desafio-4-trilhas-2b.git
cd desafio-4-trilhas-2b
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Inicie o notebook:

```bash
jupyter notebook notebooks/analise_dados.ipynb
```

## 🔎 Etapas do Projeto

* **Leitura e padronização dos dados**
* **Tratamento de nulos, outliers e duplicatas**
* **Correção de colunas categóricas (como gênero e estado)**
* **Exploração visual com gráficos categóricos e numéricos**
* **Cálculo de médias e medianas segmentadas**
* **Identificação dos principais perfis de churn (clientes que saíram)**
* **Conclusões e próximos passos estratégicos**

## 👨‍💼 Principais Insights

* Embora o estado do **Piauí (PI)** concentre o maior número de clientes no banco, o **Maranhão (MA)** apresentou a maior **proporção de evasão** relativa ao seu total de clientes, indicando um possível problema regional mais severo.
* Clientes do gênero **feminino** apresentaram **maior frequência de saída** em comparação ao masculino, mesmo sendo minoria na base.
* A **idade mediana dos clientes que saíram** foi próxima de **45 anos**, o que indica que a evasão não está concentrada apenas entre jovens ou idosos.
* O **saldo médio dos clientes que saíram** foi **ligeiramente superior** ao dos que permaneceram, sinalizando que nem sempre a retenção está ligada ao potencial financeiro imediato.
* A análise de **correlação entre variáveis numéricas** não revelou nenhum fator fortemente associado à saída, sugerindo a necessidade de considerar variáveis qualitativas ou externas.

> Esses padrões devem servir de base para hipóteses futuras, ações de retenção e construção de modelos de previsão de churn.

## 📌 Próximos Passos

* Investigar causas da evasão com variáveis não incluídas no dataset, como tempo de conta, interações ou reclamações.
* Avaliar se campanhas personalizadas poderiam reter grupos mais propensos a sair.
* Treinar modelos de machine learning com base nas features limpas para prever evasão futura (churn prediction).
* Construir dashboards para acompanhamento em tempo real com base em indicadores validados.

## 📚 Referências

* [Pandas Documentation](https://pandas.pydata.org/)
* [Seaborn Documentation](https://seaborn.pydata.org/)
* [NumPy Documentation](https://numpy.org/)
* [Matplotlib Docs](https://matplotlib.org/stable/users/explain/quick_start.html)
