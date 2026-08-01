# Development Commands

Comandos utilizados no desenvolvimento do MentorOS.

---

# Ambiente Python

## Criar ambiente virtual

```bash
python -m venv .venv
```

## Ativar ambiente virtual

```bash
.\.venv\Scripts\Activate.ps1
```

# Backend

## Executar API localmente

```bash
uvicorn app.main:app --reload
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Atualizar requirements

```bash
pip freeze > requirements.txt
```


# Git

## Criar commit
```bash
git add .
git commit -m "mensagem"
```
