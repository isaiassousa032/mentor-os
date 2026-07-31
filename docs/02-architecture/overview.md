# Overview

> Visão arquitetural de alto nível do MentorOS.

---

# Objetivo

O MentorOS é uma plataforma modular de desenvolvimento profissional baseada em Inteligência Artificial.

Sua arquitetura foi projetada para permitir evolução contínua, desacoplamento entre componentes e independência de fornecedores específicos de IA.

Cada módulo possui uma responsabilidade claramente definida e pode evoluir independentemente dos demais.

---

# Visão Geral

Em alto nível, o MentorOS é composto por cinco grandes camadas:

- Interface
- Orquestração
- Inteligência
- Persistência
- Conhecimento

Essas camadas trabalham juntas para oferecer mentorias personalizadas, registrar histórico e acompanhar a evolução do usuário.

---

# Arquitetura

```text
                Usuário
                    │
                    ▼
              Telegram Bot
                    │
                    ▼
            n8n Workflows
                    │
                    ▼
              AI Gateway
                    │
      ┌─────────────┴─────────────┐
      ▼                           ▼
Modelos de IA              Serviços externos
                    │
                    ▼
            PostgreSQL
                    │
                    ▼
        Histórico e Memória
```

---

# Camadas

## Interface

Responsável pela interação com o usuário.

Inicialmente:

- Telegram

No futuro poderá incluir:

- Web
- Aplicativo Mobile
- Discord
- WhatsApp

---

## Orquestração

Responsável por automatizar os fluxos.

Tecnologia inicial:

- n8n

Responsabilidades:

- receber mensagens;
- executar workflows;
- chamar o AI Gateway;
- salvar informações;
- disparar eventos.

---

## Inteligência

Camada responsável por toda interação com modelos de IA.

Nenhum componente do sistema deverá comunicar-se diretamente com um modelo.

Toda comunicação ocorrerá através do AI Gateway.

---

## Persistência

Responsável pelo armazenamento permanente.

Tecnologia inicial:

- PostgreSQL

Responsabilidades:

- histórico;
- memória;
- avaliações;
- configurações;
- usuários;
- projetos.

---

## Conhecimento

Camada responsável pelo contexto utilizado pelos mentores.

Inicialmente:

- prompts
- histórico

Futuramente:

- RAG
- documentos
- projetos
- apresentações
- embeddings

---

# AI Gateway

O AI Gateway é um dos principais componentes do MentorOS.

Sua função é abstrair completamente os provedores de IA.

Benefícios:

- desacoplamento;
- failover;
- múltiplos modelos;
- facilidade de migração.

---

# Componentes Principais

## Mentores

Cada mentor representa uma especialidade.

Exemplos:

- CEO
- Data Mentor
- Communication Mentor
- RH
- Product Manager

Todos utilizam a mesma infraestrutura.

Mudam apenas:

- prompts;
- contexto;
- regras.

---

## Banco de Dados

O MentorOS utiliza PostgreSQL como banco relacional principal.

Toda persistência deverá ocorrer através dessa camada.

O provedor de infraestrutura poderá ser alterado sem impacto na arquitetura.

---

## Prompts

Os prompts fazem parte da arquitetura.

Eles não deverão permanecer embutidos no código.

Cada mentor possuirá seus próprios arquivos de configuração.

---

# Princípios Arquiteturais

A arquitetura segue cinco princípios fundamentais.

- Long-Term First
- Modular by Default
- Documentation is Code
- Provider Agnostic
- Human-Centered AI

Toda decisão arquitetural deverá respeitar esses princípios.

---

# Evolução

A arquitetura foi projetada para crescer de forma incremental.

Novos componentes deverão ser adicionados através de módulos independentes, evitando impacto sobre funcionalidades já existentes.

---

# Fora do Escopo

Este documento não descreve:

- estrutura do banco;
- endpoints;
- APIs;
- detalhes de implementação;
- tecnologias específicas de infraestrutura.

Esses assuntos possuem documentação própria.

---

# Próximos Documentos

Os detalhes desta arquitetura encontram-se distribuídos em documentos específicos.

- AI Gateway
- Workflows
- Banco de Dados
- Deploy
- APIs
- ADRs

Este documento funciona como ponto de entrada para a arquitetura do MentorOS.