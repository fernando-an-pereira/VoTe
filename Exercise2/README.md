# Exercise 2

## The challenge

```
Dashboard​ ​de​ ​Tasks

Sua tarefa é implementar um dashboard de tasks com login autenticado pelo
Google onde cada task admite um ou mais arquivos em anexo como
"material de suporte" para execução.

O fluxo deve seguir a seguinte ordem:
● task​ é submetida utilizando o dashboard
● task​ vai para uma fila F
● consumer de F faz upload do anexo correspondente à task​ no S3
● status da task​ no dashboard é atualizado para "processada"
● quando desejado, usuário marca task​ como "done"​ ​pelo dashboard
● toda task​ marcada "done"​ é indexada no Elastic Search para buscas
futuras

As tasks​ devem suportar, pelo menos:
● quantidade indefinida de anexos
● nome da task
● prioridade da task​ (1 a 5)
● descrição da task
● usuário que submeteu a task
● usuário que marcou a task​ como "done"

O dashboard deve suportar, pelo menos, as seguintes operações:
● criação de task
● deleção de task
● edição de task
● leitura de task

Submissão:
● Link com acesso para código no repositório git ou equivalente
● Credenciais de leitura da AWS
● Arquivo no repositório explicando quais assumptions você fez para
desenvolver o sistema e quais foram as principais dificuldades e
desafios
```

## Assumptions

## 

## Main challenges
