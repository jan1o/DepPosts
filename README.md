# DepPosts 

O DepPosts é uma aplicação que mantém posts de autores, vinculados há alguma revista.

## Documento de Visão  

O documento de visão está disponível
[Nesse link](https://github.com/jan1o/DepPosts/blob/master/docs/REQUISITOS.md).

## Lista de User Stories

O documento com a lista de USs está disponível
[Nesse link](https://github.com/jan1o/DepPosts/blob/master/docs/LISTA_USER_STORIES.md).  

## Preparando o Ambiente  

Recomendamos o uso de um ambiente virtual para que se possa ter o seu próprio conjunto independente de pacotes Python instalados. 

Use o comando abaixo para instalar o `virtualenv`:  
`$ pip install virtualenv`  

Para criar um ambiente virtual, use o comando:  
`$ virtualenv  venv`  

_Até aqui o ambiente virtual foi criado, e dentro dele poderão ser instalados quais pacotes sem que se interfira no SO de uma forma geral._

Uma vez criando o ambiente virtual, use o comando abaixo para inicializa-lo:   
`$ venv\Scripts\activate.bat`  

_Acessando a pasta criada com o comando anterior e executando o script `activate` referente ao seu sistema operacional. O terminal indicara o uso do ambiente virtual da seguinte forma:_  
`(<ambiente virtual>) C:\caminho\para\o\seu\projeto>`  

Uma vez dentro do ambiente, instale os pacotes necessários ao projeto com o `pip`:  
`$ pip install -r requirements.txt`  

Até aqui, todos os passos executados preparam o ambiente para execução do projeto.

## Inicializando o Projeto  

Para inicializar o projeto, primeiro se faz necessário executar as migrações do mesmo, com o comando:  
`$ python manage.py makemigrations`  

_O comando `makemigrations` analisa se foram feitas mudanças nos modelos e, em caso positivo, cria novas migrações (Migrations) para alterar a estrutura do seu banco de dados, refletindo as alterações feitas._  

Após isso, execute o comando `migrate`:  
`$ python manage.py migrate`  

_Com a execução do `migrate`, o Django irá criar as diversas tabelas dos outros apps no banco de dados e as tabelas definidas nos arquivos de modelo._

Talvez seja necessário criar um super usuário, se a ideia for ir mais a fundo no projeto, para isso, use o comando:  
`$ python manage.py createsuperuser`  

Feito todos os passos anteriores, apenas execute o comando abaixo e seja para url indicada:  
`$ python manage.py runserver`.  

# Continuos Integration
Resumo sobre CI/CD está disponível
[Nesse link](https://github.com/jan1o/DepPosts/blob/master/docs/RESUMO_CI-CD.md).

Manual de Implantação do Django CI está disponivel
[Nesse link](https://github.com/jan1o/DepPosts/blob/master/docs/MANUAL_IMPLANTACAO_CI.md). 

Arquivo do Django CI está disponível
[Nesse link](https://github.com/jan1o/DepPosts/blob/master/docs/django.yml).

# Testes de Mutação

Resumo sobre testes de mutação está disponível
[Nesse link](https://github.com/jan1o/DepPosts/blob/master/docs/RESUMO_TESTES_MUTACAO.md).

Manual de implantação dos testes de mutação está disponível
[Nesse link](https://github.com/jan1o/DepPosts/blob/master/docs/MANUAL_IMPLANTA%C3%87%C3%83O_TESTES_MUTACAO.md).

`Fim 💓`.
