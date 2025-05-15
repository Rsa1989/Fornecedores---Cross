import streamlit as st
import pandas as pd
import os
import io
from datetime import datetime

st.set_page_config(page_title="Portal de Entregas - Fornecedores", layout="centered")
st.title("📦 Portal de Entregas - Fornecedores")

def gerar_modelo_excel():
    df_modelo = pd.DataFrame(columns=[
        "Fornecedor", "Material", "Obra", "Descrição", "Quantidade", 
        "Número Pedido", "Nota fiscal", "Placa veículo", "Data expedida", "Data chegada TKE"
    ])
    buffer = io.BytesIO()
    df_modelo.to_excel(buffer, index=False)
    buffer.seek(0)
    return buffer

st.subheader("📥 Baixe o modelo de planilha")
st.download_button(
    label="📄 Baixar modelo Excel",
    data=gerar_modelo_excel(),
    file_name="modelo_entrega.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

st.subheader("📤 Envie seu arquivo preenchido")
uploaded_file = st.file_uploader("Selecione o arquivo Excel preenchido", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)

        colunas_esperadas = [
            "Fornecedor", "Material", "Obra", "Descrição", "Quantidade", 
            "Número Pedido", "Nota fiscal", "Placa veículo", "Data expedida", "Data chegada TKE"
        ]

        if all(col in df.columns for col in colunas_esperadas):
            st.success("✅ Arquivo recebido com sucesso! Visualização abaixo:")
            st.dataframe(df)

            # Pega o fornecedor da primeira linha para usar no nome do arquivo
            fornecedor_nome = df.loc[0, "Fornecedor"]
            fornecedor_nome_sanitizado = str(fornecedor_nome).replace(" ", "_").replace("/", "-")

            # Filtra apenas as colunas necessárias
            df_filtrado = df[colunas_esperadas]

            # Caminho absoluto para salvar
            pasta_uploads = r"O:\DEEX\ESTOQUE\Script Cross - fornecedores\Uploads"
            os.makedirs(pasta_uploads, exist_ok=True)

            hoje = datetime.now().strftime("%Y-%m-%d_%H-%M")
            nome_arquivo = f"fornecedor_{fornecedor_nome_sanitizado}_{hoje}.csv"
            caminho_completo = os.path.join(pasta_uploads, nome_arquivo)

            df_filtrado.to_csv(caminho_completo, index=False)

            st.success(f"📁 Arquivo salvo em: {caminho_completo}")
        else:
            st.error("❌ O arquivo enviado não contém todas as colunas necessárias.")
    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")
