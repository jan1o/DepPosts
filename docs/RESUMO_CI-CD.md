# CI e CD
CI e CD são dois acrônimos frequentemente usados ​​em  práticas modernas de desenvolvimento e  DevOps .
CI significa integração contínua , uma prática recomendada DevOps fundamental em que os desenvolvedores frequentemente mesclam alterações de 
código em um repositório central onde compilações e testes automatizados são executados. Mas o CD pode significar entrega contínua ou implantação contínua. 

# Integração Contínua (CI)
Os desenvolvedores que praticam a integração contínua mesclam suas alterações de volta ao branch principal com a maior freqüência possível. 
As alterações do desenvolvedor são validadas criando um build e executando testes automatizados em relação ao build. Ao fazer isso, 
você evita desafios de integração que podem acontecer ao esperar o dia do lançamento para mesclar as alterações no branch de lançamento.

A integração contínua coloca grande ênfase na automação de teste para verificar se o aplicativo não é interrompido sempre que novos commits 
são integrados ao branch principal.

## Custos
- Sua equipe precisará escrever testes automatizados para cada novo recurso, melhoria ou correção de bug.
- Você precisa de um servidor de integração contínua que pode monitorar o repositório principal e executar os testes automaticamente para cada novo commit enviado.
- Os desenvolvedores precisam mesclar suas alterações sempre que possível, pelo menos uma vez por dia.

## Vantagens
- Menos bugs são enviados para a produção à medida que as regressões são capturadas antecipadamente pelos testes automatizados.
- Construir a versão é fácil, pois todos os problemas de integração foram resolvidos antecipadamente.
- Menos troca de contexto, pois os desenvolvedores são alertados assim que interrompem a compilação e podem trabalhar para consertá-la antes de passarem para outra tarefa.
- Os custos de teste são reduzidos drasticamente - seu servidor de CI pode executar centenas de testes em questão de segundos.
- Sua equipe de QA gasta menos tempo testando e pode se concentrar em melhorias significativas na cultura de qualidade.

# Entrega Contínua (CD)
A entrega contínua  é uma extensão da integração contínua, uma vez que implanta automaticamente todas as alterações de código em um ambiente de teste e / ou produção após o estágio de construção. 

Isso significa que, além do teste automatizado, você tem um processo de liberação automatizado e pode implantar seu aplicativo a qualquer momento clicando em um botão.

Em teoria, com a entrega contínua, você pode decidir lançar lançamentos diários, semanais, quinzenais ou o que for mais adequado aos seus requisitos de negócios. 
No entanto, se você realmente deseja obter os benefícios da entrega contínua, deve implantar na produção o mais cedo possível para se certificar de que irá liberar 
pequenos lotes que são fáceis de solucionar em caso de problema.

## Custos
- Você precisa de uma base sólida para integração contínua e seu conjunto de testes precisa cobrir o suficiente de sua base de código.
- As implantações precisam ser automatizadas. O gatilho ainda é manual, mas uma vez que a implantação é iniciada, não deve haver necessidade de intervenção humana.
- Sua equipe provavelmente precisará adotar sinalizadores de recursos para que recursos incompletos não afetem os clientes em produção.

## Vantagens
- A complexidade da implantação de software foi eliminada. Sua equipe não precisa mais perder dias se preparando para um lançamento.
- Você pode liberar com mais frequência, acelerando assim o ciclo de feedback com seus clientes.
- Há muito menos pressão sobre as decisões de pequenas alterações, o que estimula a iteração mais rápida.

# Referências
PITTET, Sten. Integração contínua vs. entrega contínua vs. implantação contínua. Atlassian, c2021. Disponível em: <https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment>. Acesso em: 05 de Abril de 2021.



