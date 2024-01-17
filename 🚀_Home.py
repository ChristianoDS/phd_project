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
'''FALAR DA TESE.'''

st.markdown("### Aquisição dos dados")
'''ONDE ESTÃO OS DADOS'''

st.markdown("### Como utilizar esse dashboard")
'''Esse dashboard foi dividido em 2 abas:'''

'''- 📊 Dashboard '''
'''Nessa aba estão representados painéis interativos referentes as análises térmicas e modelo preditivo'''

'''✉️ Contato '''
'''Aba de contato traz as principais formas que você pode entrar em contato comigo.'''
st.divider()