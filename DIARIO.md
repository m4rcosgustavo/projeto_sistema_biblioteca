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

## Registro 7 — Sexta-feira (30/10/2026)

**Data:** Marcos Gustavo da Silva Araújo

**O que foi feito:** Realizei a integração dos controllers de autores, livros, leitores e empréstimos com a aplicação Flask. Verifiquei o registro das rotas, executei o sistema e testei as páginas pelo navegador. Também realizei testes de cadastro e edição de autores.

**Dificuldade encontrada:** Conferir se todos os controllers estavam integrados corretamente e se as rotas estavam funcionando.

**Como resolvi:** Verifiquei os imports e os Blueprints, executei a aplicação e testei as funcionalidades pelo navegador. Todas as páginas testadas funcionaram normalmente.

**Próximo passo:** Realizar a revisão geral do sistema, verificar as funcionalidades de empréstimos e corrigir possíveis problemas antes da entrega do projeto.


## 30/10/2026 — Maria Luiza

**O que foi feito:**
Desenvolvimento das interfaces de empréstimos, criação da tela de listagem, organização do formulário e integração com os modelos de livros, leitores e empréstimos.

**Dificuldade encontrada:**
Organizar a exibição dos dados relacionados entre leitores, livros e empréstimos.

**Como resolvi:**
Utilizei os relacionamentos existentes nos modelos SQLAlchemy para exibir as informações nas telas.

**Próximo passo:**
Testar as interfaces integradas à funcionalidade de registro de empréstimos.

## Registro 8 — Sexta-feira (30/10/2026)

**Aluno:** Maria Luiza

**O que foi feito:** Implementei as funcionalidades de empréstimos no sistema. Desenvolvi o registro de novos empréstimos, a listagem dos registros e as consultas por livro e leitor. Também adicionei a verificação para impedir que um livro com empréstimo pendente seja emprestado novamente. Depois, implementei as opções de devolução, com registro da data, e exclusão dos empréstimos.

**Dificuldade encontrada:** Tive dificuldade para fazer a tela de novo empréstimo abrir corretamente e para fazer os registros aparecerem na listagem. Também encontrei problemas na organização dos arquivos HTML.

**Como resolvi:** Verifiquei as rotas e os templates e identifiquei que o conteúdo da listagem estava no arquivo do formulário. Separei os conteúdos nos arquivos corretos, ajustei as funcionalidades e testei novamente o sistema. Depois, confirmei o funcionamento do registro e da listagem dos empréstimos.

**Próximo passo:** Atualizar o README.md e o DIARIO.md, revisar a documentação e conferir o projeto antes da entrega.

## Registro 9 — Sábado (31/10/2026)

**Aluno:** Maria Luiza

**O que foi feito:** Atualizei a documentação do Sistema de Biblioteca. Organizei o README.md com a descrição do projeto, integrantes, responsabilidades, tecnologias, entidades, relacionamentos, funcionalidades e instruções para executar a aplicação. Também atualizei o DIARIO.md, registrando as atividades realizadas durante o desenvolvimento. Revisei os arquivos relacionados à minha parte e conferi o funcionamento das funcionalidades de empréstimos.

**Dificuldade encontrada:** Organizar as informações de forma clara e registrar as atividades sem deixar de considerar as dificuldades encontradas durante o desenvolvimento.

**Como resolvi:** Consultei o plano de trabalho, os arquivos do projeto e as funcionalidades implementadas para atualizar a documentação de acordo com o desenvolvimento realizado.

**Próximo passo:** Finalizar a conferência geral do projeto junto com os demais integrantes e verificar se todos os arquivos e alterações estão disponíveis no GitHub.

## Registro 10 — Sábado (31/10/2026)

**Data:** 31/10/2026

**Aluno:** Marcos Gustavo da Silva Araújo

**O que foi feito:** Realizei a revisão geral da integração do Sistema de Biblioteca. Executei a aplicação e conferi as telas de livros e empréstimos, verificando a apresentação dos registros e as funcionalidades disponíveis. Também executei os testes automatizados dos relacionamentos entre Autor e Livro e entre Leitor e Livro.

**Dificuldade encontrada:** Foi necessário verificar se os dados cadastrados estavam sendo apresentados corretamente e conferir se os relacionamentos do banco de dados estavam funcionando como esperado.

**Como resolvi:** Executei o arquivo `seed.py` para popular o banco de dados, conferi as telas pelo navegador e executei os testes com `python -m pytest -v`, obtendo dois testes aprovados.

**Próximo passo:** Finalizar a conferência dos arquivos do projeto e realizar o commit final no GitHub.

## Registro 11 — Sábado (31/10/2026)

**Atividade relacionada à responsabilidade de:** Heloisa Pereira

**Responsável pela execução da revisão:** Marcos Gustavo da Silva Araújo

**O que foi feito:** Realizei a conferência dos testes automatizados dos relacionamentos do banco de dados, verificando os arquivos responsáveis pelos relacionamentos 1:N entre Autor e Livro e N:N entre Leitor e Livro.

**Dificuldade encontrada:** Verificar se os testes estavam organizados corretamente e se contemplavam os relacionamentos definidos para o sistema.

**Como resolvi:** Conferi os arquivos da pasta `tests` diretamente no GitHub e considerei também a execução anterior dos testes, que apresentou dois testes aprovados.

**Próximo passo:** Manter os testes disponíveis para futuras verificações do funcionamento do banco de dados.

## Registro 12 — Sábado (31/10/2026)

**Atividade relacionada à responsabilidade de:** Maria Luiza

**Responsável pela execução da revisão:** Marcos Gustavo da Silva Araújo

**O que foi feito:** Realizei a revisão da estrutura das interfaces do Sistema de Biblioteca, conferindo a organização dos templates de autores, livros, leitores e empréstimos, além dos arquivos `base.html` e `inicio.html`.

**Dificuldade encontrada:** Verificar se todas as áreas do sistema estavam organizadas e disponíveis na estrutura do projeto.

## Registro 13 — Sábado (31/10/2026)

**Atividade relacionada à responsabilidade de:** Jullyane Sandra

**Responsável pela execução da revisão:** Marcos Gustavo da Silva Araújo

**O que foi feito:** Realizei a conferência dos arquivos relacionados à documentação e à preparação dos dados iniciais do Sistema de Biblioteca, incluindo `README.md`, `DIARIO.md` e `seed.py`.

**Dificuldade encontrada:** Conferir se as informações documentadas correspondiam às funcionalidades e à estrutura atual do projeto.

**Como resolvi:** Revisei a documentação, conferi o arquivo de povoamento do banco de dados e considerei a execução anterior do `seed.py`, que apresentou os registros cadastrados com sucesso.

**Próximo passo:** Manter a documentação atualizada e garantir que as instruções de execução e os dados iniciais estejam disponíveis para utilização do sistema.

**Como resolvi:** Acessei a pasta `templates` pelo GitHub e conferi a presença das pastas e dos arquivos responsáveis pelas interfaces.

**Próximo passo:** Manter as interfaces organizadas e verificar seu funcionamento sempre que forem realizadas novas alterações no sistema.
