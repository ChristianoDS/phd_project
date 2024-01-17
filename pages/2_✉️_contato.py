# Libraries
import streamlit as st

#======================================================================================== 
#                              Parâmetros do layout
#========================================================================================
st.set_page_config(page_title='Contato',page_icon='✉️',layout='wide')
#========================================================================================
#                           Funções
#========================================================================================

#========================================================================================
#----------------- Barra lateral ---------------------------------------------------------------------------------
#========================================================================================
# Configurações iniciais
st.markdown("# 📱✉️ Entre em contato")
st.sidebar.markdown("# PHD Project")
st.sidebar.divider()
st.sidebar.markdown("#### Desenvolvido por [Christiano Peres ](https://www.linkedin.com/in/christianods/)")

# =====================================================================
# Layout no streamlit
# =====================================================================
st.header("Links de contato")
st.divider()
st.markdown("#### Portifólio de projetos 🚀: https://christianods.github.io/portifolio_projetos")
st.markdown("#### Linkedin 🔗: https://www.linkedin.com/in/christianods")
st.markdown("#### Github 💻: https://github.com/ChristianoDS")
st.markdown("#### Email ✉️: christianoperes21@gmail.com")
st.markdown("#### Discord 💬: christianoperes")
st.divider()
          