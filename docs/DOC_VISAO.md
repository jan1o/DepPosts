# Documento de Visão

Documento construído a partido do Modelo BSI - Doc 001 - Documento de Visão que pode ser encontrado nesse [link](https://docs.google.com/document/d/1DPBcyGHgflmz5RDsZQ2X8KVBPoEF5PdAz9BBNFyLa6A/edit?usp=sharing). 

## Equipe e Definição de Papéis
|  ***Membro*** | ***Papel*** | ***E-Mail*** |
| - | - | - |
| Bruno | Programador, testador | brunno.linkin@gmail.com |
| Jorge | Programador, testador | jorgejunioufrn@gmail.com |
| Jânio | Programador, testador | juniorjanio2016@gmail.com |

## Matriz de Competências
|  ***Membro*** | ***Competências*** | 
| - | - |
| Bruno | Desenvolvedor, Python, PyCharm, Github |  
| Jorge | Desenvolvedor, Python, Github |
| Jânio | Desenvolvedor Java, Eclipse, Python, PyCharm, Github, C#, Unity |

## Perfis dos Usuários
O sistema poderá ser utilizado por diversos usuários. Temos os seguintes perfis/atores:
| Perfil | Descrição |
| - | - |
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
| RF008 - Cadastrar Usuário | Cadastrar um novo Usuário no sistema, com as informações de login, senha, nome, revista associada. | Cliente |
| RF009 - Alterar Usuário | Alterar as informações da conta cadastrada no sistema. | Cliente |
| RF010 - Deletar Usuário | Deletar a conta cadastrada no sistema. | Cliente |
| RF011 - Visualizar Dados Pessoais | Um usuário pode verificar seus dados pessoais cadastrados. | Cliente |
| RF012 - Listar Usuários | Listar todos os Usuários cadastrados no sistema. | Administrador |
| RF013 - Visualizar especificação de Usuário | Visualizar as informações de um usuário em específico. | Administrador |
| RF014 - Cadastrar Revista | Cadastrar uma revista no sistema. Uma revista possui  nome, login, senha | Revista |
| RF015 - Alterar dados de Revista. | Alterar seus dados cadastrados no sistema. | Revista |
| RF016 - Deletar Revista. | Excluir seu cadastro no sistema. | Revista |
| RF017 - Visualizar Revistas. | Visualizar lista de todas as Revistas cadastradas no sistema | Revista/Usuário |
| RF018 - Visualizar especificação de uma Revista. | Visualizar os dados públicos de uma Revista cadastrada no sistema. | Revista/Usuário |


## Lista de Requisitos Não-Funcionais
 
| Requisito | Descrição |
| - | - |
| RNF001 - Deve ser acessível via navegador | Deve abrir perfeitamente no Chrome. |

## Modelo Conceitual

![alt text](https://github.com/jan1o/DepPosts/blob/master/docs/images/diagra_classes.jpeg?raw=true)


## Riscos

Tabela com o mapeamento dos riscos do projeto, as possíveis soluções e os responsáveis.

|  ***Data*** | ***Risco*** | ***Prioridade*** | ***Responsável*** | ***Status*** | ***Providência/Solução*** |
| - | - | - | - | - | - |
| 21/03/2021 | Não aprendizado das ferramentas utilizadas pelos componentes do grupo | Alta | Todos | Vigente | Reforçar estudos sobre as ferramentas e aulas com a integrante que conhece a ferramenta |
| 21/03/2021 | Divisão de tarefas mal sucedida | Baixa | Gerente | Vigente | Acompanhar de perto o desenvolvimento de cada membro da equipe |
| 21/03/2021 | Implementação de protótipo com as tecnologias | Alto | Todos | Vigente | Encontrar tutorial com a maioria da tecnologia e implementar um caso base do sistema |
| 21/03/2021 | Prazo de entrega não ser obedecido | Alto | Todos | Vigente | Se esforçar para garantir a entrega do projeto no prazo definido. |

