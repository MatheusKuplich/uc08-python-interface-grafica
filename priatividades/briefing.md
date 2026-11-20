# Pedido recebido

O cliente precisa de um sistema para controlar os empréstimos de equipamentos, verificar o que está disponíveis e registrar quando são retirados e devolvidos. Ele também quer que o sistema seja rápido e seguro, mas ainda, sem nenhuma explicação do que espera nesses pontos.


## Problema e resultado desejado

- Problema observado no cenário: dificuldade para saber quais equipamentos estão disponíveis, os emprestados ou os que já foram devolvidos.

- Quem utilizará: funcionário que irá organizar e acompanhar os empréstimos.

- Resultado desejado: facilitar a consulta dos equipamentos disponíveis e o controle das saídas e devoluções.

- Dentro do escopo inicial: registrar os equipamentos, consultar a disponibilidade deles e anotar empréstimos e devoluções.

- Fora do escopo inicial: conectar o sistema a outros e utilizar um banco de dados.

## Perguntas ao cliente

| ID  | Pergunta                                                             | Impacto da resposta                                | Resposta ou   |
|     |                                                                      |                                                    | “a confirmar” |
|-----|----------------------------------------------------------------------|----------------------------------------------------|---------------|
| D01 | Quais informações precisam ser registradas em cada empréstimo?       | Ajuda a definir quais campos o sistema deverá ter. |  a confirmar  |
| D02 | Quem poderá retirar e devolver os equipamentos?                      | Ajuda a definir quem poderá realizar essas ações.  |  a confirmar  |
| D03 | O que o sistema precisa ter para garantir a segurança dos registros? | Ajuda a definir os cuidados necessários para       |  a confirmar  |
|     |                                                                      | proteger as informações.                           |               |

## Decisões

| ID    | Decisão/hipótese                                       | Estado      | Evidência da confirmação |
|-------|--------------------------------------------------------|-------------|--------------------------|
| DEC01 | Usar os três equipamentos do CSV como exemplo inicial. | confirmada  | Orientação da atividade. |


## Revisão
O revisor consegue identificar o que foi pedido pelo cliente e o que ainda precisa ser decidido?

**Observação:** 
o briefing apresenta o objetivo do projeto e deixa claras as dúvidas que ainda precisam ser respondidas.

**Melhoria:** 
conversar com o cliente para definir quais informações serão registradas, quem poderá utilizar o sistema e o que ele considera rapidez e segurança.
Concluído quando o problema, o escopo, as três perguntas e as decisões pendentes estiverem claros.