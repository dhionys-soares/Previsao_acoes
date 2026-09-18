# 📈 Scanner de Ações B3 — PFR

Aplicação web desenvolvida em **Python + Streamlit** para análise técnica de ações da **B3**, utilizando dados históricos do Yahoo Finance.

O projeto realiza uma varredura de diversos ativos em busca de um padrão definido como **PFR**, combinando esse padrão com indicadores técnicos como **MME 21, MME 50, Estocástico Lento e Volume** para gerar um score de até **5 pontos**.

> ⚠️ **Projeto experimental e educacional.** Os indicadores utilizados não garantem movimentos futuros dos preços e não constituem recomendação de investimento.

---

## 🎯 Objetivo

O projeto foi desenvolvido para estudar e aplicar conceitos de:

* 🐍 Python
* 📊 Análise de dados
* 📈 Análise técnica
* 🔎 Data Scanning
* 🌐 Consumo de dados financeiros
* 📉 Visualização de dados
* 🖥️ Desenvolvimento de dashboards com Streamlit

A aplicação automatiza a análise de uma lista de ações e apresenta somente os ativos que atendem ao padrão PFR definido no código.

---

## 🚀 Funcionalidades

### 🔎 Scanner automático

O sistema percorre uma lista de ações da B3 e busca aquelas que apresentam o padrão PFR.

A lista contém ações de diferentes setores e inclui ativos como:

* PETR4
* VALE3
* ITUB4
* BBAS3
* WEGE3
* MGLU3
* RENT3
* PRIO3
* SUZB3
* GGBR4
* entre diversos outros.

Os tickers são consultados utilizando o formato `.SA`, compatível com o Yahoo Finance.

### 📊 Padrão PFR

O padrão utilizado pelo scanner verifica três condições:

1. O fechamento atual é maior que o fechamento anterior;
2. A mínima atual é menor que a mínima anterior;
3. A mínima atual é menor que a mínima de dois períodos atrás.

Em termos simplificados:

```text
Fechamento atual > Fechamento anterior
        +
Mínima atual < Mínima anterior
        +
Mínima atual < Mínima de 2 períodos atrás
```

Quando essas condições são atendidas, o ativo passa para a etapa de análise dos demais indicadores.

---

## 📐 Indicadores utilizados

### MME 21

A aplicação calcula a **Média Móvel Exponencial de 21 períodos (MME21)**.

Uma das condições do score é:

```text
Preço atual > MME21
```

### MME 50

Também é calculada a **Média Móvel Exponencial de 50 períodos (MME50)**.

A relação entre as duas médias é utilizada como uma condição de tendência:

```text
MME21 > MME50
```

### 📊 Estocástico Lento

O projeto calcula o Estocástico utilizando:

* Período: 14
* Suavização do %K: 3
* Período do %D: 3

A condição considerada positiva ocorre quando:

```text
%K lento > %D
%K lento < 80
```

O dashboard também apresenta as regiões de referência de **sobrecompra (80)** e **sobrevenda (20)**.

### 📦 Volume

É calculada a média de volume dos últimos **20 pregões**.

A condição é considerada positiva quando:

```text
Volume atual > Volume médio de 20 períodos
```

### 📏 ATR 14

O **ATR de 14 períodos** também é calculado e disponibilizado nos dados detalhados da aplicação.

Atualmente, o ATR é utilizado como informação complementar e não participa diretamente do score.

---

## 🧮 Sistema de Score

Cada condição atendida adiciona **1 ponto** ao score.

| Condição             |    Pontuação |
| -------------------- | -----------: |
| PFR                  |           +1 |
| Preço > MME21        |           +1 |
| MME21 > MME50        |           +1 |
| Estocástico          |           +1 |
| Volume > média de 20 |           +1 |
| **Máximo**           | **5 pontos** |

O score é utilizado para organizar os ativos encontrados pelo scanner, facilitando a análise posterior.

> O score é uma métrica criada especificamente para este projeto e não representa uma classificação oficial de ativos.

---

## 📊 Dashboard

A aplicação possui uma interface interativa desenvolvida com **Streamlit**.

### Resumo

O dashboard apresenta:

* quantidade de ações analisadas;
* quantidade de ativos que apresentaram PFR;
* maior score encontrado.

### 🔎 Tabela de sinais

Os ativos encontrados são exibidos em uma tabela contendo:

* Ticker;
* Empresa;
* Preço;
* PFR;
* MME21;
* Tendência;
* Estocástico;
* Volume;
* Score;
* Variação percentual.

Os resultados são ordenados pelo score, do maior para o menor.

### 📈 Análise individual

Após selecionar uma ação, o dashboard apresenta:

* Score;
* Preço atual;
* Variação;
* Estocástico;
* Volume;
* condições que foram ou não atendidas.

---

## 📉 Gráficos

Para cada ativo selecionado são apresentados três gráficos interativos utilizando **Plotly**.

### Candlestick + Médias Móveis

Gráfico de candles contendo:

* Open;
* High;
* Low;
* Close;
* MME21;
* MME50.

### Estocástico

Gráfico contendo:

* %K;
* %D;
* região de sobrecompra;
* região de sobrevenda.

### Volume

Gráfico contendo:

* volume diário;
* média de volume de 20 períodos.

---

## ⚙️ Configurações

O usuário pode configurar diretamente pela barra lateral:

### Período histórico

Opções disponíveis:

```text
3 meses
6 meses
1 ano
2 anos
```

### Quantidade de ações

Também é possível definir a quantidade máxima de ações que serão analisadas pelo scanner.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia    | Utilização                      |
| ------------- | ------------------------------- |
| 🐍 Python     | Linguagem principal             |
| 🖥️ Streamlit | Interface web e dashboard       |
| 🐼 Pandas     | Manipulação e análise dos dados |
| 📊 Plotly     | Gráficos interativos            |
| 📈 yfinance   | Consulta dos dados históricos   |
| 🗓️ datetime  | Controle de data e hora         |

O aplicativo utiliza `yfinance` para consultar o histórico dos ativos e `pandas` para calcular os indicadores técnicos.

---

## 🧱 Estrutura atual

O projeto possui uma estrutura simples, concentrando a aplicação no arquivo principal:

```text
Previsao_acoes/
│
├── app.py
├── README.md
└── .gitignore
```

O `app.py` atualmente concentra:

* configuração do Streamlit;
* lista de ativos;
* consulta dos dados;
* cálculo dos indicadores;
* identificação do PFR;
* cálculo do score;
* criação dos gráficos;
* construção da interface;
* apresentação dos resultados.

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/dhionys-soares/Previsao_acoes.git
```

### 2. Acesse a pasta

```bash
cd Previsao_acoes
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual

No Windows:

```bash
.venv\Scripts\activate
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

### 5. Instale as dependências

```bash
pip install streamlit pandas plotly yfinance
```

### 6. Execute a aplicação

```bash
streamlit run app.py
```

Após iniciar, o Streamlit disponibilizará o dashboard no navegador.

---

## 🔄 Fluxo da aplicação

O funcionamento pode ser resumido da seguinte forma:

```text
Yahoo Finance
      │
      ▼
Coleta dos dados históricos
      │
      ▼
Cálculo dos indicadores
      │
      ├── MME21
      ├── MME50
      ├── Estocástico
      ├── Volume médio
      └── ATR14
      │
      ▼
Identificação do padrão PFR
      │
      ▼
Aplicação das condições
      │
      ▼
Score de 0 a 5
      │
      ▼
Ordenação dos resultados
      │
      ▼
Dashboard Streamlit
      │
      ├── Tabela de sinais
      ├── Indicadores
      ├── Candlestick
      ├── Estocástico
      └── Volume
```

---

## ⚡ Cache de dados

Para reduzir chamadas repetidas ao Yahoo Finance, o projeto utiliza o mecanismo de cache do Streamlit.

Os dados das ações e os resultados do scanner possuem cache com duração de **15 minutos (900 segundos)**.

Isso ajuda a evitar consultas desnecessárias quando a aplicação é executada novamente dentro desse período.

---

## 🧠 Sobre o projeto

Apesar do nome **Previsao_acoes**, o projeto atualmente não utiliza Machine Learning ou modelos estatísticos para realizar uma previsão de preço futuro.

A proposta atual é de **scanner e análise técnica baseada em regras**, identificando ativos que apresentam uma combinação específica de condições.

Essa distinção é importante porque:

> **Identificar um padrão técnico não significa prever com certeza o comportamento futuro de uma ação.**

O projeto foi desenvolvido principalmente como estudo prático de **Python, análise de dados, indicadores técnicos, APIs de dados financeiros e construção de aplicações interativas**.

---

## 🔮 Próximas melhorias

Algumas evoluções possíveis para o projeto:

* [ ] Separar a lógica de negócio do `app.py`;
* [ ] Criar módulos específicos para coleta e análise;
* [ ] Adicionar arquivo `requirements.txt`;
* [ ] Adicionar testes automatizados;
* [ ] Melhorar o tratamento de erros do Yahoo Finance;
* [ ] Permitir pesquisa manual de qualquer ticker;
* [ ] Adicionar outros indicadores técnicos;
* [ ] Criar backtesting das condições utilizadas;
* [ ] Registrar o histórico dos sinais encontrados;
* [ ] Criar gráficos comparativos entre ativos;
* [ ] Adicionar filtros por setor;
* [ ] Criar uma versão com configuração externa dos parâmetros;
* [ ] Avaliar modelos estatísticos ou de Machine Learning separadamente da estratégia baseada em regras.

---

## 📚 Aprendizados

Este projeto representa uma aplicação prática de conceitos de desenvolvimento e análise de dados, incluindo:

* consumo de dados externos;
* tratamento de DataFrames;
* cálculo de indicadores com Pandas;
* funções e modularização;
* cache de dados;
* construção de interfaces com Streamlit;
* visualização de séries temporais;
* gráficos financeiros com Plotly;
* criação de regras para classificação de dados;
* ordenação e filtragem de resultados;
* manipulação de exceções;
* desenvolvimento de uma aplicação de análise de dados de ponta a ponta.

---

## ⚠️ Disclaimer

Este projeto possui finalidade **educacional e experimental**.

As informações, indicadores, scores e padrões apresentados pela aplicação não constituem recomendação de compra ou venda de ativos financeiros.

O mercado financeiro envolve riscos, e resultados históricos ou padrões identificados não garantem resultados futuros.

---

## 👨‍💻 Autor

**Dhionys Soares**

Desenvolvedor em formação com foco em desenvolvimento de software, Python, análise de dados e tecnologias do ecossistema .NET.

🔗 **GitHub:** [dhionys-soares](https://github.com/dhionys-soares)

---

⭐ Se este projeto foi útil para você, considere deixar uma estrela no repositório.
