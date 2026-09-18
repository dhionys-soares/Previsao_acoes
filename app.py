import datetime as dt
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import yfinance as yf


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="Scanner PFR - B3",
    page_icon="📈",
    layout="wide",
)

TICKERS = list(dict.fromkeys([
    "PETR4.SA", "VALE3.SA", "ITUB4.SA", "BBDC4.SA", "BBAS3.SA",
    "ABEV3.SA", "B3SA3.SA", "ITSA4.SA", "WEGE3.SA", "MGLU3.SA",
    "RENT3.SA", "LREN3.SA", "RADL3.SA", "PRIO3.SA", "SUZB3.SA",
    "GGBR4.SA", "CSNA3.SA", "USIM5.SA", "CMIG4.SA", "CPLE3.SA",
    "SBSP3.SA", "VIVT3.SA", "TIMS3.SA", "EQTL3.SA", "ENGI11.SA",
    "TAEE11.SA", "EGIE3.SA", "ENEV3.SA", "VBBR3.SA", "UGPA3.SA",
    "RAIZ4.SA", "CSAN3.SA", "RAIL3.SA", "RECV3.SA", "BRAV3.SA",
    "PETR3.SA", "EMBJ3.SA", "AZUL3.SA", "CVCB3.SA", "AZZA3.SA",
    "ALPA4.SA", "VIVA3.SA", "GRND3.SA", "POMO4.SA", "RAPT4.SA",
    "TUPY3.SA", "LEVE3.SA", "FRAS3.SA", "RANI3.SA", "KLBN11.SA",
    "DXCO3.SA", "CMIN3.SA", "BRAP4.SA", "BRKM5.SA", "UNIP6.SA",
    "FESA4.SA", "JSLG3.SA", "TGMA3.SA", "MILS3.SA", "ARML3.SA",
    "KEPL3.SA", "ROMI3.SA", "INTB3.SA", "ALLD3.SA", "POSI3.SA",
    "WHRL4.SA", "SHUL4.SA", "TASA4.SA", "EALT4.SA", "MTSA4.SA",
    "MWET4.SA", "MDIA3.SA", "CAML3.SA", "SLCE3.SA", "AGRO3.SA",
    "TTEN3.SA", "SMTO3.SA", "SOJA3.SA", "JALL3.SA", "AGXY3.SA",
    "LAND3.SA", "VITT3.SA", "BEEF3.SA", "MBRF3.SA", "MRVE3.SA",
    "CYRE3.SA", "EZTC3.SA", "DIRR3.SA", "TEND3.SA", "CURY3.SA",
    "PLPL3.SA", "EVEN3.SA", "LAVV3.SA", "TRIS3.SA", "MTRE3.SA",
    "MDNE3.SA", "MELK3.SA", "HBOR3.SA", "HBSA3.SA", "LOGG3.SA",
    "LPSB3.SA", "PDGR3.SA", "TCSA3.SA", "GFSA3.SA", "SCAR3.SA",
    "VIVR3.SA", "AVLL3.SA", "ALOS3.SA", "MULT3.SA", "IGTI11.SA",
    "JHSF3.SA", "PCAR3.SA", "ASAI3.SA", "GMAT3.SA", "CEAB3.SA",
    "BHIA3.SA", "AMER3.SA", "LJQQ3.SA", "AMAR3.SA", "WEST3.SA",
    "CASH3.SA", "ENJU3.SA", "SMFT3.SA", "HYPE3.SA", "RDOR3.SA",
    "HAPV3.SA", "FLRY3.SA", "DASA3.SA", "MATD3.SA", "ONCO3.SA",
    "QUAL3.SA", "SAUD3.SA", "AALR3.SA", "VVEO3.SA", "PNVL3.SA",
    "PGMN3.SA", "DMVF3.SA", "PFRM3.SA", "BLAU3.SA", "BIOM3.SA",
    "OFSA3.SA", "SEER3.SA", "YDUQ3.SA", "COGN3.SA", "TOTS3.SA",
    "LWSA3.SA", "DESK3.SA", "FIQE3.SA", "BMOB3.SA", "IFCM3.SA",
    "CSUD3.SA", "BRST3.SA", "TELB3.SA", "WDCN3.SA", "PDTC3.SA",
    "ATED3.SA", "VAMO3.SA", "MOVI3.SA", "SIMH3.SA", "MOTV3.SA",
    "ECOR3.SA", "PASS3.SA", "GGPS3.SA", "LOGN3.SA", "ALPK3.SA",
    "TPIS3.SA", "OPCT3.SA", "SEQL3.SA", "RCSL4.SA", "PMAM3.SA",
    "BRBI11.SA", "PSSA3.SA", "CXSE3.SA", "BBSE3.SA", "SANB11.SA",
    "BBDC3.SA", "ITUB3.SA", "BPAC11.SA", "ABCB4.SA", "BMGB4.SA",
    "BRSR6.SA", "BEES3.SA", "BMEB4.SA", "BSLI4.SA", "BAZA3.SA",
    "BNBR3.SA", "PINE4.SA", "BMIN4.SA", "WIZC3.SA", "IRBR3.SA",
    "ALUP11.SA", "AURE3.SA", "CPFE3.SA", "ISAE4.SA", "SAPR11.SA",
    "CSMG3.SA", "AFLT3.SA", "CLSC4.SA", "CEBR3.SA", "CEEB3.SA",
    "CEED3.SA", "CGAS5.SA", "GEPA4.SA", "EMAE4.SA", "EQMA3B.SA",
    "ENMT3.SA", "ENMT4.SA", "REDE3.SA", "ORVR3.SA", "AMBP3.SA",
    "GOAU4.SA", "CBAV3.SA", "DEXP3.SA", "ETER3.SA", "FHER3.SA",
    "INEP3.SA", "NORD3.SA", "BALM3.SA", "MNPR3.SA", "CRPG5.SA",
    "PTBL3.SA", "EUCA4.SA", "DOHL4.SA", "CTKA4.SA", "CEDO4.SA",
    "CAMB3.SA", "HAGA4.SA", "SHOW3.SA", "MEAL3.SA", "BMKS3.SA",
    "MNDL3.SA", "PLAS3.SA", "MYPK3.SA", "WLMM3.SA", "WLMM4.SA",
    "BDLL4.SA", "SOND5.SA", "OSXB3.SA", "HOOT4.SA", "NEXP3.SA",
    "JFEN3.SA", "RNEW3.SA", "OIBR3.SA", "DTCY3.SA", "GSHP3.SA",
    "AZTE3.SA", "FICT3.SA", "AERI3.SA", "AUAU3.SA", "VULC3.SA",
]))

NOMES = {
    "PETR4.SA": "Petrobras",
    "VALE3.SA": "Vale",
    "ITUB4.SA": "Itaú Unibanco",
    "BBDC4.SA": "Banco Bradesco",
    "BBAS3.SA": "Banco do Brasil",
    "ABEV3.SA": "Ambev",
    "WEGE3.SA": "WEG",
    "MGLU3.SA": "Magazine Luiza",
    "RENT3.SA": "Localiza",
    "LREN3.SA": "Lojas Renner",
    "PRIO3.SA": "PRIO",
    "SUZB3.SA": "Suzano",
    "GGBR4.SA": "Gerdau",
    "CSNA3.SA": "CSN",
    "CMIG4.SA": "Cemig",
    "CPLE3.SA": "Copel",
    "SBSP3.SA": "Sabesp",
    "VIVT3.SA": "Vivo",
    "TIMS3.SA": "TIM",
    "EQTL3.SA": "Equatorial Energia",
    "TAEE11.SA": "Taesa",
    "EGIE3.SA": "Engie",
    "ENEV3.SA": "Eneva",
    "VBBR3.SA": "Vibra Energia",
    "UGPA3.SA": "Ultrapar",
    "RAIL3.SA": "Rumo",
    "EMBJ3.SA": "Embraer",
    "AZUL3.SA": "Azul",
    "CVCB3.SA": "CVC",
    "ALPA4.SA": "Alpargatas",
    "GRND3.SA": "Grendene",
    "POMO4.SA": "Marcopolo",
    "TUPY3.SA": "Tupy",
    "LEVE3.SA": "Mahle Metal Leve",
    "FRAS3.SA": "Fras-le",
    "KLBN11.SA": "Klabin",
    "CMIN3.SA": "CSN Mineração",
    "BRAP4.SA": "Bradespar",
    "BRKM5.SA": "Braskem",
    "UNIP6.SA": "Unipar",
    "FESA4.SA": "Ferbasa",
    "ROMI3.SA": "Indústrias Romi",
    "INTB3.SA": "Intelbras",
    "TASA4.SA": "Taurus",
    "MRVE3.SA": "MRV",
    "CYRE3.SA": "Cyrela",
    "EZTC3.SA": "EZTEC",
    "DIRR3.SA": "Direcional",
    "CURY3.SA": "Cury",
    "MULT3.SA": "Multiplan",
    "JHSF3.SA": "JHSF",
    "ASAI3.SA": "Assaí",
    "GMAT3.SA": "Grupo Mateus",
    "AMER3.SA": "Americanas",
    "HYPE3.SA": "Hypera",
    "RDOR3.SA": "Rede D'Or",
    "HAPV3.SA": "Hapvida",
    "FLRY3.SA": "Fleury",
    "TOTS3.SA": "TOTVS",
    "LWSA3.SA": "Locaweb",
    "VAMO3.SA": "Grupo Vamos",
    "MOVI3.SA": "Movida",
    "SIMH3.SA": "Simpar",
    "PSSA3.SA": "Porto Seguro",
    "BBSE3.SA": "BB Seguridade",
    "SANB11.SA": "Santander Brasil",
    "BPAC11.SA": "BTG Pactual",
    "IRBR3.SA": "IRB Brasil RE",
    "ALUP11.SA": "Alupar",
    "AURE3.SA": "Auren Energia",
    "CPFE3.SA": "CPFL Energia",
    "SAPR11.SA": "Sanepar",
    "CSMG3.SA": "COPASA",
}


# ============================================================
# FUNÇÕES
# ============================================================

@st.cache_data(ttl=900, show_spinner=False)
def buscar_acao(ticker, periodo="6mo"):
    try:
        dados = yf.Ticker(ticker).history(period=periodo, auto_adjust=False)

        if dados.empty:
            return pd.DataFrame()

        dados = dados.dropna(subset=["Open", "High", "Low", "Close"])

        return dados

    except Exception:
        return pd.DataFrame()


def calcular_indicadores(dados):
    """Calcula MME21, MME50, Estocástico lento, volume e ATR."""
    dados = dados.copy()

    # Médias móveis exponenciais
    dados["MME21"] = dados["Close"].ewm(
        span=21,
        adjust=False
    ).mean()

    dados["MME50"] = dados["Close"].ewm(
        span=50,
        adjust=False
    ).mean()

    # Estocástico
    periodo_stoch = 14
    suavizacao_k = 3
    periodo_d = 3

    maxima = dados["High"].rolling(periodo_stoch).max()
    minima = dados["Low"].rolling(periodo_stoch).min()

    intervalo = (maxima - minima).replace(0, float("nan"))

    dados["%K"] = (
        (dados["Close"] - minima) / intervalo
    ) * 100

    dados["%K_lento"] = dados["%K"].rolling(
        suavizacao_k
    ).mean()

    dados["%D"] = dados["%K_lento"].rolling(
        periodo_d
    ).mean()

    # Volume médio de 20 pregões
    dados["Volume_Medio20"] = dados["Volume"].rolling(20).mean()

    # ATR de 14 períodos
    high_low = dados["High"] - dados["Low"]
    high_close = (dados["High"] - dados["Close"].shift(1)).abs()
    low_close = (dados["Low"] - dados["Close"].shift(1)).abs()

    true_range = pd.concat(
        [high_low, high_close, low_close],
        axis=1
    ).max(axis=1)

    dados["ATR14"] = true_range.rolling(14).mean()

    return dados


def verificar_pfr(dados):

    if len(dados) < 3:
        return False

    fechamento_atual = dados["Close"].iloc[-1]
    fechamento_anterior = dados["Close"].iloc[-2]

    minima_atual = dados["Low"].iloc[-1]
    minima_anterior = dados["Low"].iloc[-2]
    minima_2_anterior = dados["Low"].iloc[-3]

    return (
        fechamento_atual > fechamento_anterior
        and minima_atual < minima_anterior
        and minima_atual < minima_2_anterior
    )


def analisar_sinal(dados):

    if len(dados) < 50:
        return None

    ultimo = dados.iloc[-1]
    anterior = dados.iloc[-2]

    pfr = verificar_pfr(dados)

    preco_mme21 = ultimo["Close"] > ultimo["MME21"]
    tendencia = ultimo["MME21"] > ultimo["MME50"]

    estocastico = (
        pd.notna(ultimo["%K_lento"])
        and pd.notna(ultimo["%D"])
        and ultimo["%K_lento"] > ultimo["%D"]
        and ultimo["%K_lento"] < 80
    )

    volume = (
        pd.notna(ultimo["Volume_Medio20"])
        and ultimo["Volume"] > ultimo["Volume_Medio20"]
    )

    score = sum([
        pfr,
        preco_mme21,
        tendencia,
        estocastico,
        volume,
    ])

    return {
        "PFR": pfr,
        "Preço > MME21": preco_mme21,
        "MME21 > MME50": tendencia,
        "Estocástico": estocastico,
        "Volume": volume,
        "Score": score,
        "Preço": ultimo["Close"],
        "MME21": ultimo["MME21"],
        "MME50": ultimo["MME50"],
        "%K": ultimo["%K_lento"],
        "%D": ultimo["%D"],
        "Volume atual": ultimo["Volume"],
        "Volume médio": ultimo["Volume_Medio20"],
        "ATR14": ultimo["ATR14"],
        "Variação": (
            (ultimo["Close"] / anterior["Close"] - 1) * 100
        ),
    }


@st.cache_data(ttl=900, show_spinner=False)
def executar_scanner(tickers):
    """Analisa todas as ações e retorna somente as que possuem PFR."""
    resultados = []

    for ticker in tickers:
        dados = buscar_acao(ticker)

        if dados.empty:
            continue

        dados = calcular_indicadores(dados)

        if not verificar_pfr(dados):
            continue

        analise = analisar_sinal(dados)

        if analise is None:
            continue

        analise["Ticker"] = ticker
        analise["Empresa"] = NOMES.get(
            ticker,
            ticker.replace(".SA", "")
        )

        analise["Dados"] = dados

        resultados.append(analise)

    return resultados


def formatar_moeda(valor):
    if pd.isna(valor):
        return "-"

    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def formatar_volume(valor):
    if pd.isna(valor):
        return "-"

    if valor >= 1_000_000:
        return f"{valor / 1_000_000:.2f}M"

    if valor >= 1_000:
        return f"{valor / 1_000:.1f}K"

    return f"{valor:.0f}"


def criar_grafico(dados, ticker):
    """Cria gráfico de candles + MME + Estocástico + Volume."""
    grafico = go.Figure()

    # Candlestick
    grafico.add_trace(
        go.Candlestick(
            x=dados.index,
            open=dados["Open"],
            high=dados["High"],
            low=dados["Low"],
            close=dados["Close"],
            name="Preço",
        )
    )

    # MME 21
    grafico.add_trace(
        go.Scatter(
            x=dados.index,
            y=dados["MME21"],
            mode="lines",
            name="MME 21",
        )
    )

    # MME 50
    grafico.add_trace(
        go.Scatter(
            x=dados.index,
            y=dados["MME50"],
            mode="lines",
            name="MME 50",
        )
    )

    grafico.update_layout(
        title=f"📈 {ticker} — Preço e Médias",
        xaxis_title="Data",
        yaxis_title="Preço",
        xaxis_rangeslider_visible=False,
        height=550,
    )

    return grafico


def criar_grafico_estocastico(dados):
    grafico = go.Figure()

    grafico.add_trace(
        go.Scatter(
            x=dados.index,
            y=dados["%K_lento"],
            mode="lines",
            name="%K",
        )
    )

    grafico.add_trace(
        go.Scatter(
            x=dados.index,
            y=dados["%D"],
            mode="lines",
            name="%D",
        )
    )

    grafico.add_hline(
        y=80,
        line_dash="dash",
        annotation_text="Sobrecompra",
    )

    grafico.add_hline(
        y=20,
        line_dash="dash",
        annotation_text="Sobrevenda",
    )

    grafico.update_layout(
        title="📊 Estocástico lento",
        xaxis_title="Data",
        yaxis_title="%",
        yaxis_range=[0, 100],
        height=300,
    )

    return grafico


def criar_grafico_volume(dados):
    grafico = go.Figure()

    grafico.add_trace(
        go.Bar(
            x=dados.index,
            y=dados["Volume"],
            name="Volume",
        )
    )

    grafico.add_trace(
        go.Scatter(
            x=dados.index,
            y=dados["Volume_Medio20"],
            mode="lines",
            name="Média 20",
        )
    )

    grafico.update_layout(
        title="📦 Volume",
        xaxis_title="Data",
        yaxis_title="Volume",
        height=300,
    )

    return grafico


# ============================================================
# INTERFACE
# ============================================================

st.title("📈 Scanner de Ações — PFR")

st.caption(
    "Scanner experimental de análise técnica. "
    "Os indicadores não garantem movimentos futuros."
)

with st.sidebar:
    st.header("⚙️ Configurações")

    periodo = st.selectbox(
        "Histórico",
        ["3mo", "6mo", "1y", "2y"],
        index=1,
    )

    quantidade = st.slider(
        "Quantidade máxima de ações para analisar",
        min_value=20,
        max_value=len(TICKERS),
        value=len(TICKERS),
        step=10,
    )

    executar = st.button(
        "🔄 Executar scanner",
        use_container_width=True,
    )

    st.divider()

    st.info(
        "Score máximo: 5 pontos\n\n"
        "• PFR\n"
        "• Preço > MME21\n"
        "• MME21 > MME50\n"
        "• Estocástico\n"
        "• Volume"
    )


# Executa automaticamente na primeira abertura
if executar or "resultados_scanner" not in st.session_state:
    with st.spinner("🔎 Analisando ações..."):
        st.session_state["resultados_scanner"] = executar_scanner(
            tuple(TICKERS[:quantidade])
        )


resultados = st.session_state.get("resultados_scanner", [])


# ============================================================
# RESUMO
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Ações analisadas",
        quantidade,
    )

with col2:
    st.metric(
        "PFR encontrados",
        len(resultados),
    )

with col3:
    if resultados:
        maior_score = max(item["Score"] for item in resultados)
    else:
        maior_score = 0

    st.metric(
        "Maior score",
        f"{maior_score}/5",
    )


if not resultados:
    st.warning("Nenhuma ação apresentou o padrão PFR.")
    st.stop()


# ============================================================
# TABELA DOS SINAIS
# ============================================================

st.subheader("🔎 Sinais encontrados")

tabela = pd.DataFrame([
    {
        "Ticker": item["Ticker"].replace(".SA", ""),
        "Empresa": item["Empresa"],
        "Preço": formatar_moeda(item["Preço"]),
        "PFR": "✓" if item["PFR"] else "✗",
        "MME21": "✓" if item["Preço > MME21"] else "✗",
        "Tendência": "✓" if item["MME21 > MME50"] else "✗",
        "Estocástico": "✓" if item["Estocástico"] else "✗",
        "Volume": "✓" if item["Volume"] else "✗",
        "Score": f'{item["Score"]}/5',
        "Variação": f'{item["Variação"]:.2f}%',
    }
    for item in sorted(
        resultados,
        key=lambda x: x["Score"],
        reverse=True,
    )
])

st.dataframe(
    tabela,
    use_container_width=True,
    hide_index=True,
)


# ============================================================
# SELEÇÃO DA AÇÃO
# ============================================================

opcoes = sorted(
    resultados,
    key=lambda x: x["Score"],
    reverse=True,
)

ticker_selecionado = st.selectbox(
    "Selecione uma ação para analisar",
    options=[item["Ticker"] for item in opcoes],
    format_func=lambda ticker: (
        f"{ticker.replace('.SA', '')} — "
        f"{NOMES.get(ticker, ticker)} — "
        f"Score "
        f"{next(x['Score'] for x in opcoes if x['Ticker'] == ticker)}/5"
    ),
)

selecionado = next(
    item for item in opcoes
    if item["Ticker"] == ticker_selecionado
)

dados = selecionado["Dados"]


# ============================================================
# DETALHES
# ============================================================

st.divider()

st.subheader(
    f"📊 {ticker_selecionado.replace('.SA', '')} — "
    f"{selecionado['Empresa']}"
)

m1, m2, m3, m4, m5 = st.columns(5)

with m1:
    st.metric(
        "Score",
        f"{selecionado['Score']}/5",
    )

with m2:
    st.metric(
        "Preço",
        formatar_moeda(selecionado["Preço"]),
    )

with m3:
    st.metric(
        "Variação",
        f"{selecionado['Variação']:.2f}%",
    )

with m4:
    st.metric(
        "Estocástico",
        f"{selecionado['%K']:.1f}",
    )

with m5:
    st.metric(
        "Volume",
        formatar_volume(selecionado["Volume atual"]),
    )


# Condições
st.subheader("🧩 Condições do sinal")

cond1, cond2, cond3, cond4, cond5 = st.columns(5)

condicoes = [
    ("PFR", selecionado["PFR"]),
    ("Preço > MME21", selecionado["Preço > MME21"]),
    ("MME21 > MME50", selecionado["MME21 > MME50"]),
    ("Estocástico", selecionado["Estocástico"]),
    ("Volume", selecionado["Volume"]),
]

for coluna, (nome, resultado) in zip(
    [cond1, cond2, cond3, cond4, cond5],
    condicoes,
):
    with coluna:
        if resultado:
            st.success(f"✓ {nome}")
        else:
            st.error(f"✗ {nome}")


# ============================================================
# GRÁFICOS
# ============================================================

st.plotly_chart(
    criar_grafico(dados, ticker_selecionado.replace(".SA", "")),
    use_container_width=True,
)

st.plotly_chart(
    criar_grafico_estocastico(dados),
    use_container_width=True,
)

st.plotly_chart(
    criar_grafico_volume(dados),
    use_container_width=True,
)


# ============================================================
# DADOS RECENTES
# ============================================================

with st.expander("📋 Ver dados recentes"):
    colunas = [
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
        "MME21",
        "MME50",
        "%K_lento",
        "%D",
        "ATR14",
    ]

    st.dataframe(
        dados[colunas].tail(20).round(2),
        use_container_width=True,
    )


st.caption(
    f"Última atualização: {dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
)