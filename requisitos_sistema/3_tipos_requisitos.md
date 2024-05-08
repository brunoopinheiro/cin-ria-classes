# Aula 3 - Tipos de Requisitos
## Tipos de Requisitos
- Requisitos de Software
    - Requisito Funcional
    - Regra de Negócio
    - Requisito Não Funcional

**Requisitos Funcionais:** descrevem funcionalidades ou serviços do sistema.
- Indicam declarações de alto nível do queo sistema deve fazer, à nível dos usuários.
- Descrevem o comportamento de elementos em termos de entrada-saída.
- Exemplos:
    - _A cafeteira deverá ser capaz de produzir café do tipo expresso, longo e cappuccino._
    - _A cafeteira deverá possuir opções de ligar, desligar e pausar o programa atual manualmente_.
    - _A cafeteira deverá ter a possibilidade de obter controle por comando de voz (ligar, desligar, pausar e selecionar programa)._

### Sintaxe para Requisitos Funcionais
> <font color="yellow">ATOR</font> **shall** <font color="red">AÇÃO</font> <font color="green">CONDIÇÃO</font>

> <font color="green">CONDIÇÃO</font>, <font color="yellow">ATOR</font> shall <font color="red">AÇÃO</font>

- <font color="green">Condição</font>: pode ser o estado ou a entrada.
    - Se a condição não aparecer explícita, entende-se que a ação é realizada sempre.
    - Estado atual geralmente é colocado na condição.
- <font color="yellow">Ator</font> é o software, mas também pode ser um componente do software.
- **Shall** é palavra obrigatória.
- <font color="red">Ação</font> é o processamento das saídas ou novo estado em termos de entradas.
    - Estado futuro e saídas geralmente são colocadas na <font color="red">ação</font>.
    - Entradas podem estar tanto na condição como na <font color="red">ação</font>.

### Regra de Negócio
- **Regras de Negócio**: são políticas, condições ou restrições que devem ser consideradas na execução dos processos de uma organização.
    - Descrevem a maneira pela qual a organização funciona.
- Regras de negócio normalmente **influenciam o comportamento** de determinados casos de uso.
    - Quando isso ocorre, os identificadores das regras do negócio devem ser adicionados à descrição dos casos de uso em questão.
    - Uso da seção "Regras do Negócio" da descrição do caso de uso.
- Exemplos de Regras de Negócio:
    - _O valor total de um pedido é igual à soma dos totais dos itens do pedido acrescido de 10% de taxa de entrega._
    - _O número máximo de alunos por turma é 50._
    - _Um cliente de uma das agências do banco não pode retirar mais do que R$ 2.000 por dia de sua conta. Após as 18:00h, esse limite cai para R$ 500._
    - _Para alugar um carro, o proponente deve estar com a carteira de motorista em situação regular._

### Regras de Negócio X Requisitos Funcionais
![](https://img.freepik.com/fotos-premium/gua-de-coco-gelada-na-praia_538646-60.jpg)
- Regras de negócio inerentes ao negócio de "vender coco na praia".
    - O coco somente será entregue ao cliente que realizar o pagamento.
    - Somente serão aceitos pagamento em dinheiro vivo. Não serão aceitos cartões de crédito, débito ou cheque.
    - Clientes que comprarem 4 cocos ganharão um coco de graça. Esta promoção não terá data para término.
    - Quando a caixa de isopor (onde ficam os cocos) ficar sem gelo o vendedor deverá parar, abastecer a caixa com gelo e somente aí continuar a vender.
    - O vendedor deverá portar ferramenta que permita furar o buraco no coco para que o cliente possa bebê-lo. Esta ferramenta não pode ser cortante, nem serrilhada nas bordas.
    - O vendedor deverá portar canudinho e fornecê-lo ao cliente ao entregar-lhe o coco, para que o cliente possa bebê-lo. Sempre deverá oferecer o canudinho, mas deverá abri-lo após o cliente aceitar recebê-lo, pois se o cliente não quiser, uma vez não aberto o canudinho (não tirado o plástico), não haverá desperdício deste material.

Se o vendedor de coco contratar um profissional para implementar software para ajudá-lo nas vendas, **parte destas regras deverão ser atendidas no sistema. Mas não serão requisitos funcionais, serão regras de negócio**.

- No exemplo do vendedor de coco, teríamos requisitos funcionais como:
    - Processar venda de coco.
    - Aplicar promoções vigentes na realização da venda.
    - Calcular quantidade de gelo conforme o tamanho da caixa de isopor.
    - Calcular quantidade de canudinhos para a quantidade de cocos contidas na caixa de isopor.
    - Incluir desconto padrão na venda de cocos.

### Requisitos Não Funcionais
Declaram as características de qualidade que o sistema deve possuir e que estão relacionadas às suas funcionalidades.
- Muitas vezes são mais críticos que os requisitos funcionais.
- Exemplos:
    - _"O sistema deve ser rápido."_
    - _"O sistema deve ser fácil de usar."_
    - _"O tempo de resposta do sistema não deve ultrapassar 2 segundos."_
    - _"O software deve ser operacionalizado no sistema Android."_

- São críticos para o sucesso de sistemas de sofware.
    - Diretamente relacionados com a satisfação dos usuários.

> _"O sistema executa todas as funcionalidades desejadas, mas é muito difícil de usar e demora muito para executar operações simples."_

### Principais Características dos NFRs (Requisitos Não Funcionais)
- `Subjetivos`: são interpretados e avaliados por diferentes pessoas que têm diferentes perspectivas e necessidades, assim eles podem ter diferentes significados para cada pessoa.
- `Relativos`: sua interpretação e importância dependem diretamente de cada sistema e sua realização é relativa.
- `Interativos`: eles interagem entre si, assim a realização de um RNF pode interferir positivamente ou negativamente outros requisitos.

- A implementação desses requisitos pode ter impacto em todo o sistema.
    - Há duas razões para isso:
        1. Requisitos não funcionais **podem afetar a arquitetura geral de um sistema** ao invés de apenas componentes individuais.
            - Por exemplo, para assegurar que sejam cumpridos os requisitos de desempenho, será necessário organizar o sistema para minimizar a comunicação entre os componentes.
        2. Um único requisito não funcional, tal como um requisito de _safety_, **pode gerar uma série de requisitos funcionais** relacionados que definam os serviços necessários no novo sistema.
            - Além disso, também podem gerar requisitos que restrinjam requisitos existentes.

### Classificação dos requisitos não funcionais- IEEE Std-830 1998
Não existe uma definição formal ou classificação única de RNF.

| **Requisitos Específicos** |
|---|
|Requisitos de Performance |
|Requisitos de Interface |
|Requisitos Operacionais |
|Requisitos de Recursos |
|Requisitos de Verificação |
|Requisitos de Aceitação |
|Requisitos de Documentação |
|Requisitos de Segurança (_security_) |
|Requisitos de Portabilidade |
|Requisitos de Qualidade |
|Requisitos de Confiabilidade |
|Requisitos de Manutenbilidade |
|Requisitos de _Safety_ |

### Classificação de Sommerville
<img src="https://www.researchgate.net/profile/Iana-Chaves/publication/311459854/figure/fig1/AS:436679518494721@1481123918481/Figura-1-Tipos-de-Requisitos-Nao-Funcionais-Fonte-Sommerville-2011-Os-RNFs-que-vem.png" />

### Requisitos Não-Funcionais - Exemplos
- **Requisitos de Produto**
    - O sistema deve ser robusto e tolerante à falhas, de forma a continua sua operação ou abortar de forma segura o modo autônomo caso haja falha de um ou mais sistemas essênciais.
- **Requisitos Organizacionais**
    - O processo de desenvolvimento do sistema e os produtos liberáveis devem estar em conformidade com o padrão empresarial XYZ.
- **Requisitos Externos**
    - Os operadores do sistema não devem ter acesso a qualquer dado que não necessitem.

### Métricas para especificar requisitos não funcionais

| Propriedade | Medida |
| --- | --- |
| Velocidade | <ul><li>Transações processadas/segundo</li><li>Tempo de Resposta de usuário/evento</li><li>Tempo de Atualização de tela</li></ul> |
| Tamanho | <ul><li>Megabytes</li><li>Número de Chips de memória ROM</li></ul> |
| Facilidade de uso | <ul><li>Tempo de Treinamento</li><li>Número de _frames_ de ajuda</li></ul> |
| Confiabilidade | <ul><li>Tempo médio para falha</li><li>Probabilidade de indisponibilidade</li><li>Taxa de Ocorrência de Falhas</li><li>Disponibilidade</li></ul> |
| Robustez | <ul><li>Tempo de reinício após falha</li><li>Percentual de eventos que causam falhas</li><li>Probabilidade de corrupção de dados em caso de falha</li></ul> |
| Portabilidade | <ul><li>Percentual de declarações dependentes do sistema-alvo</li><li>Número de sistemas-alvo</li></ul> |

## Análise e Negociação de Requisitos
### Etapas do Processo de Engenharia de Requisitos
- `Gerenciamento`
    - Rastreabilidade
    - Consistência
- `Elicitação`
    - Levantamento
    - Técnicas de Identificação
    - Detalhamento
- `Análise e Negociação`
    - Resolução de Conflitos
    - Consistência das informações
- `Especificação`
    - Descrição
    - Linguagem Natural
    - Diagramas
- `Validação`
    - Resolução de Conflitos
    - Consistência das Informações

### Análise dos Requisitos
- **Análise**: "quebrar" um sistema em seus componentes e estudar como tais componentes interagem como objetivo de entender como esse sistema funciona.
- É realizado um **estudo** dos **requisitos** elicitados na fase anterior e são **construídos modelos** para **representar** o sistema a ser construído.
- **Objetivo**: estabelecer uma **estratégia** de **solução** sem se preocupar com a maneira ***como*** a estratégia será realizada.
    - Não há preocupação com a tecnologia utilizada.

### Problemas com Requisitos e Exemplo de Checklist
Erros mais comuns:
- Ignorar um grupo de clientes.
- Ignorar um único cliente.
- Omitir um grupo de requisitos.
- Permitir inconsistências entre grupos de requisitos.
- Aceitar requisito inadequado.
- Aceitar requisito incorreto, indefinido, ou impreciso.
- Aceitar um requisito ambíguo e inconsistente.

Checklist de avaliação:
- O requisito inclui aspectos de arquitetura ou implementação?
- O requisito poderia ser decomposto em subrequisitos?
- O requisito é mesmo necessário?
- O requisito está de acordo com os objetivos do negócio?
- O requisito é ambíguo?
- O requisito é realista?
- O requisito é "testável"?

### Níveis de Requisitos
- O processo de design aplica as ferramentas de uma disciplina (system/software) para encontrar uma solução para o problema.
- A solução de um nível se torna o problema a ser resolvido pelo nível seguinte (em cadeia).

- Caso os requisitos do sistema se desdobrem apenas em um item de software:
    - **SRATS** = Sys e Sw ao mesmo tempo. (System Requirements Allocated to Software)

### High Level e Low Level Requirements
- A diferença de níveis não é apenas o nível de detalhe, mas também o escopo dos requisitos.
    - Cada elemento do LLR possui seus próprios inputs e outputs.
- Low-level requirement ≠ detalhar o máximo possível.
    - _"requirements from which Source Code can be directly implemented without further information."_
- High-level requirement ≠ ambíguo, artificialmente abstrato
    - Não está detalhado o suficiente para implementar
- Caso um HLR se desdobre para apenas um componente e não seja necessário detalhar para que seja diretamente implementado:
    - `SLR = SwHLR & SwLLR` ao mesmo tempo (single-level requirement)
- Exemplo de desdobramento
- HLR: _The software shall display the received messages in alphabetical order._
- LLR: _The input_processing component shall receive the messages and store them in [buffer] in alphabetical order, using the bubble sort algorith_
- LLR: _The output_generator component shall send [buffer] to the display._

### Boas Práticas para escrever requisitos
- Escrito em inglês no contexto de _safety-critical_
- Em voz ativa
- Deve conter _"shall"_, não _"will"_, _"should"_, _"must"_
- Apenas uma necessidade
- Sentenças afirmativas
- Não ter palavras subjetivas (bom, melhor, rápido, preciso)
- Campos obrigatórios: `ator` e `ação`.

### Negociação de Requisitos
- Negociação para quê?
    - Chegar a um acordo em relação a opções mais adequadas aos interesses dos _stakeholders_.
- Definir as prioridades dos requisitos para novas iterações de identificação e análise para o desenvolvimento.
- Chegar a acordo em relação a compromissos entre requisitos que entram em conflito.

## Diagrama de Requisitos
O diagrama de requisitos representa graficamente:
- Hierarquia entre os requisitos.
- Relacionamentos entre os requisitos e outros elementos do modelo.

- Existem <font color="red">três tipos de notação</font> usados para descrever relacionamentos entre requsitos:
    - Direct, Compartment, e Callout
- Existem 7 tipos de relacionamentos entre requisitos:
    - _Containment_
    - _Satisfy_
    - _Verify_
    - _Derive_
    - _Refine_
    - _Trace_
    - _Copy_

### Representação de Relacionamentos
- **Direct**
    - Usado quando o requieito e o elemento do modelo relacionado `aparecem no mesmo diagrama`.
    - Estabelece a dependência do elemento do modelo com a exigência no modelo.
    
- **Compartment**
    - Usado quando o requisito e o elemento do outro modelo `não aparecem no mesmo diagrama`.
    - Utilizado para elementos de outros modelos, tais como blocos ou requisitos que suportam compartimentos.

- **Callout**
    - Usado quando o requisito e o elemento do outro modelo não aparecem no mesmo diagrama.
    - Utiliza a caixa "Anotação" ao in´ves de um elemento do modelo.
    - Pode ser usado quando o elemento do outro modelo ou ferramenta não suporta compartimentos.

### Tipos de Relacionamentos entre requisitos
- **Containment:**
    - Representa hierarquia entre os requisitos.
    - Também pode ser usado para representar quais requisitos estão contidos em um Pacote.

- **Satisfy**
    - Representa quando um elemento de outro modelo satisfaz um requisito.
    - A seta aponta para o requisito.

- **Verify**
    - Representa quando um caso de teste é usado para verificar um requisito.
    - A seta aponta para o requisito que é verificado.

- **Derive**
    - usado quando um requisito é derivado de outro requisito baseado na fase de análise.
    - A seta aponta para o requisito de origem.

- **Refine**
    - Usado para representar um `elemento de outro modelo` que esclarece um requisito.
    - A seta aponta para o requisito.

- **Trace**
    - Usado para relacionar requisitos a `elementos de outros modelos` que representa uma origem do requisito.
    - A seta aponta para o elemento do outro modelo.

- **Copy**
    - Relaciona uma cópia de um requisito com o original.
    - A ponta da seta indica o requisito origem.
    - Normalmente utilizado quando o requisito de origem está contido em um padrão.
    
### Demonstrando Justificativas
- Usado para explicar ou justificar um requisito ou um relacionamento entre requisitos.

## Especificação de Requisitos
- É importante registrar as informações coletadas e identificadas na etapa de levantamento de requisitos de forma adequada.
- Documentos de Requisitos = Descrição das características que o sistema deverá apresentar.
- Para documentar requisitos podem ser utilizadas a linguagem natural, modelos formais e diagramas.

### Documento de Requisitos
É um documento utilizado para comunicar os requisitos aos clientes, engenheiros e gerentes.

| | |
|:--:|---|
| **Clientes do Sistema** | Especificam e leem os requisitos para verificar se estes satisfazem suas necessidades. Os clientes especificam as alterações nos requisitos. |
| **Gerentes** | Usam o documento de requisitos para planejar uma proposta para o sistema e planejar o processo de desenvolvimento do sistema. |
| **Engenheiros do Sistema** | Usam os requisitos para entender o sistema que será desenvolvido. |
| **Engenheiros de Teste do Sistema** | Usam os requisitos para desenvolver testes de validação do sistema. |
| **Engenheiros de Manutenção do Sistema** | Usam os requisitos para entender o sistema e os relacionamentos entre suas partes. |
