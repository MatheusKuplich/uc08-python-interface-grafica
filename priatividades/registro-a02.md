# A02 — estados e transições do cadastro

**Código do estudante:** [seu código]  
**Arquivo e interpretador executados:** `estado_cadastro.py` e `cadastro_completo.py` — Python 3

## Retomada sem consulta

**1. O que get devolve? Por que int pode falhar?**

Minha resposta inicial: `get()` pega o texto digitado no campo. `int()` transforma o texto em número inteiro, mas pode dar erro se o valor estiver vazio ou tiver letras ou decimais, como `2.5`.

**2. O que muda entre passar uma função e chamá-la ao ligar um botão?**

Minha resposta inicial: Passar a função, como `command=registrar`, faz com que ela seja executada quando o botão for clicado. Já `command=registrar()` chama a função imediatamente, durante a criação do botão.

**3. Que caso detecta um nome preenchido somente com espaços?**

Minha resposta inicial: Usar `nome.strip() == ""`, porque `strip()` remove os espaços do começo e do fim do texto.

## Preveja e depois execute (nomes sempre fictícios)

| Caso | Estado/ação | Previsão | Observação | Ajuste |
|---|---|---|---|---|
| T01 | Abrir e Exibir antes de Registrar | Deve informar que não existe cadastro confirmado. | A confirmar no teste. | Nenhum, se funcionar como esperado. |
| T02 | Registrar Lia / Costa / 18 e Exibir | Deve mostrar Lia Costa, com idade 18. | A confirmar no teste. | Nenhum, se funcionar como esperado. |
| T03 | Editar para Rui / Lima / 22; somente Exibir | Deve continuar mostrando Lia Costa, pois Rui ainda não foi registrado. | A confirmar no teste. | Não alterar o registro confirmado ao editar os campos. |
| T04 | Limpar campos e depois Exibir | Os campos devem ficar vazios, mas o cadastro de Lia deve continuar salvo na memória. | A confirmar no teste. | Separar a limpeza dos campos da limpeza do registro. |
| T05 | Após um válido, tentar registrar outro nome com idade abc | Deve recusar a idade inválida e manter o cadastro anterior. | A confirmar no teste. | Validar os dados antes de atualizar o registro. |
| T06 | Registrar Rui / Lima / 22; depois Exibir | Deve mostrar Rui Lima, pois o novo cadastro é válido. | A confirmar no teste. | Nenhum, se funcionar como esperado. |
| T07 | Nome vazio ou somente espaços | Deve recusar o cadastro. | A confirmar no teste. | Verificar se o nome está vazio após `strip()`. |
| T08 | Sobrenome vazio ou somente espaços | Deve recusar o cadastro. | A confirmar no teste. | Aplicar a mesma validação ao sobrenome. |
| T09 | Idade vazia, 0, -2 e 2.5 (um teste por entrada) | Deve recusar todas essas entradas. | A confirmar no teste. | Validar a conversão, exigir idade maior que zero e aceitar somente números inteiros. |
| T10 | Espaços nas pontas e nome composto | Deve remover espaços extras nas pontas e manter os espaços entre as palavras. | A confirmar no teste. | Aplicar `strip()` antes de confirmar os dados. |
| T11 | Fechar, reabrir e Exibir | Deve começar sem cadastro, pois os dados não são salvos em arquivo ou banco de dados. | A confirmar no teste. | Usar armazenamento permanente se isso for necessário no projeto. |

## Uso da interface

**Percorri campos e botões com Tab/Shift+Tab:** [preencher após testar]

**Mensagem que precisei melhorar:** [escrever a mensagem, se alguma ficou confusa; caso contrário, informar que nenhuma precisou de ajuste]

**Colega que testou (código fictício ou combinado):** [preencher após o teste]

## Fechamento sem consulta

**Por que Limpar campos não deve apagar o registro confirmado?**

Porque os campos servem para digitar ou editar informações, enquanto o registro confirmado guarda o último cadastro válido. Limpar os campos não deve apagar os dados que já foram confirmados.

**Como uma tentativa inválida pode estragar um cadastro anterior se a ordem do código estiver errada?**

Se o programa atualizar o registro antes de validar todos os dados, uma tentativa inválida pode substituir um cadastro correto por informações erradas ou incompletas. Por isso, é importante validar primeiro e confirmar somente depois.

**Minha dificuldade, ajuste e próximo passo:**

Minha dificuldade foi entender a diferença entre os dados digitados e o cadastro confirmado. O ajuste é verificar os dados antes de salvar o registro. Meu próximo passo é praticar mais testes com entradas válidas e inválidas e conferir se o cadastro anterior continua correto.

**Entregas externas:** `estado_cadastro.py`, `cadastro_completo.py` e este registro em Markdown.



Caso	Previsão	Observação	Ajuste
T01	O programa deve avisar que ainda não há nenhum cadastro.	Ainda preciso testar para ver se isso acontece.	Se funcionar como esperado, não precisa mudar nada.
T02	Deve aparecer o cadastro de Lia Costa, com 18 anos.	Ainda preciso conferir se os dados aparecem corretamente.	Se estiver tudo certo, não precisa de ajustes.
T03	Deve continuar aparecendo Lia Costa, porque os dados de Rui ainda não foram registrados.	Vou conferir se editar os campos muda ou não o cadastro salvo.	Garantir que mudar os campos não altere o último cadastro confirmado.
T04	Os campos devem ficar vazios, mas o cadastro de Lia deve continuar salvo.	Vou verificar se limpar os campos mantém o cadastro anterior.	Fazer com que limpar os campos não apague o cadastro salvo.
T05	O programa deve recusar a idade abc e manter o cadastro anterior.	Vou conferir se os dados anteriores continuam os mesmos depois da tentativa inválida.	Só atualizar o cadastro depois de validar todos os dados.
T06	Deve aparecer o cadastro de Rui Lima, com 22 anos.	Vou conferir se o novo cadastro substituiu o anterior corretamente.	Se funcionar como esperado, não precisa mudar nada.
T07	O programa deve impedir o cadastro se o nome estiver vazio ou tiver apenas espaços.	Vou testar as duas situações para ver se o programa as identifica.	Verificar se o nome continua vazio depois de remover os espaços extras com strip().
T08	O programa deve impedir o cadastro se o sobrenome estiver vazio ou tiver apenas espaços.	Vou testar se a validação funciona nos dois casos.	Aplicar ao sobrenome a mesma verificação feita no nome.
T09	O programa deve recusar o campo vazio, o zero, o número negativo e o decimal 2.5.	Vou testar cada valor separadamente para conferir se todos são rejeitados.	Verificar se a idade é um número inteiro maior que zero.
T10	O programa deve retirar os espaços extras do começo e do fim, sem juntar as palavras do nome composto.	Vou conferir se os nomes ficam corretos depois do registro.	Usar strip() para remover os espaços das pontas antes de salvar os dados.
T11	Ao abrir o programa novamente, não deve aparecer o cadastro anterior, pois os dados só ficam guardados na memória durante a execução.	Vou conferir se o cadastro realmente desaparece depois de fechar o programa.	Se for necessário manter os dados após fechar o programa, será preciso salvá-los em um arquivo ou banco de dados.


Por que Limpar campos não deve apagar o registro confirmado?

Porque limpar os campos serve apenas para apagar o que foi digitado. O cadastro confirmado deve continuar guardado, já que representa os últimos dados válidos registrados.

Como uma tentativa inválida pode estragar um cadastro anterior se a ordem do código estiver errada?

Isso pode acontecer se o programa salvar os novos dados antes de verificar se estão corretos. Assim, uma tentativa inválida pode acabar apagando ou substituindo um cadastro válido. Por isso, o certo é validar tudo primeiro e só depois atualizar o registro.

Minha dificuldade, ajuste e próximo passo:

Minha dificuldade foi entender a diferença entre os dados que estão sendo digitados e aqueles que já foram confirmados. O ajuste é conferir todos os dados antes de salvar o cadastro. Meu próximo passo é testar outras situações, incluindo dados inválidos, para verificar se o registro anterior continua correto.