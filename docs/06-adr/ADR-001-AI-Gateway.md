# ADR-001 — AI Gateway

**Status:** Aceito

**Data:** 31/07/2026

---

# Contexto

O MentorOS depende de modelos de Inteligência Artificial para executar praticamente todas as suas funcionalidades.

Inicialmente o projeto utilizará o Google Gemini, aproveitando o plano Google AI Pro disponível durante o desenvolvimento.

Entretanto, a disponibilidade, custos, limites de uso e qualidade dos modelos podem mudar ao longo do tempo.

Além disso, o projeto possui como princípio arquitetural a independência de fornecedores (Provider Agnostic).

Dessa forma, conectar diretamente os workflows do n8n ou o backend a um modelo específico criaria um forte acoplamento tecnológico.

---

# Problema

Como permitir que o MentorOS utilize diferentes modelos de IA sem que o restante da arquitetura precise ser alterado sempre que houver mudança de provedor?

---

# Decisão

Toda comunicação entre o MentorOS e modelos de Inteligência Artificial deverá ocorrer exclusivamente através de um componente chamado **AI Gateway**.

Nenhum workflow do n8n, serviço do backend ou mentor poderá se comunicar diretamente com um provedor de IA.

O AI Gateway será responsável por abstrair completamente essa comunicação.

---

# Responsabilidades do AI Gateway

O AI Gateway deverá:

- receber solicitações dos workflows;
- selecionar o modelo apropriado;
- encaminhar requisições;
- tratar erros;
- realizar failover entre provedores quando necessário;
- padronizar respostas;
- registrar métricas e logs;
- ocultar detalhes específicos de cada API.

---

# Arquitetura

```text
             Mentor
                │
                ▼
         n8n Workflow
                │
                ▼
          AI Gateway
                │
    ┌───────────┼───────────┐
    ▼           ▼           ▼
 Gemini      OpenRouter    Outros
```

Toda expansão futura deverá ocorrer abaixo do AI Gateway.

Os demais componentes do sistema permanecerão inalterados.

---

# Alternativas Consideradas

## Alternativa 1

Conectar diretamente ao Google Gemini.

### Vantagens

- implementação extremamente simples;
- menor quantidade de componentes.

### Desvantagens

- forte acoplamento;
- difícil migração;
- ausência de failover;
- duplicação de lógica em diferentes workflows.

---

## Alternativa 2

Conectar cada workflow ao seu próprio modelo.

### Vantagens

- simplicidade inicial.

### Desvantagens

- manutenção complexa;
- repetição de configuração;
- inconsistência entre workflows;
- difícil gerenciamento.

---

## Alternativa 3 (Escolhida)

Criar uma camada intermediária (AI Gateway).

### Vantagens

- desacoplamento;
- reutilização;
- facilidade para trocar modelos;
- suporte a múltiplos provedores;
- implementação de failover;
- centralização de configurações;
- arquitetura preparada para crescer.

### Desvantagens

- pequena complexidade adicional;
- necessidade de manter um componente intermediário.

---

# Consequências

Após esta decisão:

- todo novo mentor utilizará o AI Gateway;
- novos modelos poderão ser adicionados sem alterar os workflows existentes;
- mudanças de provedor terão impacto mínimo na arquitetura;
- funcionalidades como cache, balanceamento, métricas e failover poderão ser implementadas futuramente sem modificar os consumidores.

---

# Implementação Inicial

A primeira versão do AI Gateway será simples.

Ela deverá:

- receber uma solicitação;
- encaminhar ao Google Gemini;
- retornar a resposta ao solicitante.

Nenhuma funcionalidade adicional será implementada antes de existir necessidade real.

Este comportamento segue o princípio YAGNI adotado pelo projeto.

---

# Evolução Planejada

Conforme o crescimento do MentorOS, o AI Gateway poderá incorporar funcionalidades como:

- failover automático;
- seleção inteligente de modelos;
- cache de respostas;
- controle de custos;
- rate limiting;
- observabilidade;
- métricas de utilização;
- versionamento de prompts;
- políticas de retry;
- balanceamento entre provedores.

Essas funcionalidades serão implementadas apenas quando agregarem valor ao projeto.

---

# Princípios Arquiteturais Atendidos

Esta decisão está alinhada aos seguintes princípios do MentorOS:

- Long-Term First
- Modular by Default
- Provider Agnostic
- Documentation is Code
- Human-Centered AI

---

# Revisão

Esta ADR deverá ser revisada apenas caso a arquitetura do AI Gateway sofra mudanças significativas.