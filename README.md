# sistema_escolar
Projeto da faculdade utilizando habilidades aprendidas em sala. Leia o README para mais.

# 📚 Sistema de Gestão Acadêmica

Bem-vindo ao **Sistema de Gestão Acadêmica**, um projeto desenvolvido com **Python**, **Streamlit** e **MySQL** para facilitar o gerenciamento de alunos, endereços, notas e disciplinas de forma simples, intuitiva e 100% web.

---

## 🚀 Funcionalidades

✅ Cadastro de alunos  
✅ Cadastro e atualização de endereços  
✅ Cadastro e edição de notas  
✅ Upload de arquivos (CSV, Excel, JSON)  
✅ Geração de PDF com as notas dos alunos  
✅ Interface interativa via Streamlit  
✅ Integração com banco de dados MySQL

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12
- Streamlit
- SQLAlchemy
- MySQL
- Pandas
- FPDF

---

## 📁 Estrutura do Projeto

```bash
📦 db_escola/
├── app.py                 # Interface principal do sistema (Streamlit)
├── functions.py           # Funções de CRUD e utilidades
├── db_connection.py       # Conexão com o banco de dados MySQL
├── .env                   # Configurações sensíveis (host, user, senha...)
├── create_db.sql          # Script para criação do banco de dados
└── README.md              # Este arquivo


Clonar o repositorio
git clone https://github.com/pedrocadaluz/sistema_escolar.git
cd sistema_escolar

Crie e ative o venv
cd caminho/para/seu/projeto
python -m venv meu_ambiente_virtual
meu_ambiente_virtual\Scripts\activate #Windows
source meu_ambiente_virtual/bin/activate #Mac/Linux
deactivate #para desativar

Instale as dependências:
pip install -r requirements.txt

Crie um arquivo .env e configure da seguinte maneira:
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=escola


Para executar o projeto basta:
streamlit run app.py


## 🧾 Exemplo de Uso
Acesse a aba "🏫 Cadastro de Endereço" para registrar endereços por CEP

Cadastre alunos em "👨‍🎓 Cadastro de Aluno" vinculando ao CEP existente

Registre ou edite notas por disciplina

Gere um PDF com todas as notas em "📄 Gerar PDF"

Use "📤 Upload de Arquivos" para importar dados em massa para o banco


## 👨‍💻 Autor
Desenvolvido por Pedro Arthur Miranda 🚀

Sinta-se à vontade para abrir issues, contribuir com melhorias ou sugestões!