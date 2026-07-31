# Engineering Handbook

> Manual de Engenharia do MentorOS

**Versão:** 1.0  
**Status:** Ativo

---

# 1. Objetivo

Este documento define os padrões de engenharia adotados no MentorOS.

Seu objetivo é garantir consistência, qualidade e facilidade de manutenção durante todo o ciclo de vida do projeto.

Todas as decisões de desenvolvimento deverão seguir as diretrizes descritas neste manual.

---

# 2. Filosofia do Projeto

O MentorOS é um projeto pessoal de longo prazo.

A prioridade não é desenvolver rapidamente, mas construir uma plataforma robusta, organizada e preparada para evoluir durante muitos anos.

Os princípios abaixo orientam todas as decisões técnicas.

---

## Simplicidade

Sempre escolher a solução mais simples que resolva o problema atual.

Evitar abstrações desnecessárias.

---

## Modularidade

Cada componente deve possuir apenas uma responsabilidade.

Exemplos:

- cada mentor é independente;
- cada workflow possui uma única finalidade;
- cada integração deve ser desacoplada.

---

## Evolução Contínua

O projeto nunca será considerado "finalizado".

Novas funcionalidades poderão ser incorporadas continuamente.

---

## Documentação Primeiro

Toda funcionalidade relevante deverá possuir documentação mínima antes da implementação.

---

## Independência de Fornecedor

O MentorOS nunca deverá depender exclusivamente de um modelo de IA específico.

Toda comunicação com modelos deverá ocorrer através do AI Gateway.

---

## YAGNI

Não implementar funcionalidades antes que exista uma necessidade real.

Arquitetura preparada para crescer.

Implementação apenas quando necessário.

---

## Qualidade acima de velocidade

Código simples e bem documentado é preferível a soluções extremamente sofisticadas.

---

# 3. Organização do Projeto

Cada diretório possui uma responsabilidade clara.

| Diretório | Responsabilidade |
|-----------|------------------|
| backend | Código Python |
| docs | Documentação |
| database | Scripts SQL |
| n8n | Workflows |
| prompts | Prompts utilizados pelos agentes |
| tests | Testes |
| scripts | Scripts auxiliares |

---

# 4. Organização da Documentação

A documentação segue uma organização por domínio.

Cada documento deve possuir um único propósito.

Evitar duplicação de informações.

Quando necessário, utilizar links entre documentos.

---

# 5. Convenções de Nomenclatura

## Arquivos

Utilizar:

snake_case

Exemplo

```
data_mentor.md
```

---

## Workflows

Formato:

```
wf_<domínio>_<ação>
```

Exemplos

```
wf_ceo_daily_question

wf_ai_gateway

wf_video_analysis
```

---

## Banco de Dados

Tabela:

snake_case

Colunas:

snake_case

Primary Key

```
id
```

Foreign Key

```
mentor_id

conversation_id
```

Timestamp

```
created_at

updated_at
```

---

## Variáveis Python

PEP8.

---

## Branches

Formato

```
feature/...

bugfix/...

docs/...

refactor/...
```

Exemplos

```
feature/mentor-ceo

docs/engineering-handbook

bugfix/telegram-timeout
```

---

# 6. Git Workflow

Fluxo padrão

```
Issue

↓

Kanban

↓

Branch

↓

Desenvolvimento

↓

Testes

↓

Documentação

↓

Merge

↓

Release
```

Cada funcionalidade deverá possuir uma branch própria.

---

# 7. Workflows do n8n

Princípios

- um workflow = uma responsabilidade;
- evitar workflows gigantes;
- reutilizar componentes sempre que possível;
- documentar todos os workflows.

---

# 8. AI Gateway

Toda comunicação com modelos de IA deverá passar pelo AI Gateway.

Objetivos

- desacoplamento;
- failover;
- múltiplos provedores;
- facilidade para futuras migrações.

---

# 9. Prompts

Cada agente possuirá seus próprios prompts.

Os prompts deverão permanecer fora do código.

Estrutura

```
prompts/

mentor/

system.md

examples.md
```

---

# 10. Banco de Dados

Nunca alterar estruturas diretamente.

Toda alteração estrutural deverá ocorrer através de migrations.

---

# 11. Logging

Todo erro relevante deverá ser registrado.

Evitar mensagens genéricas.

Sempre fornecer contexto suficiente para depuração.

---

# 12. Testes

Funcionalidades críticas deverão possuir testes antes da conclusão da tarefa.

Sempre validar:

- fluxo esperado;
- tratamento de erro;
- casos extremos.

---

# 13. Definition of Done

Uma tarefa somente será considerada concluída quando:

- implementação finalizada;
- testes executados;
- documentação atualizada;
- código revisado;
- Kanban atualizado.

---

# 14. Architecture Decision Records (ADR)

Criar uma ADR quando a decisão:

- impactar arquitetura;
- envolver escolha tecnológica;
- afetar futuras implementações.

---

# 15. Checklist para Novas Funcionalidades

Antes de implementar:

- Existe uma necessidade real?
- Está alinhada aos objetivos do projeto?
- Há especificação mínima?
- Existe documentação?
- A arquitetura suporta essa funcionalidade?

---

# 16. Checklist para Releases

Antes de publicar uma nova versão:

- Documentação atualizada
- CHANGELOG atualizado
- Roadmap revisado
- Backlog atualizado
- Testes executados

---

# 17. Filosofia de Aprendizado

O MentorOS não é apenas um software.

É uma plataforma criada para acelerar o desenvolvimento profissional do seu usuário.

Sempre que houver conflito entre adicionar uma funcionalidade "interessante" e outra que realmente contribua para o aprendizado, a segunda deverá ser priorizada.

---

# 18. Melhoria Contínua

Este documento é vivo.

Sempre que uma nova convenção ou padrão for oficialmente adotado, este Handbook deverá ser atualizado.