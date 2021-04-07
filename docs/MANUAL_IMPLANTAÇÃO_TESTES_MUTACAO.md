# Manual de Implantação de Testes de Mutação

## Mutmut

Mutmut é um sistema de teste de mutação para Python, com um forte foco na facilidade de uso.
Alguns recursos de destaque:
- Os mutantes encontrados podem ser aplicados no disco com um comando simples, tornando muito fácil trabalhar com os resultados
- Lembra do trabalho que foi feito, para que você possa trabalhar de forma incremental
- Suporta todos os executores de teste (porque mutmut só precisa de um código de saída do comando de teste)
- Se você usar o executor de teste hammett <https://github.com/boxed/hammett> , poderá ir extremamente rápido! Há um manuseio especial para este corredor que tem alguns resultados bastante dramáticos.
- Pode usar dados de cobertura para fazer testes de mutação apenas nas linhas cobertas
- Batalha testada em bibliotecas reais por várias empresas

## Instalação e Execução

Para implantar o mutmut em seu projeto python que utiliza testes unitários pytest execute o seguinte comando no prompt:

`$
pip install mutmut
`

Para executar o mutmut, execute o comando no prompt:

`$
mutmut run
`

Dessa forma é gerado um arquivo nomeado .mutmut-cache com os resultados da execução. Neste arquivo são registrados os seguintes parâmetros:

🎉 Killed mutants. The gol is for everything to end up in this bucket.   
⏰ Timeout. Test suite took 10 times as long as the baseline so were killed.  
🤔 Suspicious.  Tests took a long time, but not long enough to be fatal.  
🙁 Survived. This means your tests needs to be expanded.  
🔇 Skipped.  Skipped.  


Você pode exibir os resultados da execução com o comando 

`$
mutmut show
`
