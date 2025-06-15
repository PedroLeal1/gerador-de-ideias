import streamlit as st
import google.generativeai as genai

# Configura a API do Gemini com segurança
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Inicializa o modelo
model = genai.GenerativeModel("gemini-1.5-flash")

# Configuração da página
st.set_page_config(page_title="Gerador de Ideias Virais")
st.title("🎯 Gerador de Ideias Virais para Criadores de Conteúdo")

# Entrada do tema principal
tema = st.text_input("Informe o nicho ou tema do seu conteúdo (ex: futebol, games, maquiagem):")

# Escolha do formato
formato = st.selectbox(
    "Formato do conteúdo:",
    ["Vídeo", "Post de Instagram", "Reels/TikTok", "Tweet", "Carrossel"]
)

# Escolha da categoria de conteúdo
st.markdown("### Tipos de Conteúdo:")
categoria = st.selectbox(
    "Escolha o estilo principal do seu conteúdo:",
    [
        "🎮 Entretenimento",
        "🎭 Humor",
        "📚 Educativo",
        "📢 Promoção",
        "🎯 Opinião",
        "🧠 Curiosidades"
    ]
)

# Grau de Originalidade
st.markdown("### Grau de Originalidade:")
originalidade = st.selectbox(
    "Escolha o nível:",
    ["🚀 Inovador", "⚖️ Equilibrado", "🔥 Popular e Seguro"]
)

# Geração
if st.button("Gerar Ideia"):
    if tema:
        # Montagem do prompt
        prompt = (
            f"Crie uma ideia viral de conteúdo no formato '{formato}' sobre o tema '{tema}'. "
            f"O estilo do conteúdo deve ser '{categoria}'. "
            f"Busque um nível de originalidade '{originalidade}'. "
            f"Responda com uma ideia prática, bem detalhada, aplicável e diretamente executável por um criador de conteúdo."
        )

        try:
            resposta = model.generate_content(prompt)
            st.subheader("💡 Ideia Gerada:")
            st.write(resposta.text)
        except Exception as e:
            st.error(f"Erro ao gerar a ideia: {e}")
    else:
        st.warning("Por favor, informe o tema.")
