import pandas as pd
import streamlit as st
from sqlalchemy import text
from db_connection import get_engine
from fpdf import FPDF

engine = get_engine()

def executar_sql(query, params=None):
    try:
        with engine.begin() as conn:
            conn.execute(text(query), params or {})
    except Exception as e:
        st.error(f"Erro ao executar SQL: {e}")

def subir_arquivo(arquivo, tabela):
    try:
        if arquivo.name.endswith('.csv'):
            df = pd.read_csv(arquivo)
        elif arquivo.name.endswith('.xlsx'):
            df = pd.read_excel(arquivo)
        elif arquivo.name.endswith('.json'):
            df = pd.read_json(arquivo)
        else:
            st.error("Formato de arquivo não suportado.")
            return

        df.to_sql(tabela, con=engine, if_exists="append", index=False)
        st.success("Arquivo enviado com sucesso.")
    except Exception as e:
        st.error(f"Erro ao subir o arquivo: {e}")

def cadastro_aluno(data):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM tb_enderecos WHERE cep = :cep"),
            {"cep": data["cep"]}
        )
        endereco_existe = result.fetchone()

    # Se o CEP não existir, mostra um aviso e interrompe o cadastro
    if not endereco_existe:
        st.warning("CEP não encontrado. Por favor, cadastre o endereço primeiro na aba '🏫 Cadastro de Endereço'.")
        return

    executar_sql("""
        INSERT INTO tb_alunos (nome_aluno, email, cep, carro_id)
        VALUES (:nome_aluno, :email, :cep, :carro_id)
    """, data)

def editar_aluno(id_aluno, nome=None, email=None, cep=None, carro_id=None):
    campos = []
    dados = {"id": id_aluno}
    if nome:
        campos.append("nome_aluno = :nome")
        dados["nome"] = nome
    if email:
        campos.append("email = :email")
        dados["email"] = email
    if cep:
        campos.append("cep = :cep")
        dados["cep"] = cep
    if carro_id is not None:
        campos.append("carro_id = :carro_id")
        dados["carro_id"] = carro_id

    if campos:
        query = f"UPDATE tb_alunos SET {', '.join(campos)} WHERE id = :id"
        executar_sql(query, dados)

def cadastrar_endereco(data):
    executar_sql("""
        INSERT INTO tb_enderecos (cep, endereco, cidade, estado)
        VALUES (:cep, :endereco, :cidade, :estado)
    """, data)

def cadastrar_nota(data):
    executar_sql("""
        INSERT INTO tb_notas (aluno_id, disciplina_id, nota)
        VALUES (:aluno_id, :disciplina_id, :nota)
    """, data)

def editar_nota(data):
    executar_sql("""
        UPDATE tb_notas SET nota = :nota
        WHERE aluno_id = :aluno_id AND disciplina_id = :disciplina_id
    """, data)

def gerar_pdf(dados):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Relatório de Notas", ln=True, align="C")
    pdf.ln(10)

    for _, row in dados.iterrows():
        linha = f"Aluno ID: {row['aluno_id']} - {row['nome_aluno']} | Disciplina: {row['nome_disciplina']} | Nota: {row['nota']}"
        pdf.multi_cell(0, 10, linha)

    output = pdf.output(dest='S').encode('latin1')
    return output

def carregar_tabelas():
    with engine.connect() as conn:
        df_alunos = pd.read_sql("SELECT * FROM tb_alunos", con=conn)
        df_disciplinas = pd.read_sql("SELECT * FROM tb_disciplinas", con=conn)
        df_notas = pd.read_sql("SELECT * FROM tb_notas", con=conn)
    return df_alunos, df_disciplinas, df_notas

def consultar_sql(query, params=None):
    try:
        with engine.connect() as conn:
            return pd.read_sql(text(query), con=conn, params=params or {})
    except Exception as e:
        st.error(f"Erro ao consultar SQL: {e}")
        return pd.DataFrame()

def atualizar_sql(query, params=None):
    try:
        with engine.begin() as conn:
            conn.execute(text(query), params or {})
    except Exception as e:
        st.error(f"Erro ao atualizar dados: {e}")



df_alunos, df_disciplinas, df_notas = carregar_tabelas()
