import streamlit as st

st.set_page_config(
    page_title = "Home",
    page_icon = "🚀",
    layout = "wide")

st.sidebar.markdown("# PHD Project")
st.sidebar.divider()
st.sidebar.markdown("#### Desenvolvido por [Christiano Peres ](https://www.linkedin.com/in/christianods/)")
# ======================== Estrutura do home ================================
st.title("Dashboards")

st.divider()
st.markdown("### Seja muito bem-vindo ao dashboard interativo da minha tese de doutorado")
'''Esse dashboard tem por objetivo ajudar a vizualizar os dados de minha tese referentes a análise térmica e também acesso ao modelo preditivo desenvolvido nesse trabalho'''

st.markdown("### Sobre o Projeto")
'''O crescente aumento alarmante da concentração de dióxido de carbono (CO2) na atmosfera, majoritariamente decorrente de emissões de origem humana, representa uma ameaça significativa à vida na Terra. Nesse contexto, tecnologias de captura e armazenamento de carbono (CCS) têm emergido como soluções promissoras, como a adsorção em materiais carbonosos, destacando-se como uma abordagem proeminente. Esse trabalho tem por objetivo, desenvolver um modelo de aprendizado de máquina simples e aprimorado para prever a captura desse gás de efeito estufa para esse trabalho e realizar a captura do gás em biomassas de estudo'''

st.markdown("### Aquisição dos dados")
'''Os dados foram gerados através de análises de laboratório e armazenados em um dataframe.'''

st.markdown("### Como utilizar esse dashboard")
'''Esse dashboard foi dividido em 2 abas:'''

'''📊 Dashboard '''
'''- Nessa aba estão representados painéis interativos referentes as análises térmicas das amostras FACPFP-4700, FACBP-4600 e FACM-4450 e modelo preditivo aprimorado por validação cruzada.'''

'''✉️ Contato '''
'''- Aba de contato traz as principais formas que você pode entrar em contato comigo.'''
st.divider()
