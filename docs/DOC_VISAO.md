# Documento de Visão

Documento construído a partido do Modelo BSI - Doc 001 - Documento de Visão que pode ser encontrado nesse [link](https://docs.google.com/document/d/1DPBcyGHgflmz5RDsZQ2X8KVBPoEF5PdAz9BBNFyLa6A/edit?usp=sharing). 

## Equipe e Definição de Papéis
| Requisitos envolvidos | | |
| - | - | - |
|  ***Membro*** | ***Papel*** | ***E-Mail*** |
| Bruno | Programador, testador | brunno.linkin@gmail.com |

## Matriz de Competências
| Requisitos envolvidos | |
| - | - |
|  ***Membro*** | ***Competências*** | 
| Bruno | Desenvolvedor, Python, PyCharm, Github |  

## Matriz de Competências 
O sistema poderá ser utilizado por diversos usuários. Temos os seguintes perfis/atores:
| Perfil | Descrição |
| - | - |
|  ***Membro*** | ***Competências*** | 
| Administrador | Este usuário realiza os cadastros base e pode realizar qualquer função. | 
| Usuário | Este usuário pode realizar cadastros de posts e manipular seus posts. |
| Revista | Este usuário pode realizar cadastro próprio e ter posts associados a si. |

## Lista de Requisitos Funcionais

| Requisitos envolvidos | | |
| - | - | - |
|  ***Requisito*** | ***Descrição*** | ***Ator*** |
| RF001 - Cadastrar Post | Cadastrar um post no sistema. Um Post possui título, autor, corpo, revista associada. | Cliente |
| RF002 - Alterar Post | Alterar um Post cadastrado por si. | Cliente |
| RF003 - Deletar Post  | Deletar um Post Cadastrado por si.  | Cliente |
| RF004 - Listar todos os Posts  | Listar todos os Posts cadastrados no sistema.  | Cliente  |
| RF005 - Listar todos os Posts próprios | Listar todos os Posts cadastrados por si.  | Cliente  |
| RF006 - Visualizar especificação de um Post | Visualizar as informações de qualquer Post cadastrado.  |  Cliente |
| RF007 - Visualizar especificação de um Post Próprio |  Visualizar as informações de um Post cadastrado por si próprio com a opção de deletar e alterar tal Post | Cliente  |

## Modelo Conceitual

![alt text](https://github.com/jan1o/DepPosts/blob/master/docs/images/diagra_classes.jpeg?raw=true)