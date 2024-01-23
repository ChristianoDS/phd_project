# Phd Project

# Sobre o projeto
Esse projeto trata da apresentação dos dados gerados através de programação Python e do modelo de Machine Learning (ML) construído como parte da minha tese de doutorado.

# Problema de Pesquisa
O crescente aumento da concentração de dióxido de carbono (CO2) na atmosfera, majoritariamente decorrente de emissões de origem humana, representa uma ameaça significativa à vida na Terra. Nesse contexto, tecnologias de captura e armazenamento de carbono (CCS) têm emergido como soluções promissoras, como a adsorção em materiais carbonosos, destacando-se como uma abordagem proeminente. Capturar esse gás estufa e reduzir custos tornam-se de suma importancia, com isso, surge a necessidade da criação de um modelo preditivo para prever a captura do CO2, reduzindo custos de laboraório e despezas operacionais.

# Premissas assumidas
Para criação do modelo de ML, foram assumidas variáveis explicativas (features) de área superficial específica (BET) e volume de microporo.
Os dados foram gerados de forma experimental e transpostos para um dataframe.
O conjunto de dados do dataframe já se encontra limpo e processado, não havendo necessidade da etapa de Limpeza.

# Estratégia de solução do problema
Esse dashboard foi dividido em 2 abas:

📊 Dashboard 
- Nessa aba estão representados painéis interativos referentes as análises térmicas das amostras FACPFP-4700, FACBP-4600 e FACM-4450 e modelo preditivo aprimorado por validação cruzada.

✉️ Contato 
- Aba de contato traz as principais formas que você pode entrar em contato comigo.

# Principais insights
- Para esse estudo, área superficial BET e volume de microporo explicam cerca de 89% da captura de CO2.

# O produto final do projeto
Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.

O painel pode ser acessado através desse link: [https://christiano-zomato-project.streamlit.app/]

# Conclusão
Para essa tese, o modelo de machine learning de regressão linear múltipla melhorado com validação cruzada apresentou uma precisão de 89%. Área BET e volume de microporos são features extremamente relevantes no modelo preditivo.

# Próximos passos
Testar mais modelos de machine learning, como redes neurais aritificais. 
Realizar experimentação com outras temperaturas (500, 800 e 1000°C)

# Ferramentas utilizadas:
- ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
- ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
- ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
