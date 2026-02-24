import streamlit as st
from core.convert import analisarPdf
from core.cleaner import clearText
from core.chunking import chunkText
from core.embeddings import embedding
from database.vetor_db import initDB, addChunks, search
from core.rag import answerQuestion

st.title("Chat De IA especialista em Odonto")

uploaded_file = st.file_uploader("Escolha um PDF ou TXT", type=["pdf", "txt"])

if uploaded_file:
    try:
        raw_text = analisarPdf(uploaded_file)
        clean_text = clearText(raw_text)

        chunks = chunkText(clean_text)
        st.success(f"Documento processado em {len(chunks)} chunks.")

        collection = initDB()
        addChunks(collection, chunks, embedding)
        st.info("Chunks adicionados ao banco vetorial com embeddings.")

    except Exception as e:
        st.error(f"Erro ao processar arquivo: {e}")

st.subheader("Realize uma interação sobre o documento:")

question = st.text_input("Digite sua dúvida aqui")

top_k = st.slider("Número de trechos a recuperar (top-k)", 1, 10, 3)

if st.button("Resposta") and question and uploaded_file:
    with st.spinner("Buscando respostas!"):
        result = answerQuestion(collection, question, embedding, k=top_k)

        st.markdown("**Resposta gerada:**")
        st.write(result["answer"])

        st.markdown("**Trechos utilizados:**")
        for i, seg in enumerate(result["segments"]):
            st.write(f"{i+1}: {seg[:300]}...")  

        st.markdown("**Scores de similaridade:**")
        st.write(result["scores"])