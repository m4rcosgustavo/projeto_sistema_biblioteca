
# Sistema de Biblioteca

Projeto desenvolvido em grupo para organizar autores, livros, leitores e empréstimos, utilizando Python, Flask e SQLite.

## Objetivo

Desenvolver um sistema para organizar os livros da biblioteca, cadastrar leitores e registrar empréstimos e devoluções.

## Tecnologias utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML e CSS

## Funcionalidades do sistema

- Cadastro e consulta de autores.
- Cadastro e consulta de livros.
- Cadastro e consulta de leitores.
- Registro e remoção de empréstimos.
- Consulta dos empréstimos e registro de devoluções.

## Estrutura do projeto

- `app.py`: inicialização da aplicação.
- `database.py`: configuração do banco de dados.
- `models/`: modelos de autores, livros, leitores e empréstimos.
- `controllers/`: rotas e lógica das funcionalidades.
- `templates/`: páginas HTML.
- `static/`: arquivos CSS.
- `seed.py`: dados iniciais para testes.
- `README.md`: documentação do projeto.
- `DIARIO.md`: diário de desenvolvimento.

## Como executar

1. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

2. Execute a aplicação:

   ```bash
   python app.py
   ```

3. Acesse no navegador:

   `http://127.0.0.1:5000`

## Integrantes e responsabilidades

- Marcos Gustavo: estrutura e integração.
- Heloisa Pereira: banco de dados e modelos.
- Maria Luiza: interfaces e cadastros.
- Jullyane Sandra: empréstimos e documentação.
