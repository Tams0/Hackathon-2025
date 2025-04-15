import streamlit as st
import openai
import os
from azure.storage.blob import BlobServiceClient

# Load secrets (via variables d'env dans Azure App Service)
openai.api_key = os.getenv("OPENAI_API_KEY")
azure_conn_str = os.getenv("AZURE_STORAGE_CONN_STRING")

# Azure Blob init
blob_service_client = BlobServiceClient.from_connection_string(azure_conn_str)
container_client = blob_service_client.get_container_client("mycontainer")

# UI Streamlit
st.title("Ma Super App avec Azure et OpenAI")

prompt = st.text_input("Pose une question à GPT:")

if prompt:
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    st.write(response["choices"][0]["message"]["content"])

    # (exemple) Lister les fichiers blob Azure
    st.subheader("Contenu du container Azure:")
    for blob in container_client.list_blobs():
        st.write(blob.name)
