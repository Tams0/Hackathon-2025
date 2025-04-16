import streamlit as st
import openai
import os

# 🔐 Configuration avec tes infos Azure
openai.api_type = "azure"
openai.api_base = "https://openairessource001.openai.azure.com/"
openai.api_version = "2024-07-18"
openai.api_key = ""

# Le nom du déploiement (modèle GPT que tu as déployé sur Azure)
DEPLOYMENT_NAME = "gpt-4o-mini"

# 🎨 Interface utilisateur
st.set_page_config(page_title="Chat RAG Azure", layout="centered")
st.title("📄🔍 Chat PDF avec RAG sur Azure")

# 💬 Entrée utilisateur
question = st.text_input("Pose ta question sur les documents PDF :", "")

if question:
    with st.spinner("Recherche en cours..."):

        try:
            # Envoie de la requête à Azure OpenAI avec Azure Search intégré (RAG)
            response = openai.ChatCompletion.create(
                engine=DEPLOYMENT_NAME,
                messages=[
                    {"role": "system", "content": "Tu es un assistant qui répond en te basant sur les documents internes."},
                    {"role": "user", "content": question}
                ],
                temperature=0,
                top_p=1,
                max_tokens=500,
                stop=None,
                stream=False,
                tools=[],
                extra_headers={
                    "azure-search-endpoint": "https://aisearchressource001.search.windows.net",
                    "azure-search-index-name": "nosprogrammes",
                    "azure-search-key": ""
                }
            )

            # 🎯 Affichage de la réponse
            answer = response['choices'][0]['message']['content']
            st.markdown("### 🧠 Réponse")
            st.write(answer)

        except Exception as e:
            st.error(f"Erreur lors de la récupération de réponse : {e}")
