# NYC Taxi Data Pipeline


Este projeto tem como objetivo criar um pipeline de dados para obter, processar e analisar dados de corridas de táxi amarelo de Nova York. Utilizando tecnologias como Docker, Python e bibliotecas de manipulação de dados, o pipeline baixa os dados, processa-os para remover inconsistências e gera métricas específicas, que são então salvas em arquivos CSV.

## Objetivos
* Obtenção de Dados: Baixar dados de corridas de táxi amarelo de Nova York a partir de um repositório público.
* Processamento de Dados: Processar os dados para remover inconsistências e preparar para análise.
* Geração de Métricas: Calcular e salvar métricas específicas em arquivos CSV.
Métricas Calculadas
Total Acumulado de Viagens por Mês:

Calcula o total de corridas realizadas em cada mês.
Distância Média de Viagem por Mês:

Calcula a distância média de viagem para cada mês, incluindo uma métrica de Média Móvel de 3 Meses.
Porcentagem da Receita Total por Mês:

Calcula a porcentagem da receita total mensal em relação à receita anual total.

## Descrição dos Componentes
* Dockerfile: Define o ambiente Docker para garantir a reprodutibilidade do pipeline.

* requirements.txt: Lista as dependências necessárias para rodar o projeto.

* src/main.py: Ponto de entrada principal do pipeline que coordena o download, processamento e geração de métricas.
src/download_data.py: Script responsável por baixar os dados de táxi de Nova York.

* src/process_data.py: Script responsável por processar os dados baixados, removendo inconsistências.

* src/save_data.py: Script responsável por calcular e salvar as métricas em arquivos CSV.

* data/: Diretório onde os arquivos de dados e métricas serão armazenados

## Como rodar o projeto

### Pré-requisitos

- Docker instalado

### Passos

1. Construa a imagem Docker:
    ```sh
    docker build -t nyc_taxi_pipeline .
    ```

2. Rode o contêiner Docker:
    ```sh
    docker run -v $(pwd)/data:/app/data nyc_taxi_pipeline
    ```

Os arquivos Parquet processados serão salvos na pasta `data/parquet`.

## Estrutura do Projeto

nyc_taxi_pipeline/
│
├── Dockerfile
├── README.md
├── requirements.txt
├── src/
│   ├── main.py
│   ├── download_data.py
│   ├── process_data.py
│   └── save_data.py
└── data/

