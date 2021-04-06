# Passo a passo
## Configurar a integração contínua com Github Actions, usando Django CI.

- 1: Acesse o seu repositório no github.
- 2: Entre na parte de Actions do seu repositório.
- 3: Localize o Django CI e clique em Set up this workflow.
- 4: Clique em Start Commit e marque a opção de "create a new Branch from this commit and start a pull request".
- 5: Clique em Propose new file.

Pronto! O seu repositório já está configurado com o Django CI.

## Explicando o [django.yml]()

O arquivo django.yml, usando pelo Actions do GitHub é uma forma de fácil leitura humana (yml == Ain’t Markup Language <> Não é uma linguagem de marcação). Basicamente, é um padrão de dados hierárquicos e legível por humanos que pode ser usado em conjunto com todas as linguagens de programação, e usualmente é utilizado para armazenar arquivos de configuração.

A seguir o nosso django.yml:

```yaml
name: Django CI

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      max-parallel: 4
      matrix:
        python-version: [3.7, 3.8, 3.9]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run Tests
      run: |
        python manage.py test
```

A tag `name` serve apenas para dizer o nome do que aqui é chamado de `Action` (do GitHub Actions), o seu funcionamento começa a partir da tag `on`, que quer dizer basicamente um "quando", seguindo um passo a passo, oq ue ta dentro da tag on quer dizer:

"Quando ocorrer um `push` em alguma das `branches` desta lista, que no case tema apenas a `master` ou um `pull_request` em algumas das `branches` desta outra lista (que também tem apenas a `master`, mas que poderia ter outras branches), execute o `jobs` a seguir.".

Ao iniciar o job de fato, com o `build`, todo o processo deve ser realizado em uma VM `runs-on` ubuntu-latest.

O bloco dentro da tag `strategy` é uma definição bastante crítica, principalmente em projeto médios/grandes, ela define quantas vezes, ao mesmo tempo, essa action pode ocorrer, com o `max-parallel` em 4, a `matrix` com uma lista de `python-versions` nos diz quais versões do python devem ser usadas no projeto como um todo. Resumidamente, esse bloco diz o seguinte:  

##### `Limite as execuções dessa action em no máximo 4 usando apenas essas versões do python para a execução da action.`  

Os `steps` são literalmente os passos que serão executados, nesses passos, são usados (`uses`) determinados pacotes, é interessante sempre nomear os passos executados, por isso temos `name`s dentro de toda a actions (ela também é refletida na visualização da acton no próprio console da guia Action do repositório).

Logo após o `uses: actions/setup-python@v2`, vemos o `with` fazendo referência direta a matrix de versões do python (`python-version: [3.7, 3.8, 3.9]`) citada anteriormente.

Por fim, se tem a instalação dos pacotes do projeto, usando o comando `run` seguindo de um comando que normalmente usaríamos no terminal da nossa maquina local, mas nesse caso, em um ambiente controlado e de forma automatizada.

A seguir, o mesmo django.yml, comentado:

```yaml

# nome da action
name: Django CI

# condição de execução
# execute apenas em casos de push ou pull request na branche master
on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

# execução
jobs:
  build:
    # ambiente onde a action será executada
    runs-on: ubuntu-latest
    strategy:
      # limite de actions funcionando em paralelo
      max-parallel: 4
      # versões do python para o projeto
      matrix:
        python-version: [3.7, 3.8, 3.9]
  
    # passos que devem ser executados
    steps:
      # pacote/dependência necessária
    - uses: actions/checkout@v2
      # nome do passo do step
    - name: Set up Python ${{ matrix.python-version }}
      # pacote/dependência necessária
      uses: actions/setup-python@v2
      # usando a versão do python
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install Dependencies
      # comando de terminal
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run Tests
      # comando de terminal
      run: |
        python manage.py test
```

 Fim 💓👨‍💻