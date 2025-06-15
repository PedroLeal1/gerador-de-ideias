import streamlit as st
import google.generativeai as genai

# ✅ Coloque sua chave real aqui
API_KEY = "AIzaSyBG8DG3bokET1QmKIwWJUQxo3U5KbAUNx0"

# ✅ Segurança básica: se esquecer de colocar, avisa e para tudo
if not API_KEY:
    st.error("❌ Chave da API não foi definida. Edite o código e insira sua chave.")
    st.stop()

# ✅ Configura a API do Gemini
genai.configure(api_key=API_KEY)

# ✅ Inicializa o modelo Gemini
try:
    model = genai.GenerativeModel("gemini-2.0-flash")
except Exception as e:
    st.error(f"Erro ao inicializar o modelo: {e}")
    st.stop()

# Configuração da página
st.set_page_config(page_title="Gerador de Ideias Virais")
st.title("🎯 Gerador de Ideias Virais para Criadores de Conteúdo")

# Entrada do tema principal
tema = st.text_input("Informe o nicho ou tema do seu conteúdo (ex: futebol, games, maquiagem):")

# Escolha do formato
formato = st.selectbox("Formato do conteúdo:", ["Vídeo", "Post de Instagram", "Reels/TikTok", "Tweet", "Carrossel"])

# Checkboxes de modificadores
st.markdown("### Personalizações extras:")
humor = st.checkbox("Adicionar humor")
chamada = st.checkbox("Incluir chamada para engajamento")
trend = st.checkbox("Inspirar-se em tendências atuais")

# Geração
if st.button("Gerar Ideia"):
    if tema:
        prompt = f"Crie uma ideia viral de conteúdo no formato '{formato}' sobre o tema '{tema}'."
        if humor:
            prompt += " Adicione um toque de humor."
        if chamada:
            prompt += " Inclua uma chamada para incentivar o engajamento do público."
        if trend:
            prompt += " Considere tendências atuais relevantes."

        prompt += " Responda com uma ideia prática, bem detalhada, para ser executada pelo criador de conteúdo."

        try:
            resposta = model.generate_content(prompt)
            st.subheader("💡 Ideia Gerada:")
            st.write(resposta.text)
        except Exception as e:
            st.error(f"Erro ao gerar a ideia: {e}")
    else:
        st.warning("Por favor, informe o tema.")
