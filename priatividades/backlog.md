# Organização do trabalho
O objetivo é dividir o projeto em pelo menos cinco tarefas menores, deixando claro o que precisa ser feito, quem ficará responsável e como será possível conferir se cada tarefa foi concluída.
Use o arquivo `backlog.md` para organizar as tarefas. Cada uma deve estar ligada a um requisito e ter prioridade, dependência, responsável, revisor e uma evidência de conclusão.

Durante a atividade, os integrantes devem trocar de papel na metade do tempo, para que todos tenham a oportunidade de participar da execução e da revisão.
Antes de começar a programar, vamos organizar os requisitos, os esboços das telas e as tarefas. A parte de arquitetura, dependências e código será trabalhada nas próximas aulas.


## Preparação do ambiente
Abra a pasta nova do projeto no VS Code, acessando **Arquivo → Abrir pasta**. Depois, abra o terminal integrado PowerShell e siga as orientações do arquivo `guia-ferramentas.md`.
Antes de iniciar um repositório Git, confira se a pasta já pertence a algum repositório. Execute os comandos abaixo no terminal, um por vez:

```powershell
Get-Location
Get-ChildItem -Force
git --version
git rev-parse --show-toplevel
```

Se a pasta for nova e não estiver dentro de outro repositório, você poderá inicializar o Git:

```powershell
git init
git status --short
git rev-parse --show-toplevel
git remote -v
```

**Atenção:** só execute `git init` depois de confirmar que está na pasta correta. Esse comando cria um repositório local, mas não cria um commit nem envia arquivos para a internet. Nesta aula, não faça `push` nem altere configurações globais.

Não instale pacotes com `pip` nesta etapa. O primeiro commit revisado está previsto para a atividade A04.

## Backlog e quadro

As tarefas serão organizadas em quatro estados: **A fazer**, **Em andamento**, **Em revisão** e **Concluído**.

A prioridade indica o que precisa ser feito primeiro, considerando a importância e a urgência. A dependência mostra se uma tarefa precisa esperar outra ser concluída.

| ID  | Ação pequena                        | Requisito | Prioridade | Depende de | Responsável       | Revisor       | Estado  | Evidência de conclusão             |
|-----|-------------------------------------|-----------|------------|------------|-------------------|---------------|---------|------------------------------------|
| T01 | Organizar os requisitos do projeto. | RF01–RF03 | Alta       | Nenhuma    | Analista          | Revisor       | A fazer | Arquivo `requisitos.md` revisado.  |
|     |                                     |           |            |            |                   | de requisitos |         |                                    |
| T02 | Desenhar as duas telas em texto.    | RF01–RF03 | Alta       | T01        | Designer de       | Analista      | A fazer | Esboços salvos e revisados.        |
|     |                                     |           |            |            | interface         |               |         |                                    |
| T03 | Definir os campos dos equipamentos. | RF01      | Alta       | T01        | Analista          | Revisor de    | A fazer | Campos e finalidades registrados.  |
|     |                                     |           |            |            |                   | requisitos    |         |                                    |
| T04 | Planejar as consultas de            | RF02      | Alta       | T03        | Responsável       | Analista      | A fazer | Cenários de consulta               |
|     | disponibilidade.                    |           |            |            | pelo planejamento |               |         | documentados.                      |
| T05 | Revisar as tarefas e                | RF01–RF03 | Média      | T01, T02,  | Revisor da equipe | Outro         | A fazer | `backlog.md` revisado e pendências |
|     | preparar os documentos.             |           |            | T03 e T04  |                   | integrante    |         | registradas.                       |

 |

## Plano de versionamento

- **Pasta de trabalho e raiz Git:** 
registrar o caminho da pasta do projeto, sem expor dados pessoais.


- **Ferramenta e versão:** 
anotar a versão do Git exibida pelo terminal.


- **Arquivos para revisão antes do primeiro commit em A04:** 
`briefing.md`, `requisitos.md`, `backlog.md` e os demais documentos produzidos na atividade.


- **Arquivos que não devem entrar no histórico:** 
senhas, tokens, dados pessoais reais e arquivos locais desnecessários.


- **Como conferir o estado e as alterações:** 
usar `git status --short` e `git diff`.


- **Responsável pela revisão:** 
um integrante diferente do autor deve conferir os arquivos e registrar o resultado da revisão.


- **Pendências de instalação ou permissão:** 
registrar qualquer problema encontrado, sem tentar instalar ferramentas fora do combinado.


- **Cópia de segurança:** 
seguir o procedimento autorizado pela instituição. O Git local ajuda a acompanhar alterações, mas não substitui uma cópia de segurança.


## Critério de conclusão
A atividade estará concluída quando houver pelo menos cinco tarefas pequenas, ligadas aos requisitos, com prioridades, dependências, responsáveis, revisores e evidências de conclusão.
Também é necessário confirmar a situação do Git ou registrar claramente qualquer pendência.

**Dica:** 
em vez de escrever algo amplo, como “fazer o sistema”, descreva uma tarefa pequena que outra pessoa consiga verificar quando estiver pronta.