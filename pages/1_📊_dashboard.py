# Importação das bibliotecas

import picnik as pnk 
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.linear_model import LinearRegression

# =============================================================================
# ------------------ Gráficos -------------------------------------------------
# =============================================================================
# Arquivos bases
# -------CO2 ------------------------------
df10 = pd.read_excel("./dataset/df_co2.xlsx")
# ------ TGA ------------------------------
df1 = pd.read_excel("./dataset/CAMA700_10_Ni.xls")
df2 = pd.read_excel("./dataset/CAMA700_15_Ni.xls")
df3 = pd.read_excel("./dataset/CAMA700_20_Ni.xls")

df11 = pd.read_excel("./dataset/CABA600_10_Ni.xls")
df12 = pd.read_excel("./dataset/CABA600_15_Ni.xls")
df13 = pd.read_excel("./dataset/CABA600_20_Ni.xls")

df21 = pd.read_excel("./dataset/CAMABA450_10_Ni.xls")
df22= pd.read_excel("./dataset/CAMABA450_15_Ni.xls")
df23 = pd.read_excel("./dataset/CAMABA450_20_Ni.xls")

#Arquivo picNIK
df4 = pd.read_excel("./dataset/Activation_Energies_Results_1.xlsx")
df5 = pd.read_excel("./dataset/Activation_Energies_Results_FACPFP-4700_Ni.xlsx")
df5.columns = ['modelos','media','desvio_pad']

df41 = pd.read_excel("./dataset/Activation_Energies_Results_2.xlsx")
df51 = pd.read_excel("./dataset/Activation_Energies_Results_FACPBP-4600_Ni.xlsx")
df51.columns = ['modelos','media','desvio_pad']

df42 = pd.read_excel("./dataset/Activation_Energies_Results_3.xlsx")
df52 = pd.read_excel("./dataset/Activation_Energies_Results_FACM-4450_Ni.xlsx")
df52.columns = ['modelos','media','desvio_pad']

# ## Eliminando o cabeçalho da tabela dos dados
# Caso precise eliminar alguma linha, 0 é a linha a ser eliminada e axis=0 é linha, axis=1 é coluna

df1=df1.drop(0, axis=0)
df2=df2.drop(0, axis=0)
df3=df3.drop(0, axis=0)

df11=df11.drop(0, axis=0)
df12=df12.drop(0, axis=0)
df13=df13.drop(0, axis=0)

df21=df21.drop(0, axis=0)
df22=df22.drop(0, axis=0)
df23=df23.drop(0, axis=0)

# =================================================================================================
# ## Construindo o gráfico dos modelos cinéticos calculados pelo modelo de Ramirez et al (2022)
# =================================================================================================
# -------------------- FACPFP-4700 -----------------------------------------------------------------
colsA_10 = ["KAS [kJ/mol]"]
colsA_20 = ["OFW [kJ/mol]"]
colsA_30 = ["Fr [kJ/mol]"]
xA0 = df4.alpha
yA0 = df4.loc[:,colsA_10].values
y1A0 = df4.loc[:,colsA_20].values
y2A0 = df4.loc[:,colsA_30].values

fig2 = px.line()
fig2.add_scatter(x=xA0, y=yA0.flatten(), mode='markers+lines', name='KAS', marker=dict(size=5, symbol='circle'))
fig2.add_scatter(x=xA0, y=y1A0.flatten(), mode='markers+lines', name='OFW', marker=dict(size=5, symbol='square'))
fig2.add_scatter(x=xA0, y=y2A0.flatten(), mode='markers+lines', name='Fr', marker=dict(size=5, symbol='triangle-down'))

# Configurações do layout
fig2.update_layout(
    xaxis_title="Alpha",
    yaxis_title="Ea [kJ/mol]",
    title = 'Ea values',
    xaxis=dict(range=[0.1, 0.95]),
    yaxis=dict(range=[0, 250]))
# -------------------- FACBP-4600 -----------------------------------------------------------------
colsB_10 = ["KAS [kJ/mol]"]
colsB_20 = ["OFW [kJ/mol]"]
colsB_30 = ["Fr [kJ/mol]"]
xA0B = df41.alpha
yA0B = df41.loc[:,colsB_10].values
y1A0B = df41.loc[:,colsB_20].values
y2A0B = df41.loc[:,colsB_30].values

fig21 = px.line()
fig21.add_scatter(x=xA0B, y=yA0B.flatten(), mode='markers+lines', name='KAS', marker=dict(size=5, symbol='circle'))
fig21.add_scatter(x=xA0B, y=y1A0B.flatten(), mode='markers+lines', name='OFW', marker=dict(size=5, symbol='square'))
fig21.add_scatter(x=xA0B, y=y2A0B.flatten(), mode='markers+lines', name='Fr', marker=dict(size=5, symbol='triangle-down'))

# Configurações do layout
fig21.update_layout(
    xaxis_title="Alpha",
    yaxis_title="Ea [kJ/mol]",
    title = 'Ea values',
    xaxis=dict(range=[0.1, 0.95]),
    yaxis=dict(range=[0, 400]))
# -------------------- FACM-4450 -----------------------------------------------------------------
colsC_10 = ["KAS [kJ/mol]"]
colsC_20 = ["OFW [kJ/mol]"]
colsC_30 = ["Fr [kJ/mol]"]
xA0C = df42.alpha
yA0C = df42.loc[:,colsC_10].values
y1A0C = df42.loc[:,colsC_20].values
y2A0C= df42.loc[:,colsC_30].values

fig22 = px.line()
fig22.add_scatter(x=xA0C, y=yA0C.flatten(), mode='markers+lines', name='KAS', marker=dict(size=5, symbol='circle'))
fig22.add_scatter(x=xA0C, y=y1A0C.flatten(), mode='markers+lines', name='OFW', marker=dict(size=5, symbol='square'))
fig22.add_scatter(x=xA0C, y=y2A0C.flatten(), mode='markers+lines', name='Fr', marker=dict(size=5, symbol='triangle-down'))

# Configurações do layout
fig22.update_layout(
    xaxis_title="Alpha",
    yaxis_title="Ea [kJ/mol]",
    title = 'Ea values',
    xaxis=dict(range=[0.1, 0.95]),
    yaxis=dict(range=[0, 300]))
# =================================================================
# ## Construindo o gráfico da massa x temp
# =================================================================
# ------------------------ FACPFP-4700 ----------------------------
# Definindo as colunas
colsA = ["Weight"]
colsB = ["Weight"]
colsC = ["Weight"]

# Obtendo os valores para o gráfico
x1, x2, x3 = df1["Temperature"], df2["Temperature"], df3["Temperature"]
y1, y2, y3 = df1[colsA].values, df2[colsB].values, df3[colsC].values

# Criando o gráfico Plotly
fig = px.line()
fig.add_scatter(x=x1, y=y1.flatten(), mode='markers+lines', name='10°C/min', marker=dict(size=5, symbol='circle'))
fig.add_scatter(x=x2, y=y2.flatten(), mode='markers+lines', name='15°C/min', marker=dict(size=5, symbol='square'))
fig.add_scatter(x=x3, y=y3.flatten(), mode='markers+lines', name='20°C/min', marker=dict(size=5, symbol='triangle-down'))

# Configurações do layout
fig.update_layout(
    xaxis_title="Temperature [°C]",
    yaxis_title="Mass [%]",
    title = 'TGA Curves',
    xaxis=dict(range=[25, 1000]),
    yaxis=dict(range=[0, 105]),
)
# ------------------------ FACBP-4600 ----------------------------
# Definindo as colunas
colsA = ["Weight"]
colsA = ["Weight"]
colsA = ["Weight"]

# Obtendo os valores para o gráfico
x21, x22, x23 = df11["Temperature"], df12["Temperature"], df13["Temperature"]
y21, y22, y23 = df11[colsA].values, df12[colsB].values, df13[colsC].values

# Criando o gráfico Plotly
fig23 = px.line()
fig23.add_scatter(x=x21, y=y21.flatten(), mode='markers+lines', name='10°C/min', marker=dict(size=5, symbol='circle'))
fig23.add_scatter(x=x22, y=y22.flatten(), mode='markers+lines', name='15°C/min', marker=dict(size=5, symbol='square'))
fig23.add_scatter(x=x23, y=y23.flatten(), mode='markers+lines', name='20°C/min', marker=dict(size=5, symbol='triangle-down'))

# Configurações do layout
fig23.update_layout(
    xaxis_title="Temperature [°C]",
    yaxis_title="Mass [%]",
    title = 'TGA Curves',
    xaxis=dict(range=[25, 1000]),
    yaxis=dict(range=[0, 105]),
)
# ------------------------ FACM-4450 ----------------------------
# Definindo as colunas
colsA = ["Weight"]
colsB = ["Weight"]
colsC = ["Weight"]

# Obtendo os valores para o gráfico
x31, x32, x33 = df21["Temperature"], df22["Temperature"], df23["Temperature"]
y31, y32, y33 = df21[colsA].values, df22[colsB].values, df23[colsC].values

# Criando o gráfico Plotly
fig24 = px.line()
fig24.add_scatter(x=x31, y=y31.flatten(), mode='markers+lines', name='10°C/min', marker=dict(size=5, symbol='circle'))
fig24.add_scatter(x=x32, y=y32.flatten(), mode='markers+lines', name='15°C/min', marker=dict(size=5, symbol='square'))
fig24.add_scatter(x=x33, y=y33.flatten(), mode='markers+lines', name='20°C/min', marker=dict(size=5, symbol='triangle-down'))

# Configurações do layout
fig24.update_layout(
    xaxis_title="Temperature [°C]",
    yaxis_title="Mass [%]",
    title = 'TGA Curves',
    xaxis=dict(range=[25, 1000]),
    yaxis=dict(range=[0, 105]),
)

# ======================================================================================
# ------------------ Layout Streamlit --------------------------------------------------
# ======================================================================================
tab1, tab2, tab3, tab4 = st.tabs (["FACPFP-4700", "FACBP-4600", "M", "CO2_Prediction"]) 
with tab1:
    st.markdown ("### Métricas de análise térmica: FACPFP-4700")
    st.divider()
    st.plotly_chart(fig, use_container_width=True)
    st.divider()
    st.plotly_chart(fig2, use_container_width=True)
    st.divider()
    st.markdown ("#### Resultados da análise cinética")
    st.dataframe(df5)  
with tab2:
    st.markdown ("### Métricas de análise térmica: FACBP-4600")
    st.divider()
    st.plotly_chart(fig23, use_container_width=True)
    st.divider()
    st.plotly_chart(fig21, use_container_width=True)
    st.divider()
    st.markdown ("#### Resultados da análise cinética")
    st.dataframe(df51) 
with tab3:
    st.markdown ("### Métricas de análise térmica: FACM-4450")
    st.divider()
    st.plotly_chart(fig24, use_container_width=True)
    st.divider()
    st.plotly_chart(fig22, use_container_width=True)
    st.divider()
    st.markdown ("#### Resultados da análise cinética")
    st.dataframe(df52) 
with tab4:
    # =============================================================================
    # ------------------ Modelo preditivo -------------------------------------------------
    # =============================================================================
    import streamlit as st
    import pandas as pd
    import numpy as np
    from sklearn.linear_model import LinearRegression

    # Suponha que df10 seja seu DataFrame

    independente = df10.iloc[:, [2, 4]].values
    dependente = df10.iloc[:, 1].values
    modelo = LinearRegression()
    modelo_final = modelo.fit(independente, dependente)

    val_bet = st.text_input('Entre com o valor da área BET (m2/g)')
    val_micro = st.text_input('Entre com o valor de microporo (cm3/g)')

    if val_bet and val_micro:  # Verifica se ambos os valores foram inseridos
        val_bet = float(val_bet)
        val_micro = float(val_micro)
        
        previsoes_novos_dados = modelo_final.predict([[val_bet, val_micro]]).round(2)
        st.metric('Valor previsto de captura de CO2:', previsoes_novos_dados, 'mmol/g')
    else:
        st.warning('Por favor, insira valores para a área BET e microporo.')
