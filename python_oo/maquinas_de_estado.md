# Máquina de Estados
> Um modelo que representa os estados de um objeto e as transições entre esses estados. Eventos que podem disparar ações que resultam em mudanças de estado.

## Exemplo: Semáforo
- **Teste**
- **Vermelho**
- **Verde**
- **Amarelo**
- **Erro**

### Transições:
- Inicial: **Teste** -(a1)-> **Vermelho**
- Fluxo Principal: **Vermelho** -(a2)-> **Verde** -(a3)-> **Amarelo** -(a4)-> **Vermelho**
- Erro: Loop no estado de erro.
- Qualquer `aN` pode levar a um estado de erro.
