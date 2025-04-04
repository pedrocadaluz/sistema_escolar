import streamlit as st
from functions import (
    subir_arquivo, cadastrar_endereco, cadastro_aluno,
    editar_aluno, cadastrar_nota, editar_nota,
    gerar_pdf, df_alunos, df_disciplinas, df_notas,
    consultar_sql, atualizar_sql
)
from io import BytesIO

st.set_page_config(page_title="Gestão Acadêmica", layout="wide")
st.title("Sistema de Cadastro Acadêmico")

aba = st.sidebar.radio("Escolha uma opção:", [
    "🏫 Cadastro de Endereço",
    "🔁 Atualizar Endereço",
    "👨‍🎓 Cadastro de Aluno",
    "✏️ Editar Aluno",
    "📝 Cadastro de Nota",
    "✏️ Editar Nota",
    "📤 Upload de Arquivos",
    "📄 Gerar PDF"
])

if aba == "📤 Upload de Arquivos":
    st.subheader("Upload de Arquivo")
    arquivo = st.file_uploader("Escolha um arquivo", type=["csv", "xlsx", "json"])
    tabela = st.text_input("Nome da tabela de destino")
    if st.button("Enviar"):
        subir_arquivo(arquivo, tabela)

elif aba == "👨‍🎓 Cadastro de Aluno":
    st.subheader("Cadastrar Aluno")
    nome = st.text_input("Nome completo")
    email = st.text_input("E-mail")
    cep = st.text_input("CEP")
    carro_id = st.number_input("ID do carro", min_value=0, step=1)
    if st.button("Cadastrar"):
        cadastro_aluno({"nome_aluno": nome, "email": email, "cep": cep, "carro_id": carro_id})
        st.success("Aluno cadastrado com sucesso!")

elif aba == "✏️ Editar Aluno":
    st.subheader("Editar Aluno")
    id_aluno = st.number_input("ID do aluno", min_value=1, step=1)
    nome = st.text_input("Novo nome (opcional)")
    email = st.text_input("Novo e-mail (opcional)")
    cep = st.text_input("Novo CEP (opcional)")
    carro_id = st.number_input("Novo ID do carro (opcional)", min_value=0, step=1)
    if st.button("Atualizar"):
        editar_aluno(id_aluno, nome or None, email or None, cep or None, carro_id or None)
        st.success("Dados atualizados!")

elif aba == "🏫 Cadastro de Endereço":
    st.subheader("Cadastrar Endereço")
    cep = st.text_input("CEP")
    endereco = st.text_input("Endereço")
    cidade = st.text_input("Cidade")
    estado = st.text_input("Estado")
    if st.button("Cadastrar Endereço"):
        cadastrar_endereco({"cep": cep, "endereco": endereco, "cidade": cidade, "estado": estado})
        st.success("Endereço cadastrado com sucesso!")

elif aba == "Atualizar Endereço":
    st.subheader("Atualizar Endereço Existente")

    enderecos_df = consultar_sql("SELECT * FROM tb_enderecos")

    if not enderecos_df.empty:
        st.write("Endereços encontrados:")
        st.dataframe(enderecos_df)

        cep_selecionado = st.selectbox("Selecione o CEP para atualizar:", enderecos_df["cep"].unique())
        endereco_atual = enderecos_df[enderecos_df["cep"] == cep_selecionado].iloc[0]

        with st.form("form_atualiza_endereco"):
            novo_endereco = st.text_input("Endereço", value=endereco_atual["endereco"])
            nova_cidade = st.text_input("Cidade", value=endereco_atual["cidade"])
            novo_estado = st.text_input("Estado", value=endereco_atual["estado"])
            submit = st.form_submit_button("Atualizar Endereço")

        if submit:
            atualizar_sql("""
                UPDATE tb_enderecos
                SET endereco = :endereco,
                    cidade = :cidade,
                    estado = :estado
                WHERE cep = :cep
            """, {
                "endereco": novo_endereco,
                "cidade": nova_cidade,
                "estado": novo_estado,
                "cep": cep_selecionado
            })
            st.success(f"Endereço do CEP {cep_selecionado} atualizado com sucesso!")
    else:
        st.warning("Nenhum endereço cadastrado para atualizar.")


elif aba == "📝 Cadastro de Nota":
    st.subheader("Cadastrar Nota")
    aluno_id = st.number_input("ID do Aluno", min_value=1, step=1)
    disciplina_id = st.number_input("ID da Disciplina", min_value=1, step=1)
    nota = st.number_input("Nota", min_value=0.0, max_value=10.0, step=0.1)
    if st.button("Cadastrar Nota"):
        cadastrar_nota({"aluno_id": aluno_id, "disciplina_id": disciplina_id, "nota": nota})
        st.success("Nota cadastrada com sucesso!")

elif aba == "✏️ Editar Nota":
    st.subheader("Editar Nota")
    aluno_id = st.number_input("ID do Aluno", min_value=1, step=1)
    disciplina_id = st.number_input("ID da Disciplina", min_value=1, step=1)
    nova_nota = st.number_input("Nova Nota", min_value=0.0, max_value=10.0, step=0.1)
    if st.button("Atualizar Nota"):
        editar_nota({"aluno_id": aluno_id, "disciplina_id": disciplina_id, "nota": nova_nota})
        st.success("Nota atualizada!")

elif aba == "📄 Gerar PDF":
    st.subheader("Gerar PDF de Notas")

    try:
        dados = df_notas.merge(df_alunos, left_on="aluno_id", right_on="id") \
                        .merge(df_disciplinas, left_on="disciplina_id", right_on="id")

        dados = dados[["aluno_id", "nome_aluno", "nome_disciplina", "nota"]]

        if st.button("Gerar PDF"):
            pdf_bytes = gerar_pdf(dados)
            st.download_button(
                "📥 Baixar PDF",
                data=BytesIO(pdf_bytes),
                file_name="notas_alunos.pdf",
                mime="application/pdf"
            )

    except KeyError as e:
        st.error(f"Erro ao gerar PDF: coluna não encontrada. Detalhes: {e}")
    except Exception as e:
        st.error(f"Erro inesperado: {e}")
