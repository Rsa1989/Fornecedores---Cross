import streamlit as st
import pandas as pd
import os
import io
from datetime import datetime
import base64

# Configuração da página
st.set_page_config(page_title="Portal de Entregas - Fornecedores", layout="centered")

def carregar_logo(caminho_logo):
    with open(caminho_logo, "rb") as f:
        return base64.b64encode(f.read()).decode()
    
# Adiciona o logo no canto superior esquerdo
st.markdown(
    """
    <style>
    .logo-container {
        display: flex;
        align-items: center;
    }
    .logo-container img {
        width: 120px;
        margin-right: 15px;
    }
    .logo-container h1 {
        margin: 0;
        font-size: 28px;
    }
    </style>
    <div class="logo-container">
        <img src="data:image/png;base64,{imagem_base64}">
        <h1>📦 Portal de Entregas - Fornecedores</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# (Opcional: remova o st.title se já está no HTML acima)
# st.title("📦 Portal de Entregas - Fornecedores")
