# Testes de Mutação
Teste de mutação é um tipo de teste de software no qual certas declarações de código são alteradas/transformadas com a finalidade de verificar se os casos de testes já 
feitos são capazes de encontrar erros ou inconsistências no código-fonte base.

O seu objetivo é garantir a qualidade dos casos de uso de teste para que ele não falhe no código de fonte mutado. As alterações no “programa mutante” devem ser 
relativamente pequenas, para que não afetem o objetivo geral do programa. Testes de mutação também podem ser chamados de testes de estratégia baseados em falha, pelo fato 
de envolver a criação de uma falha no programa, tem características de testes de caixa branca e é usado principalmente em testes de unidade.

“Os testadores de mutação modificam (modificam) o código do seu projeto de pequenas maneiras e, em seguida, executam o conjunto de testes. Se todos os testes passarem, 
essa mutação é considerada um problema: um bug que seus testes não detectaram. A teoria é que uma mutação mudará o comportamento do seu programa, portanto, se o seu conjunto 
de testes estiver testando suficientemente perto, alguns testes devem falhar para cada mutação. Se uma mutação não produzir uma falha no teste, você precisará adicioná-la aos 
seus testes.” (Traduzido pelo autor) Disponível em: 
<https://nedbatchelder.com/blog/201903/mutmut.html>
