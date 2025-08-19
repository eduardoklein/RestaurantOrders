# Restaurant Orders

Projeto desenvolvido para gerenciamento de pedidos, controle de estoque e análise de restrições alimentares em um restaurante.

## Sumário

-   [Descrição](#descrição)
-   [Estrutura do Projeto](#estrutura-do-projeto)
-   [Como Executar](#como-executar)
-   [Testes](#testes)
-   [Autores](#autores)

## Descrição

O Restaurant Orders é uma aplicação Python que permite gerenciar pedidos de pratos, controlar o estoque de ingredientes e consultar restrições alimentares dos pratos do cardápio. O projeto foi desenvolvido como parte do curso da Trybe, com foco em manipulação de dados, testes automatizados e boas práticas de desenvolvimento.

## Estrutura do Projeto

```
.editorconfig
.gitignore
dev-requirements.txt
pyproject.toml
README.md
requirements.txt
setup.cfg
setup.py
data/
    inventory_base_data.csv
    menu_base_data.csv
src/
    __init__.py
    app.py
    models/
        __init__.py
        dish.py
        ingredient.py
    services/
        __init__.py
        inventory_control.py
        menu_builder.py
        menu_data.py
tests/
    __init__.py
    dish/
        __init__.py
        test_dish.py
    ingredient/
        __init__.py
        test_ingredient.py
```

-   **Pasta `src/`**: contém o código principal da aplicação.
-   **Pasta `models/`**: modelos de dados para ingredientes e pratos.
-   **Pasta `services/`**: regras de negócio e manipulação de dados.
-   **Pasta `data/`**: arquivos CSV com dados de estoque e cardápio.
-   **Pasta `tests/`**: testes automatizados para os módulos principais.

## Como Executar

Instale as dependências:

```sh
pip install -r requirements.txt
```

Para ambiente de desenvolvimento, instale também:

```sh
pip install -r dev-requirements.txt
```

Execute a aplicação FastAPI:

```sh
uvicorn src.app:app --reload
```

Acesse a documentação interativa em [http://localhost:8000/docs](http://localhost:8000/docs).

## Testes

Para rodar os testes automatizados:

```sh
pytest
```

Os testes estão localizados na pasta `tests/`.

## Autores

-   **Eduardo Klein** - Desenvolvimento dos módulos em `src/models/`, `src/services/` e testes em `tests/`.
-   **Trybe** - Fornecimento dos dados, estrutura inicial do projeto e arquivos de configuração.

Este projeto foi desenvolvido como parte do
