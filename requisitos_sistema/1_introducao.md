# Aula 1 - Requisitos
## Introdução
> Requisitos do sistema busca diminuir as divergências de entendimento entre as necessidades reais do projeto, as exigências do cliente, e a implementação real e manutenção do código.

<img src="https://jkolb.com.br/wp-content/uploads/2013/09/project_sw.jpg" width="800px" />

## Atividades do Processo de Software
Existem vários processos de desenvolvimento mas todos envolvem:
- **Especificação** - definição do que o sistema deve fazer;
- **Projeto e Implementação** - definição da organização do sistema e implementação do sistema;
- **Validação** - avaliação de que o sistema faz o que o cliente deseja;
- **Evolução** - evolução em resposta a mudanças nas necessidades do cliente.
## Modelos de Processo de Software
- Metodologias Tradicionais (modelo cascata)
- Metodologias Evolucionárias (incremental, prototipação, espiral)
- Metodologias Ágeis (XP, SCRUM, Crystal)
- Metodologias Emergentes (baseadas em reuso, em componentes)

## Engenharia de Software (ES)
É uma disciplina da engenharia que se preocupa com todos os aspectos da produção de software.
- Desde o ínicio da especificação do sistema até a manutenção do sistema após esse estar sendo usado.
- Disciplina da engenharia.
    - Utiliza teorias e métodos adequados para resolver os problemas tendo em mente as restrições organizacionais e financeiras.
- Todos os aspectos da produção de software.

## Elementos da ES
- Processo
    - Define os passos gerais para o desenvolvimento e manutenção do software.
    - Serve como uma estrutura de encadeamento de métodos e ferramentas.
- Métodos
    - São os _"how to's"_ de como fazer um passo específico do processo.
- Ferramentas
    - Automatizam o processo e os métodos.

## Engenharia de Requisitos
> _"The serious problems that have happened with software have to do with requirements, not coding errors."_ 
>
> **Nancy Leveson**

> **Documentário:** Downfall, the case against boieng. Netflix (2022)

- **33%** de erros acontecem em engenharia de requisitos.
- **36%** de erros em engenharia de requisitos ocasionam falha do projeto.

### Sintomas de ER mal aplicada
<img src="https://vilelasagna.ddns.net/wp-content/uploads/2019/08/gohorsenew.jpg" width="800px" />

### Importância da ER
- Gause, Donald and Gerald Weinberg. Exploring Requirements: Quality Before Design:
    - Encontrar e corrigir defeitos de requisitos após a entrega é muitas vezes 100 vezes mais caro do que encontrá-los e corrigi-los durante as fases de requisito e design (Boehm e Basili, 2001).

| Development Phase | Cost Ratio |
|:---:|:---:|
| Requirements | 1 |
| Design | 3 - 6x |
| Implementation | 10x |
| Development Testing | 15 - 40x |
| Acceptance Testing | 30 - 70x |
| Post Release | 40 - 1000x |

## Definição
> **Engenharia de Requisitos (ER)** é um conjunto de atividades relacionadas a `identificação e comunicação` do 
`propósito` de um sistema e os `contextos` nos quais será usado. Portanto, ER atua como uma ponte entre `as necessidades do mundo real` de usuários, clientes, e outros `envolvidos` afetados pelo software, e as `capacidades e oportunidades` proporcionadas por tecnologias.
- A comunicação é tão importante quanto a análise.
- Designers precisam saber como e onde o sistema será usado.
- Qualidade significa adequação à finalidade. Não posso dizer nada sobre qualidade à menos que você entenda o propósito.
- Requisitos são parcialmente sobre o que é necessário...
- ...e em parte sobre o que é possível.
- Precisa identificar todas as partes interessadas - não apenas o cliente e o usuário.

## Elicitação de Requisitos
- ELICITAR = Eliciar + Clarear + Extrair + Descobrir, tornar explícito, obter o máximo de informação para o conhecimento do objeto em questão.
- Pode envolver:
    - Usuários finais
    - Gerentes
    - Engenheiros
    - Especialistas de domínio
- Estes são chamados `stakeholders` (partes interessadas).

### Técnicas de Elicitação de Requisitos e Levantamento de Informações
- Questionários/Formulários
- Análise de documentos
- Prototipação
- Etnografia
- Reuso
- _Brainstorm_
- Grupos Focais
- Entrevistas
- **GERSE** (Guia de Elicitação de Requisitos para Sistemas Embarcados de Pequeno e Médio porte)