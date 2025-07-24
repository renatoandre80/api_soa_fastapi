# API de Gerenciamento de Usuários

Este é um projeto de API RESTful simples para gerenciar dados de usuários, implementado com FastAPI como framework web, SQLAlchemy para interação com o banco de dados e SQLite para persistência de dados.

## Funcionalidades

A API permite realizar as seguintes operações CRUD (Create, Read, Delete) em recursos de usuário:

- **Criação de Usuário**: Adiciona um novo usuário ao sistema com um nome e e-mail.
- **Leitura de Usuário**: Recupera informações de um usuário específico utilizando seu ID.
- **Deleção de Usuário**: Remove um usuário existente do sistema.
- **Validação de E-mail**: Garante que os e-mails dos usuários sejam únicos no banco de dados.

## Estrutura do Projeto

## Estrutura do Projeto

O projeto está organizado nos seguintes arquivos:
├── app/
│ ├── init.py
│ ├── crud.py
│ ├── database.py
│ ├── main.py
│ ├── models.py
│ └── schemas.py
├── .gitignore
├── README.md
├── requirements.txt
└── users.db (será gerado automaticamente)

### main.py:

- É o ponto de entrada principal da aplicação FastAPI.
- Define os endpoints da API (`/users/`, `/users/{user_id}`).
- Gerencia as dependências do banco de dados e as respostas HTTP.

### crud.py:

- Contém as funções de manipulação de dados (CRUD - Create, Read, Update, Delete) que interagem diretamente com o banco de dados.
- Define operações para buscar, criar e deletar usuários.

### models.py:

- Define o modelo de dados para a tabela `users` no banco de dados usando o ORM SQLAlchemy.
- Mapeia a classe `User` para a tabela correspondente, incluindo colunas como `id`, `name` e `email`.

### schemas.py:

- Define os schemas de validação e serialização de dados usando Pydantic.
- As classes `UserCreate` e `UserResponse` especificam a estrutura dos dados para as requisições (entrada) e respostas (saída) da API, respectivamente.

### database.py:

- Configura a conexão com o banco de dados SQLite (`users.db`).
- Cria a engine do SQLAlchemy e a SessionLocal para gerenciar as sessões do banco de dados.
- Fornece a função `get_db` para injeção de dependência das sessões do banco de dados no FastAPI.

### users.db:

- Este arquivo é o banco de dados SQLite que será criado automaticamente na primeira vez que a aplicação for executada, persistindo os dados dos usuários.

### requirements.txt:

- Lista todas as dependências Python necessárias para o projeto.

## Tecnologias Utilizadas

- **FastAPI**: Framework web moderno, rápido (de alto desempenho) para construir APIs com Python 3.7+ baseado em tipagem padrão do Python.
- **SQLAlchemy**: Um poderoso toolkit SQL e Object-Relational Mapper (ORM) para Python, que oferece um conjunto completo de padrões de persistência de dados de nível empresarial.
- **SQLite**: Um sistema de gerenciamento de banco de dados relacional contido em uma pequena biblioteca C. É muito usado em projetos pequenos e embarcados.
- **Pydantic**: Biblioteca para validação de dados e configurações usando type hints do Python. É amplamente utilizada pelo FastAPI para validação e serialização.
- **Uvicorn**: Um servidor ASGI rápido, usado para executar aplicações assíncronas como o FastAPI.

