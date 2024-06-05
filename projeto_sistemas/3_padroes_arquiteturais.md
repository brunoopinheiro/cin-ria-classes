# Padrões Arquiteturais - Aula 3
## Introdução
> _Fundamental concepts or properties of an entity in its environment and governing principles for the realization and evolution of this entity and its related life cycle processes._ (ISO/IEC/IEEE 42010:2022)

São padrões que alteram o sistema como um todo. São padrões de alto nível, que definem a estrutura global do sistema.

Padrões arquiteturais: **soluções** arquiteturais utilizadas **recorrentemente**
- Arquitetura cliente-servidor
- Arquitetura em camadas
- Arquitetura MVC
- Arquitetura orientada a serviços
- Arquitetura baseada em microsserviços

## Arquitetura Cliente-Servidor
Responsabilidades mudaram ao longo do tempo.
- Cliente
- Servidor

![Arquitetura Cliente-Servidor](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Client-server-model.svg/500px-Client-server-model.svg.png)

## Arquitetura em Camadas
Benefícios da arquitetura em camadas:
- Dividir para conquistar
- Separação de conceitos
- Reuso
- Extensibilidade

Se as interfaces forem **preservadas**, mudanças em uma camada não afetam as outras.

![alt text](https://www.alura.com.br/artigos/assets/padroes-arquiteturais-arquitetura-software-descomplicada/imagem6.jpg)

## Arquitetura MVC
- Model: lógica de negócio
    - Regras de Negócio
    - Interage com meio de persistência.
- View: interface com o usuário
    - Gerencia a apresentação dos dados.
- Controller: intermediário entre Model e View
    - Intermediário entre Model e View e Usuário

![Arquitetura MVC](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/MVC-Process.svg/500px-MVC-Process.svg.png)

## Arquitetura Orientada a Serviços
Elementos principais
- Aplicações
- Meio de comunicação
- Repositório de serviços
- Serviços:
    - Contrato
    - Implementação

![](https://www.alura.com.br/artigos/assets/padroes-arquiteturais-arquitetura-software-descomplicada/imagem9.jpg)

> Camada de negócio é particionada em serviços, e estes interagem com a persistência.

## Arquitetura Baseada em Microsserviços
Originalmente, em SOA:
- Comunicação compartilhada
- Persistência compartilhada

Uma releitura de SOA:
- Maior desacoplamento
- Tipicamente, persistência local.

![](https://www.alura.com.br/artigos/assets/padroes-arquiteturais-arquitetura-software-descomplicada/imagem12.jpg)

## Conteúdo Extra
- [Arquitetura de Software Descomplicada](https://www.alura.com.br/artigos/padroes-arquiteturais-arquitetura-software-descomplicada)