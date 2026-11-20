# Requisitos, regras e aceite
O objetivo é definir o que o sistema precisa fazer, quais regras deve seguir e como podemos verificar se cada funcionalidade está funcionando como esperado.

Use o arquivo `requisitos.md` para registrar três requisitos funcionais, duas regras de negócio e um requisito de qualidade. As regras que ainda não foram definidas pelo cliente devem ser marcadas como propostas, até que sejam revisadas.

Como não existe um sistema implementado nesta atividade, a verificação será feita no papel, simulando o que aconteceria com uma entrada válida, uma inválida e outra que esteja exatamente no limite definido para a funcionalidade escolhida.

## Requisitos

| ID   | Descrição verificável                                                   | Necessidade atendida                  | Prioridade e justificativa                          | Regra vinculada |
|------|-------------------------------------------------------------------------|---------------------------------------|-----------------------------------------------------|-----------------|
| RF01 | Permitir o cadastro de equipamentos com código, descrição e quantidade. | Organizar os equipamentos disponíveis | Alta, pois é necessário registrar os equipamentos   | RN01            |
|      |                                                                         |                                       | para controlar os empréstimos.                      |                 |
| RF02 | Permitir consultar se um equipamento está disponível para empréstimo.   | Evitar dúvidas sobre a                | Alta, pois essa consulta é uma das principais       | RN01            |
|      |                                                                         | disponibilidade dos equipamentos.     | necessidades do sistema.                            |                 |
| RF03 | Permitir registrar a retirada e a devolução de equipamentos.            | Acompanhar os empréstimos e saber     | Alta, pois é a principal finalidade do sistema.     | RN02            |
|      |                                                                         | quais equipamentos foram devolvidos.  |                                                     |                 |
| RQ01 | Ao consultar um equipamento, o sistema deverá apresentar o resultado    | Tornar a consulta rápida para o       | Média, pois o cliente pediu rapidez,                | A confirmar     |
|      | em até 2 segundos, em condições de teste previamente definidas.         | usuário.                              | mas o limite ainda precisa ser validado.            |                 |



## Regras do domínio

| ID   | Regra proposta                                                                     | Confirmada ou a confirmar?                   |
|------|------------------------------------------------------------------------------------|----------------------------------------------|
| RN01 | Um equipamento só poderá ser emprestado se houver unidades disponíveis.            | Proposta, aguardando confirmação do cliente. |
| RN02 | A devolução deverá ser registrada para atualizar a disponibilidade do equipamento. | Proposta, aguardando confirmação do cliente. |

## Critérios e simulações da funcionalidade prioritária

A funcionalidade escolhida será o registro de empréstimos. Os exemplos abaixo mostram como ela deveria se comportar em diferentes situações.

| ID   | RF/RQ  | Condição inicial                    | Ação                                  | Resultado esperado                                                                   | Tipo      |
|      |        |                                     |                                       |                                                                                      | de caso   |
|------|--------|-------------------------------------|---------------------------------------|--------------------------------------------------------------------------------------|-----------|
| CA01 |  RF03  | Há 3 unidades disponíveis.          | Registrar o empréstimo de 1 unidade.  | O empréstimo é registrado e a quantidade disponível passa a ser 2.                   | Válido    |
| CA02 |  RF03  | Não há unidades disponíveis.        | Tentar registrar um novo empréstimo.  | O empréstimo não é realizado e uma mensagem informa que não há unidades disponíveis. | Inválido  |
| CA03 |  RF03  | Há exatamente 1 unidade disponível. | Registrar o empréstimo dessa unidade. | O empréstimo é registrado e a disponibilidade passa a ser 0.                         | Fronteira |

**Resultado observado na simulação em papel:** 
os três cenários apresentam resultados diferentes conforme a quantidade disponível.

**Ambiguidades descobertas:**
ainda é necessário confirmar se o sistema controlará a quantidade de unidades ou cada equipamento individualmente, além de definir as regras para registrar empréstimos e devoluções.


**Decisão de correção:**
manter as regras como propostas até que o cliente confirme como o controle deverá funcionar.


## Esboço de duas telas
- **Tela 1 — Equipamentos:** apresentar os campos Código, Descrição e Quantidade, além dos botões Cadastrar e Consultar. Após o cadastro, exibir uma mensagem de confirmação; se algum campo obrigatório estiver vazio, informar o que precisa ser corrigido.
- **Tela 2 — Empréstimos e devoluções:** apresentar o código do equipamento, a quantidade e a ação desejada (retirar ou devolver). Exibir uma mensagem confirmando a operação ou explicando por que ela não pôde ser realizada. Após concluir, permitir voltar à tela de equipamentos.


## Dados e finalidade

| Campo       | Para qual tarefa?                             | Exemplo    | Necessário ou dúvida?     |
|             |                                               | sintético  |                           |
|-------------|-----------------------------------------------|------------|---------------------------|
| Código      | Identificar o equipamento.                    | EQ01       | Necessário                |
| Descrição   | Saber qual equipamento está sendo consultado. | Notebook   | Necessário                |
| Quantidade  | Controlar quantas unidades estão disponíveis. | 3          | Necessário                |
| Ação        | Informar se o equipamento será retirado       | Retirada   | Necessário                |
|             | ou devolvido.                                 |            |                           |
| Responsável | Identificar quem realizou o empréstimo.       | Operador01 | A confirmar com o cliente |


## Critério de conclusão
A atividade estará concluída quando outra dupla conseguir repetir as três simulações, entender os resultados esperados e identificar quais requisitos e regras estão relacionados a cada caso.
