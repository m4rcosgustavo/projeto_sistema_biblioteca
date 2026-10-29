# Diário de Desenvolvimento — Sistema de Biblioteca

## Registro 1 — Quarta-feira (28/10/2026)

**Data:** 28/10/2026
**Aluno:** Marcos Gustavo da Silva Araújo

**O que foi feito:** Organização inicial do projeto, preparação da estrutura MVC e configuração dos arquivos principais da aplicação Flask e do banco de dados SQLite.

**Dificuldade encontrada:** Organizar a aplicação em camadas e definir uma estrutura que permita integrar os modelos, os controllers e as interfaces desenvolvidas pelos integrantes do grupo.

**Como resolvi:** Separei as responsabilidades entre os arquivos e as pastas do projeto, preparando a estrutura para facilitar a integração das partes desenvolvidas pelo grupo.

**Próximo passo:** Integrar as rotas da aplicação, alinhar a configuração do banco de dados com os modelos e verificar se o sistema funciona corretamente.

## Registro 2 — Quarta-feira (28/10/2026)
**Aluno:** Heloisa Pereira

**O que foi feito:** Iniciei o desenvolvimento da camada de dados do Sistema de Biblioteca, organizando os modelos de Autor, Livro, Leitor e Empréstimo com SQLAlchemy. Também participei da configuração inicial do banco de dados SQLite e executei a aplicação para verificar seu funcionamento.

**Dificuldade encontrada:** Ocorreu um erro na inicialização do banco de dados porque a função db.init_app(app) estava sendo chamada duas vezes no arquivo app.py.

**Como resolvi:** Analisei o código e corrigi a inicialização duplicada, mantendo apenas uma chamada de db.init_app(app). Depois, executei novamente a aplicação e confirmei que ela iniciou corretamente.

**Próximo passo:** Implementar e testar o relacionamento 1 entre Autor e Livro, conferir as chaves estrangeiras e avançar na preparação da tabela intermediária de empréstimos.

## Registro 3 — Quarta-feira (28/10/2026)
**Aluno:** Maria Luiza

**O que foi feito:** Desenvolvi o template base da aplicação do Sistema de Biblioteca, criando a estrutura inicial da interface com cabeçalho, menu de navegação, área de conteúdo e rodapé. Também preparei a estilização com CSS para padronizar a aparência das páginas e ajustei a rota inicial do Flask para renderizar o template da página inicial.

**Dificuldade encontrada:** Os arquivos base.html e style.css estavam vazios, então foi necessário preparar a estrutura inicial da interface.

**Como resolvi:** Criei o template base utilizando HTML e Jinja2, adicionei os estilos em CSS e preparei a página inicial para utilizar o template.

**Próximo passo:** Desenvolver as telas de cadastro, edição e listagem de autores, livros e leitores, integrando-as às rotas da aplicação.

## Registro 4 — Quarta-feira (28/10/2026)
**Aluno:** Jullyane Sandra

**O que foi feito:** Realizei o planejamento inicial da minha parte no Sistema de Biblioteca e comecei a documentação do projeto no README.md, descrevendo o objetivo, as tecnologias utilizadas, a estrutura dos arquivos e as instruções para executar a aplicação.

**Dificuldade encontrada:** Organizar as informações do projeto enquanto algumas funcionalidades ainda estavam em desenvolvimento.

**Como resolvi:** Consultei os arquivos existentes no repositório e organizei as informações para documentar a estrutura e as funcionalidades previstas para o sistema.

**Próximo passo:** Preparar o fluxo de empréstimos, incluindo consultas de livros e leitores, registro e remoção de empréstimos.

## Registro 5 — Quinta-feira (29/10/2026)

**Aluno:** Marcos Gustavo da Silva Araújo

**O que foi feito:** Dei continuidade à estrutura MVC do Sistema de Biblioteca, integrando o controlador de autores à aplicação Flask. Criei a rota de listagem de autores e o template correspondente, aproveitando a estrutura visual já existente no projeto. Também verifiquei o registro da rota e executei a aplicação para testar seu funcionamento.

**Dificuldade encontrada:** Os Blueprints estavam definidos, mas ainda não havia uma rota implementada para listar os autores. Também foi necessário conectar o controlador à aplicação e preparar o template utilizado na listagem.

**Como resolvi:** Implementei a rota `GET /autores/`, utilizei o modelo `Autor` para consultar os registros no banco de dados e criei o template `templates/autores/lista.html`. Depois, conferi as rotas registradas pelo Flask e testei a aplicação no navegador.

**Próximo passo:** Dar continuidade à integração dos controladores de livros, leitores e empréstimos, testar as funcionalidades e verificar a integração com as demais partes do sistema.

## Registro 6 — Quinta-feira (29/10/2026)

**Aluno:** Heloisa Pereira

**O que foi feito:** Criei um teste automatizado para verificar o relacionamento 1:N entre Autor e Livro, confirmando que um autor pode possuir vários livros associados.

**Dificuldade encontrada:** Era necessário verificar se o relacionamento funcionava com mais de um livro para o mesmo autor.

**Como resolvi:** Utilizei um teste com dois livros vinculados ao mesmo autor e verificações das chaves estrangeiras e da coleção de livros do autor.

**Próximo passo:** Implementar e testar o relacionamento entre Leitor, Livro e Empréstimo.
