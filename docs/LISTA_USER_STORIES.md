# Documento Lista de User Stories  

Documento construído a partido do Modelo BSI - Doc 004 - Lista de User Stories que pode ser encontrado nesse [link](https://docs.google.com/document/d/1Ns2J9KTpLgNOpCZjXJXw_RSCSijTJhUx4zgFhYecEJg/edit?usp=sharing). 

## Descrição  

Este documento descreve os User Stories criados a partir da Lista de Requisitos no [Documento 001 - Documento de Visão](https://github.com/tacianosilva/eng-software-2/blob/master/docs/doc-visao.md).  Este documento também pode ser adaptado para descrever Casos de Uso. Modelo de documento baseado nas características do processo easYProcess (YP).

### User Story US01 - Manter Usuário

| US001 - Manter Usuário  |    |
| - | - |
| Descrição   | O sistema deve manter um cadastro de usuário que tem acesso ao sistema via login e senha. Um usuário tem os atributos … . O usuário pode registrar-se diretamente no sistema. Além disso, o usuário poderá alterar alguns dados, como o e-mail ou a senha.  |

| ***Requisitos envolvidos*** |  |
| ------ | ------ |
| RF008 | Cadastrar Usuário |
| RF009 | Alterar Usuário |
| RF010 | Excluir Usuário |
| RF011 | Consultar Usuário |
| RF012 | Listar Todos Usuários |
| RF013 | Visualizar especificação de Usuário |

| Prioridade | Essencial |
| ------ | ------ |
| ***Estimativa*** | ***8 horas*** |
| Tempo Gasto (real) |  |

| Testes de Aceitação (TA) | | | | |
| - | - | - | - | - |
| TA01.01 | Login de Usuário bem sucedido. | Usuário digita login e senha corretamente. | Sucesso ao logar. |  |
| TA01.02 | Login de usuário mal sucedido. | Usuário digita login ou senha incorreto. | Falha ao logar |  |
| TA01.03 | Alteração de dados pessoais. | Usuário Altera dados pessoais. | Dados alterados com sucesso. |  |
| TA01.04 | Exclusão de conta | Usuário deleta sua conta. | Usuário deletado com sucesso. |  |
| TA01.05 | Cadastrar conta bem sucedido | Usuário digita um login novo e único e uma senha. | Redirecionamento para tela de informações pessoais. |  |
| TA01.06 | Cadastrar conta mal sucedido 01 | Usuário digita um login já existente. | Usuário não cadastrado |  |
| TA01.07 | Cadastrar conta mal sucedido 02 | Usuário digita login válido, mas não digita senha. | Usuário não cadastrado. |  |
| TA01.08 | Cadastrar conta mal sucedido 03 | Usuário digita senha, mas não digita login. | Usuário não cadastrado. |  |
| TA01.09 | Informações pessoais cadastradas bem sucedido | Usuário digita todas as informações pessoais necessárias. | Usuário cadastrado com sucesso. |  |
| TA01.10 | Cadastrar informações pessoais mal sucedido. | Usuário não digita informações pessoais necessárias. | Usuário não cadastrado. |  |
| TA01.11 | Listar Todos Usuários | Administrador tenta visualizar usuários. | Lista de todos os Usuários exibida. |  |
| TA01.12 | Exibir um usuário | Administrador tenta visualizar os dados pessoais de um usuário | Dados pessoais (exceto senha) exibidos. |  |

### User Story US02 - Manter Posts  

| US002 - Manter Post  |    |
| - | - |
| Descrição   | O sistema deve manter todos os posts nele inseridos. Um usuário pode fazer, alterar, deletar e visualizar suas postagens. | 

| ***Requisitos envolvidos*** |  |
| ------ | ------ |
| RF001 | Cadastrar Post |
| RF002 | Alterar Post |
| RF003 | Deletar Post |
| RF004 | Listar todos os Posts |
| RF005 | Listar todos os Posts Próprios |
| RF006 | Visualizar Post |
| RF007 | Visualizar Posts Próprios |

| Prioridade | Essencial |
| ------ | ------ |
| ***Estimativa*** | ***8 horas*** |
| Tempo Gasto (real) |  |

| Testes de Aceitação (TA) | | | | |
| - | - | - | - | - |
| ***Código*** | ***Descrição*** | ***Passos*** | ***Resultado Esperado*** | ***Resultado Obtido*** |
| TA02.01 | Postagem bem sucedida. | Usuário digita os dados do post corretamente. | Sucesso ao postar conteúdo. | Sucesso ao postar |
| TA02.02 | Postagem mal sucedida | Usuário digita algum dado do post de forma incorreta | Falha ao postar conteúdo. |  |
| TA02.03 | Alteração de dados do post | Usuário altera dados do post. | Dados do post alterados com sucesso. |  |
| TA02.04 | Exclusão de post. | Usuário deleta um post. | Post deletado com sucesso |  |
| TA02.05 | Listar todos os posts | O usuário tenta ver todos os posts. | Lista de todos os posts. |  |
| TA02.06 | Listar todos os posts próprios | O usuário tenta ver todos os seus post | Lista de todos os posts próprios. |  |

### User Story US03 - Manter Revista

| US003 - Manter Revista | |
| - | - |
| Descrição | O sistema deve manter um cadastro de revista que tem acesso ao sistema via login e senha. Uma revista tem os atributos nome, login, e senha. A revista pode registrar-se diretamente no sistema. Além disso, a revista poderá alterar alguns de seus dados como o nome, e a senha. |

| ***Requisitos envolvidos*** |  |
| ------ | ------ |
| RF014 | Cadastrar Revista |
| RF015 | Alterar dados de Revista |
| RF016 | Deletar Revista |
| RF017 | Visualizar Revistas | 
| RF018 | Visualizar especificação de uma Revista |

| Prioridade | Essencial |
| ------ | ------ |
| ***Estimativa*** | ***6 horas*** |
| Tempo Gasto (real) |  |

| Testes de Aceitação (TA) | | | | |
| - | - | - | - | - |
| ***Código*** | ***Descrição*** | ***Passos*** | ***Resultado Esperado*** | ***Resultado Obtido*** |
| TA03.01 | Login de revista bem sucedido. | Revista digita login e senha corretamente. | Sucesso ao logar. |
| TA03.02 | Login de revista mal sucedido. | Revista digita login ou senha incorreta. | Falha ao logar |
| TA03.03 | Alteração de dados próprios. | Revista altera dados próprios. | Dados alterados com sucesso. |
| TA03.04 | Exclusão da revista. | Revista deleta sua conta. | Revista deletada com sucesso. |
| TA03.05 | Cadastrar revista bem sucedido | Revista digita um nome único, um login novo e único e uma senha. | Redirecionamento para tela de informações próprias. |
| TA03.06 | Cadastrar revista mal sucedido 01 | Revista digita um login já existente. | Revista não cadastrada. |
| TA03.07 | Cadastrar revista mal sucedido 02 | Revista digita login válido, mas não digita senha. | Revista não cadastrada. |
| TA03.08 | Cadastrar revista mal sucedido 03 | Revista digita senha, mas não digita login. | Revista não cadastrada. |
| TA03.09 | Cadastrar revista mal sucedido 04 | Revista digita senha e login válidos, mas não digita o nome válido. | Revista não cadastrada. |
| TA03.10 | Listar todas as revistas. | Administrador tenta visualizar revistas. | Lista de toda as revistas exibida. |
| TA03.11 | Exibir uma revista | Administrador tenta visualizar os dados de uma revista | Dados da revista (exceto senha) exibidos. |
