# Sistema de Biblioteca

Projeto desenvolvido em grupo para a disciplina de Programação para Servidores Web (PSI), utilizando Python, Flask, SQLAlchemy e SQLite.

## 1. Tema e objetivo

O tema escolhido foi **Sistema de Biblioteca**. O objetivo é organizar autores, livros e leitores, permitindo registrar empréstimos, consultar os registros e controlar as devoluções.

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

## 4. Entidades do sistema

O sistema utiliza quatro modelos:

- **Autor:** armazena os dados dos autores.
- **Livro:** armazena título, gênero, ano de publicação e autor relacionado.
- **Leitor:** armazena nome e e-mail dos leitores.
- **Empréstimo:** registra o leitor, o livro, a data do empréstimo e a data da devolução.

## 5. Relacionamentos

### Relacionamento 1:N — Autor e Livro

Um autor pode possuir vários livros cadastrados, mas cada livro está relacionado a um autor. Esse relacionamento é feito por meio da chave estrangeira `autor_id` no modelo Livro.

### Relacionamento N:N — Leitor e Livro

Um leitor pode pegar vários livros emprestados e um mesmo livro pode ser emprestado a diferentes leitores ao longo do tempo.

Esse relacionamento é representado pelo modelo intermediário `Emprestimo`, que armazena as chaves estrangeiras `leitor_id` e `livro_id`, além das datas do empréstimo e da devolução.

## 6. Funcionalidades

- Cadastro e consulta de autores.
- Cadastro, edição e consulta de livros.
- Cadastro, edição e consulta de leitores.
- Registro de empréstimos.
- Listagem dos empréstimos realizados.
- Consulta de empréstimos por livro e por leitor.
- Verificação de empréstimos pendentes, evitando registrar novamente um livro que ainda não foi devolvido.
- Registro da devolução com a data correspondente.
- Exclusão de registros de empréstimos.

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

### Instalar as dependências

No terminal, dentro da pasta do projeto, execute:

```bash
pip install -r requirements.txt
```

### Criar o banco de dados

O banco SQLite é configurado na aplicação. As tabelas são criadas automaticamente quando a aplicação é inicializada, por meio de `db.create_all()`.

O arquivo `seed.py` está reservado para dados iniciais. Como não há dados iniciais implementados nele, os primeiros autores, livros e leitores devem ser cadastrados pelas telas do sistema.

### Executar a aplicação

```bash
python app.py
```

Depois, acesse no navegador:

```text
http://127.0.0.1:5000
```

## 9. Principais dificuldades

Durante o desenvolvimento, foram encontrados problemas na organização dos arquivos de listagem e formulário de empréstimos. O conteúdo da listagem estava no arquivo do formulário, fazendo com que a tela de novo empréstimo não abrisse corretamente.

Também foi necessário conferir o funcionamento das rotas, dos relacionamentos e da persistência dos registros no banco de dados.

As correções foram realizadas separando corretamente os templates, conferindo os endereços das rotas e testando o cadastro e a listagem dos empréstimos.

## 10. Declaração de autoria e uso de IA

O projeto foi desenvolvido em grupo, com divisão de tarefas entre os integrantes. Foram utilizadas ferramentas de IA como apoio para tirar dúvidas, auxiliar na identificação de erros e organizar a documentação. Os integrantes devem revisar o código e compreender as funcionalidades que desenvolveram, sendo responsáveis pelo trabalho entregue.