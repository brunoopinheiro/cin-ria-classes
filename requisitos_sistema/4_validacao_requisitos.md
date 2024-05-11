# Aula 4 - Validação de Requisitos
## O que é validação de requisitos?
> Consiste na verificação do documento de requisitos em relação á consistência, completude e acurácia.

- Será que realmente entendi o que o cliente deseja?
    - Devo me certificar de que não houve falha em nossa interação (comunicação).

- Exemplos de problemas:
    - Não conformidade com normas de qualidade.
    - Requisitos mal descritos, ambíguos.
    - Erros no entendimento do sistema ou problema a ser solucionado.
    - Conflitos entre requisitos que não foram detectados no processo de análise.
    - Realizar suposições ruins.
    - Escrever implementação (COMO) ao invés de requisitos (O QUE).
    - Descrever operações ao invés de escrever requisitos.
    - Usar termos incorretos.
    - Usar estrutura de frase incorreta ou gramática ruim.
    - Requisitos ausentes.
    - Especificação Excessiva.

### Palavras com potenciais problemas em uma especificação
| Attribute | What to consider |
|---|---|
|_Always, Every, All, None, Never_ | If you see words such as these that denote something as certain and absolute, make sure that they are indeed, certain. Think of cases that violate them when reviewing the spec.|
| _Certainly, Therefore, Clearly, Obviously, Ordinary, Customarily, Most, Mostly_ | These words then to persuade you into accepting something as given. Dont fall into the trap. |
| _Some, Sometimes, Often, Usually, Ordinarily, Customarily, Most, Mostly_ | These words are too vague. It's impossible to test a feature that operates "sometimes". |
| _Etc, And so forth, And so on, Such as_ | Lists that finish with that words aren't testable. There needs to be no confusion as to how the series is generated and what appears next on the list. |
| _Good, Fast, Cheap, Efficient, Small, Stable_ | These are unquantifiable terms. They aren't testable. If they appear in a specification, they must be further defined to explain exactly what they mean. |
| _Handled, Proccessed, Rejected, Skipped, Eliminated_ | These terms can hide large amounts of functionality and need to be specified. |
| _If... Then (but missing Else)_ | Look for statements that have "If... Then" clauses but don't have a matching "Else". Ask yourself what will happen if the "If" doesn't happen. | 

### Atributos de Requisitos
- `Não-Ambíguo` - cada requisito deve ter apenas uma interpretação;
- `Compreensível` - A interpretação de cada requisito deve ser nítida;
- `Correto` - O requisito deve indicar algo exigido do sistema definido pelos _stakeholders_;
- `Conciso` - Não deve ser incluída nenhuma informação desnecessária;
- `Rastreável` - Cada requisito derivado deve ser rastreável a um requisito de nível mais alto através de algum nome exclusivou ou número;
- `Independente de Design` - O requisito não deve especificar uma determinada solução;
- `Verificável` - Um processo finito e custo-efetivo deve ser definido para verificar que o requisito foi satisfeito;
- `Único` - os requisitos não devem ser redundantes a outros requisitos;
- `Completo`
    - (a) deve ser incluído tudo o que o sistema é obrigado a fazer ao longo do seu ciclo de vida;
    - (b) devem ser definidas respostas a todas as entradas possíveis ao longo do ciclo de vida do sistema;
    - (c) o documento deve ser definido de forma clara e autocontido;
- `Consistente`
    - (a) **interno** - Não devem existir dois subconjuntos de requisitos em conflito;
    - (b) **externo** - Nenhum subconjunto de requisitos deve entrar em confito com documentos a partir dos quais os requisitos são definidos;
- `Necessário` - Deve ser incluída a real necessidade do requisito.
- `Viável` - As soluções satisfazem restrições de desempenho, custo e cronograma.
- `Organizado` - Devem ser agrupados de acordo com um conjunto hierárquico de conceitos.

## Técnicas de Validação
<div style="display: flex; gap: 5px;">
    <div style="border: 2px solid yellow; width: 120px; text-align: center;">
        <span>Reuniões de Revisão</span>
    </div>
    <div style="border: 2px solid yellow; width: 120px; text-align: center;">
        <span>Checklists</span>
    </div>
    <div style="border: 2px solid yellow; width: 120px; text-align: center;">
        <span>Prototipação</span>
    </div>
    <div style="border: 2px solid yellow; width: 120px; text-align: center;">
        <span>Desenvolvimento do manual do Usuário</span>
    </div>
    <div style="border: 2px solid yellow; width: 120px; text-align: center;">
        <span>Validação de Modelos</span>
    </div>
</div>

## 1- Reuniões de Revisão de Requisitos
> Reunião formal no qual um grupo de pessoas lê e analisa os requisitos, procuram problemas, marcam uma reunião para discutir esses problemas e definem um conjunto de ações para resolver os problemas identificados.

### Processo de Revisão de Requisitos:
`Planejar a Revisão` => `Distribuir Documentos` => `Preparar-se para a revisão` => `Realizar Reunião de Revisão` => `Definir Ações de Acompanhamento` => `Revisar Documento`

### Antes da Reunião
- Realizar atitudes para evitar desperdício de tempo e trabalho dos revisores:
    - Remover erros que podem ser detectados sem uma revisão completa do documento: erros de ortografia, digitação, formatação, templates errados, espaçamento, numeração de seções, tamanho de fontes, legenda de figuras e tabelas, etc.
- Uma pessoa, que não participou da escrita do documento, deve ficar responsável por essa verificação antes de distribuir o documento para os demais membros do grupo.
- Essa atividade, geralmente, não gasta mais que um dia para ser concluída.

### Condução da Reunião
- Reunião formal que deve ser conduzida por alguém que não esteja envolvido na elaboração do documento de requisitos a ser validado.
- Durante a reunião:
    - O analista de requisitos apresenta cada requisito para comentários do grupo.
    - Os problemas identificados são discutidos.
    - Ações de acompanhamento/correção são definidas.
- Um membro do grupo deve ser responsável por fazer as anotações.

### Duração das Revisões de Requisitos
- Depende do tamanho do documento de requisitos.
- Estimativas de especialistas:
    - Uma média de 20-40 requisitos por hora podem ser inspecionados.
        - Mesmo tempo é estimado para a preparação.
    - Um documento de 400 requisitos requer um total de:
        - 50 horas de esforço considerando uma equipe de 4 pessoas.

## 2- Checklists de Revisão
- Devem ser genéricas e serem entendidas por não especialistas no domínio.
- Não devem ser muito longas.
    - Se possuem muitos itens, os analistas podem não relembrar todos os itens.
- Não devem incidir sobre requisitos individualmente.
    - mas com as propriedades de qualidade do documento como um todo e com as relações entre requisitos.

### Checklist de atributos de qualidade de requisitos
| **Attribute** | **What to Consider** |
|---|---|
|**Complete**| Is anything missing or forgotten? Is it thorough? Does it include everything necessary to make it stand alone? |
|**Accurate**| Does it properly define the goal? Are there any errors? Is it factual and true? |
|**Precise, Unanmbiguous and Clear**| Is the description exact and not vague? Is there a single interpretation? Is it easy to read and understand? |
|**Consistent**| Is the description of the feature written so that it doesn't conflict with itself or other items in the specification? |
|**Relevant**| Is the statement necessary to specify the feature? Is there extra information that should be left out? Is the feature traceble to an original customer need? |
|**Feasible**| Can the feature be implemented with the available personnel, tools, and resources within the specified budget and schedule? |
|**Code-free**| Does the specification stick with defining product and not the underlying software design, architecture, and code? |
|**Testable**| Can the feature be tested? Is enough information provided that a tester could create tests to verify its operation? |

## Gerenciamento de Requisitos
### Mudanças de Requisitos são Inevitáveis
<div style="display: flex; gap: 4px; flex-wrap: wrap">
    <div style="background-color: #323aa8; font-color: white; width: 120px; text-align: center; padding: 4px">
        <span>Erros em requisitos, conflitos e inconsistências</span>
    </div>
    <div style="background-color: #323aa8; font-color: white; width: 120px; text-align: center; padding: 4px">
        <span>Evolução do conhecimento sobre as necessidades dos usuários finais</span>
    </div>
    <div style="background-color: #323aa8; font-color: white; width: 120px; text-align: center; padding: 4px">
        <span>Problemas técnicos, Cronograma e de Custos</span>
    </div>
    <div style="background-color: #323aa8; font-color: white; width: 120px; text-align: center; padding: 4px">
        <span>Mudanças nas prioridades dos clientes</span>
    </div>
    <div style="background-color: #323aa8; font-color: white; width: 120px; text-align: center; padding: 4px">
        <span>Mudanças Ambientais</span>
    </div>
    <div style="background-color: #323aa8; font-color: white; width: 120px; text-align: center; padding: 4px">
        <span>Mudanças Organizacionais</span>
    </div>
    <div style="background-color: #323aa8; font-color: white; width: 120px; text-align: center; padding: 4px">
        <span>O desempenho ou a confiabilidade do sistema pode demandar melhorias</span>
    </div>
    <div style="background-color: #323aa8; font-color: white; width: 120px; text-align: center; padding: 4px">
        <span>Computadores e equipamentos novos são adicionados ao sistema</span>
    </div>
    <div style="background-color: #323aa8; font-color: white; width: 120px; text-align: center; padding: 4px">
        <span>Nossos requisitos emergem quando o software é usado</span>
    </div>
</div>

### Baseline
- Uma "fotografia" de uma versão de cada artefato no repositório do projeto de desenvolvimento de software.
- Normalmente gerada ao final de uma fase do desenvolvimento.
- Representa marcos de versionamento de artefatos:
    - Final de Especificação de Requisitos.
    - Modelos documentados e revisados.
    - Final da Implementação de um módulo.
    - Erros encontrados e corrigidos.
    - Implantação de uma versão do sistema.
- Ex.: versão 1.0.0

> **Baseline de Requisitos:** um conjunto de requisitos revisados e aprovados alocados para uma versão do software.
É uma configuração formalmente aprovada para servir de referência para o desenvolvimento posterior do sistema.

> _"Uma especificação ou produto que foi formalmente revisto e aprovado, o qual daí em diante serve como base para o desenvolvimento futuro e que pode ser modificado apenas por meio de procedimentos formais de controle da modificação."_ (IEEE Std no. 610.12-1990)

### Gerenciamento de Mudança
- Está relacionado com os procedimentos, processos e padrões que serão usados para gerenciar as mudanças nos requisitos do sistema.
- Ex.: Tabelas, Jira, Confluence, Formulários.

### Gerenciamento de Requisitos
- É o processo de compreender e controlar as mudanças nos requisitos do sistema.
- As principais atividades são:
    - Gerenciar mudanças nos requisitos que foram acordados.
    - Gerenciar o relacionamento entre os requisitos.
    - Gerenciar as dependências entre os requisitos e outros artefatos produzidos no processo de engenharia do sistema.

### Rastreamento de Requisitos
- Requisitos não podem ser gerenciados efetivamente sem o rastreamento de requisitos.

| Rastreamento **das fontes dos requisitos** | Rastreamento **da razão dos requisitos** | Rastreamento **requisitos-requisitos** |
| --- | --- | --- |
| Relaciona o requisito, pessoas e documentos que especificaram os requisitos. | Relaciona o requisito com a descrição do porque o requisito foi especificado. | <ul><li>Relaciona requisitos com outros requisitos que são, de alguma forma, dependentes deles.</li><li>Deve ser um relacionamento em duas direções (dependentes "dependente-de")</li></ul> |

| Rastreamento **requisitos-arquitetura** | Rastreamento **requisitos-projeto** | Rastreamento **requisitos-interface** |
| --- | --- | --- |
| <ul><li>Relaciona os requisitos com os susbsistemas (componentes da arquitetura) onde estes requisitos estão implementados.</li><li>Isto é particularmente importante quando os subsistemas estão sendo desenvolvidos por diferentes subcontratados (empresas terceirizadas).</li></ul> | Relaciona os requisitos com hardware especifico ou com elementos de projeto de software que são usados para implementar os requisitos. | Relaciona os requisitos com a interface externa do sistema que será usada para acessar as funcionalidades descritas nos requisitos. |

### Rastreabilidade e Standards
DO 178-C - Section 11.21 Trace Data

- Trace Data estabilishes the associations between life cycle data items contents. Trace Data should be provided that demonstrates bi-directional associations between:
    - a. System requirements allocated to software and high-level requirements.
    - b. High-level requirements and low-level requirements.
    - c. Low-level requirements and Source Code.
    - d. Software Requirements and test cases.
    - e. Test cases and test procedures.
    - f. Test procedures and test results.
    
### Rastreamento Backwards/Fowards
Rastreamento de informação é aquela informação que ajuda a analisar o impacto de uma mudança de requisito. Ela relaciona requisitos entre si e outras representações do sistema.

| Rastreamento Backwards-From | Rastreamento Foward-from | Rastreamento Backwards-to | Rastreamento Forward-to |
| --- | --- | --- | --- |
| Relaciona requisitos a suas fontes em outros documentos ou a pessoas. | Relaciona requisitos ao projeto e componentes de implementação | Relaciona o projeto e componentes de implementação aos requisitos. | Relaciona outros documentos (que podem ter precedido o documento de requisito) aos requisitos relevantes |

### Identificação de Requisitos
- É essencial para o gerenciamento de requisitos que cada requisito tenha uma identificação única.
- Técnicas de identificação de requisitos
    - **Identificação estática**: Os requisitos podem ser identificados através de um nome simbólico que está associado ao próprio requisito. Por exemplo, RF01, HLR, LLR, etc.
    - **Referência Cruzada**: ao reorganizar seu documento e adicionar novos requisitos, o sistema mantém controle de referência cruzada e automaticamente referencia seus requisitos dependendo do capítulo, seção e posição dentro da seção.
    - **Identificação do Registro no Banco de Dados**: quando um requisito é identificado ele é registrado em um banco de dados, sendo atribuido um identificador de registro no banco de dados. Este identificador do banco de dados é usado em todas as referências subsequentes do requisito.

### Tabelas de Rastreamento X Listas de Rastreamento
- Tabelas de Rastreamento:
    - Mostram o relacionamento entre os requisitos ou entre requisitos e componentes do projeto.
        - Os requisitos são listados ao longo dos eixos horizontais e verticais e os relacionamentos são marcados nas células da tabela.
    - As tabelas de rastreamento que mostram as dependências devem ser definidas com o número dos requisitos que são usados para rotular as linhas e colunas da tabela.

| | R1 | R2 | R3 | R4 | R5 | R6 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **R1** |  |  | X | X |  |  |
| **R2** |  |  |  |  | X | X |
| **R3** |  |  |  | X | X |  |
| **R4** |  | X |  |  |  |  |
| **R5** |  |  |  |  |  | X |
| **R6** |  |  |  |  |  |  |

- Listas de Rastreamento
    - Se o número de requisitos a ser gerenciado for pequeno (até 250), as tabelas de requisito podem ser implementadas usando uma planilha.
    - Se o número de requisitos a ser gerenciado for grande (centenas ou milhares) as tabelas de requisitos serão problemáticas e as tabelas ficarão esparsamente populadas.
    - Poderá ser usada de forma simplificada de rastreamento onde ao lado da descrição dos requisitos, são mantidas uma ou mais listas de identificadores dos requisitos relacionados.
    - Listas de rastreamento são simples listas de relacionamentos que podem ser implementadas como texto ou tabelas simples.

| Requisito | Depende de |
|:---:|:---:|
| **R1** | R3, R4 |
| **R2** | R5, R6 |
| **R3** | R4, R5 |
| **R4** | R2 |
| **R5** | R6 |

## Práticas do Gerenciamento de Requisitos
<div style="display: flex; gap: 4px; flex-wrap: wrap">
    <div style="background-color: #323aa8; font-color: white; width: 120px; text-align: center; padding: 4px">
        <span>Criar uma baseline de Requisitos</span>
    </div>
    <div style="background-color: #323aa8; font-color: white; width: 120px; text-align: center; padding: 4px">
        <span>Gerenciar versões do documento de requisitos</span>
    </div>
    <div style="background-color: #323aa8; font-color: white; width: 120px; text-align: center; padding: 4px">
        <span>Seguir um processo de controle de mudança</span>
    </div>
    <div style="background-color: #323aa8; font-color: white; width: 120px; text-align: center; padding: 4px">
        <span>Realizar análise de impacto</span>
    </div>
    <div style="background-color: #323aa8; font-color: white; width: 120px; text-align: center; padding: 4px">
        <span>Rastrear o status de cada requisito</span>
    </div>
    <div style="background-color: #323aa8; font-color: white; width: 120px; text-align: center; padding: 4px">
        <span>Rastrear requisitos em arquitetura, código e teste</span>
    </div>
    <div style="background-color: #323aa8; font-color: white; width: 120px; text-align: center; padding: 4px">
        <span>Armanezar requisitos em uma ferramenta de requisitos</span>
    </div>
</div>
