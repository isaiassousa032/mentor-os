# AI Gateway

> Especificação técnica do componente responsável pela comunicação com modelos de Inteligência Artificial.

---

# Objetivo

O AI Gateway é uma camada intermediária responsável por abstrair a comunicação entre o MentorOS e os diferentes provedores de Inteligência Artificial.

Seu objetivo é permitir evolução tecnológica sem alterar os componentes consumidores.

---

# Responsabilidade

O AI Gateway será responsável por:

- receber solicitações de IA;
- validar requisições;
- selecionar o provedor adequado;
- enviar prompts aos modelos;
- padronizar respostas;
- tratar erros;
- registrar informações relevantes.

---

# Arquitetura

```text
             n8n Workflow
                  |
                  |
                  v

             AI Gateway

                  |
       ---------------------
       |         |         |
       v         v         v

    Gemini   OpenRouter  Outros
```

---

# Componentes

## Gateway

Responsável pela interface pública do sistema.

Exemplo:

```python
response = gateway.ask(
    prompt="Analise esta ideia"
)
```

O consumidor não precisa conhecer o modelo utilizado.

---

## Providers

Cada provedor possui sua própria implementação.

Exemplo:

```
providers/

├── gemini.py
├── openrouter.py
└── openai.py
```

---

# Fluxo de Comunicação

1. Usuário envia mensagem.
2. n8n recebe evento.
3. Workflow chama AI Gateway.
4. Gateway seleciona modelo.
5. Provider executa chamada.
6. Resposta retorna ao usuário.

---

# Provedores Iniciais

## Google Gemini

Primeiro provedor utilizado.

Motivo:

- disponibilidade atual;
- plano Google AI Pro;
- bom custo-benefício inicial.

---

## Futuros provedores

Possíveis integrações:

- OpenRouter;
- OpenAI;
- Anthropic;
- modelos locais.

---

# Failover

No futuro o AI Gateway poderá selecionar outro provedor quando:

- limite de uso for atingido;
- serviço estiver indisponível;
- custo exceder determinado limite.

---

# Versionamento

O AI Gateway deverá evoluir mantendo compatibilidade.

Mudanças significativas deverão ser registradas através de ADRs.

---

# Primeira Implementação

A versão inicial deverá possuir apenas:

- conexão com Gemini;
- envio de prompt;
- retorno da resposta.

Funcionalidades avançadas serão adicionadas apenas quando houver necessidade real.

---

# Princípios Seguidos

- Provider Agnostic
- Modular by Default
- YAGNI
- Documentation is Code