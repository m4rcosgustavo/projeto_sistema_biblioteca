# Sistema de Biblioteca

Projeto desenvolvido em grupo para a disciplina de Programação para Servidores Web (PSI), utilizando Python, Flask, SQLAlchemy e SQLite.

## 1. Tema e objetivo

O tema escolhido foi **Sistema de Biblioteca**.

O objetivo é organizar autores, livros e leitores, permitindo cadastrar e consultar registros, realizar empréstimos, controlar devoluções e acompanhar a situação dos livros emprestados.

## 2. Integrantes e responsabilidades

- **Marcos Gustavo:** estrutura MVC, configuração da aplicação e integração das rotas.
- **Heloisa Pereira:** banco de dados, modelos e relacionamentos.
- **Maria Luiza:** interfaces, formulários e telas de cadastro.
- **Jullyane Sandra:** funcionalidades de empréstimos, consultas e documentação.

## 3. Tecnologias utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy ORM
- SQLite
- HTML
- CSS
- Jinja2
- Pytest

## 4. Entidades do sistema

O sistema utiliza quatro modelos:

- **Autor:** armazena os dados dos autores, como nome e nacionalidade.
- **Livro:** armazena título, gênero, ano de publicação e o autor relacionado.
- **Leitor:** armazena nome e e-mail dos leitores.
- **Empréstimo:** registra o leitor, o livro, a data do empréstimo e a data da devolução.

## 5. Relacionamentos

### Relacionamento 1:N — Autor e Livro

Um autor pode possuir vários livros cadastrados, mas cada livro está relacionado a um único autor.

Esse relacionamento é feito por meio da chave estrangeira `autor_id`, presente no modelo Livro.

### Relacionamento N:N — Leitor e Livro

Um leitor pode pegar vários livros emprestados e um mesmo livro pode ser emprestado a diferentes leitores ao longo do tempo.

Esse relacionamento é representado pelo modelo intermediário `Emprestimo`, que armazena as chaves estrangeiras `leitor_id` e `livro_id`, além das datas do empréstimo e da devolução.

## 6. Funcionalidades

O sistema possui as seguintes funcionalidades:

- Cadastro e consulta de autores.
- Cadastro, edição, consulta e exclusão de livros.
- Cadastro, edição, consulta e exclusão de leitores.
- Registro de novos empréstimos.
- Listagem dos empréstimos realizados.
- Consulta de empréstimos por livro e por leitor.
- Verificação de empréstimos pendentes, evitando que um livro ainda não devolvido seja emprestado novamente.
- Registro da devolução com a data correspondente.
- Exclusão de registros de empréstimos.
- Associação entre autores e livros.
- Associação entre leitores e livros por meio dos empréstimos.

## 7. Estrutura do projeto

```text
projeto_sistema_biblioteca/
│
├── app.py
├── database.py
├── seed.py
├── requirements.txt
├── README.md
├── DIARIO.md
│
├── controllers/
│   ├── __init__.py
│   ├── autores.py
│   ├── livros.py
│   ├── leitores.py
│   └── emprestimos.py
│
├── models/
│   ├── __init__.py
│   ├── autor.py
│   ├── livro.py
│   ├── leitor.py
│   └── emprestimo.py
│
├── templates/
│   ├── base.html
│   ├── inicio.html
│   ├── autores/
│   ├── livros/
│   ├── leitores/
│   └── emprestimos/
│
├── static/
│   └── style.css
│
└── tests/
    ├── test_relacionamento_autor_livro.py
    └── test_relacionamento_leitor_livro.py
```

## 8. Como instalar e executar

### Pré-requisitos

- Python 3 instalado.
- Git instalado.

### Clonar o repositório

```bash
git clone https://github.com/m4rcosgustavo/projeto_sistema_biblioteca.git
```

Entre na pasta do projeto:

```bash
cd projeto_sistema_biblioteca
```

### Criar o ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```powershell
.venv\Scripts\activate
```

### Instalar as dependências

Com o ambiente virtual ativado, execute:

```bash
pip install -r requirements.txt
```

### Criar e popular o banco de dados

O banco de dados SQLite é configurado na aplicação. As tabelas são criadas automaticamente quando a aplicação é inicializada, por meio de `db.create_all()`.

O arquivo `seed.py` permite cadastrar dados iniciais para facilitar os testes e a demonstração do sistema.

Para executar o cadastro dos dados iniciais, utilize:

```bash
python seed.py
```

O script verifica os registros existentes para evitar cadastros duplicados.

### Executar a aplicação

Para iniciar o sistema, execute:

```bash
python app.py
```

Depois, acesse no navegador:

http://127.0.0.1:5000/

### Executar os testes automatizados

Para executar os testes de relacionamento, utilize:

```bash
python -m pytest -v
```

Os testes verificam:

- Se um autor pode possuir vários livros.
- Se um leitor pode pegar vários livros emprestados e se um livro pode estar associado a diferentes leitores.

## 9. Testes realizados

Durante a revisão do projeto, foram executados testes automatizados utilizando Pytest.

Resultado obtido:

```text
2 passed
```

Os dois testes foram aprovados:

- `test_autor_pode_ter_varios_livros`
- `test_leitor_pode_ter_varios_livros_e_livro_pode_ter_varios_leitores`

Também foram realizadas verificações manuais das telas de livros e empréstimos pelo navegador.

## 10. Principais dificuldades

Durante o desenvolvimento, foram encontrados problemas na organização dos arquivos de listagem e formulário de empréstimos. O conteúdo da listagem estava no arquivo do formulário, fazendo com que a tela de novo empréstimo não abrisse corretamente.

Também foi necessário conferir o funcionamento das rotas, dos relacionamentos e da persistência dos registros no banco de dados.

As correções foram realizadas separando corretamente os templates, conferindo os endereços das rotas e testando o cadastro e a listagem dos empréstimos.

Outra etapa importante foi verificar a integração dos controllers com a aplicação Flask e executar testes automatizados para conferir os relacionamentos entre as entidades.
