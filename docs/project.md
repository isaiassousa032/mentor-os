# Project Context

> Documento de referência rápida do projeto MentorOS.

> Última atualização: 01/08/2026

---

# Visão Geral

**Nome:** MentorOS

**Missão**

Construir um sistema de IA que desenvolve pessoas, e não apenas automatiza tarefas.

---

# Objetivo

Criar uma plataforma modular de mentoria baseada em Inteligência Artificial capaz de acompanhar a evolução profissional do usuário por meio de diferentes mentores especializados.

---

# Stack Atual

## Backend

- Python
- FastAPI

## Banco de Dados

- PostgreSQL
- Neon

## Automação

- n8n

## Infraestrutura

- Oracle Cloud VM (Always Free)

## Interface

- Telegram

## IA

Provedor atual:

- Google Gemini

Planejado:

- OpenRouter
- OpenAI
- Anthropic
- IA Local

---

# Arquitetura

Fluxo atual:

Telegram

↓

n8n

↓

Backend (FastAPI)

↓

AI Gateway

↓

Gemini

↓

PostgreSQL

---

# Princípios

- Long-Term First
- Modular by Default
- Documentation is Code
- Provider Agnostic
- Human-Centered AI

Pergunta norteadora:

> "Isso torna o MentorOS um mentor melhor?"

---

# Estrutura da documentação

- Product
- Architecture
- Database
- Prompts
- Development
- ADR
- Deployment
- Releases

---

# Estado Atual

Sprint atual:

Sprint 1

Status:

Em desenvolvimento.

---

# Funcionalidades Implementadas

- Estrutura do projeto
- Documentação base
- FastAPI
- Swagger
- Configuração inicial

---

# Próximo Objetivo

Implementar o AI Gateway v1.

---

# Decisões Arquiteturais

ADR-001

AI Gateway obrigatório para qualquer comunicação com modelos de IA.

---

# Roadmap Resumido

Sprint 1

- AI Gateway
- Gemini
- PostgreSQL
- n8n
- Telegram
- Mentor CEO

---

# Observações

Este documento deve ser atualizado ao final de cada sprint.