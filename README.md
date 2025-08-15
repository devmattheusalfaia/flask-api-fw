# Flask App — Estrutura Estilo Laravel

Este projeto é um exemplo de aplicação **Flask** organizada com uma estrutura inspirada no Laravel, contendo **controllers**, **services**, **routes**, **bootstrap** e **config** bem definidos.  
Conta também com suporte para **Docker**, **hot reload** em desenvolvimento e **Gunicorn** para produção.

---

## 📂 Estrutura de Pastas

```

flask\_app/
│
├── app/                    # Lógica da aplicação
│   ├── controllers/        # Controladores
│   ├── services/           # Regras de negócio
│   └── **init**.py
│
├── bootstrap/              # Inicialização da aplicação
│   └── app.py
│
├── config/                 # Configurações
│   ├── config.py
│   └── development.py
│
├── routes/                 # Definição de rotas
│   └── web.py
│
├── wsgi.py                 # Ponto de entrada WSGI (prod)
├── requirements.txt        # Dependências
├── docker-compose.yml
├── Dockerfile
├── .dockerignore
├── .env.example
└── README.md

````

---

## 🚀 Rodando o projeto

### 1️⃣ Ambiente local (venv)
```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Rodar servidor
python run.py
# ou, se preferir:
flask run --debug
````

Acesse: [http://localhost:5000](http://localhost:5000)

---

### 2️⃣ Ambiente com Docker 🐳 (desenvolvimento com hot reload)

```bash
docker compose up --build web
```

Acesse: [http://localhost:5000](http://localhost:5000)
Qualquer alteração no código recarrega automaticamente.

---

### 3️⃣ Ambiente com Docker (produção com Gunicorn)

```bash
docker compose up --build web_prod
```

Acesse: [http://localhost:8000](http://localhost:8000)

---

## ⚙️ Variáveis de ambiente

Copie o arquivo `.env.example` para `.env` e ajuste os valores:

```
SECRET_KEY=your-secret-key
```

---

## 📦 Dependências principais

* **Flask** — Framework web
* **Gunicorn** — Servidor WSGI para produção
* **Watchdog** — (opcional) Melhor detecção de mudanças no hot reload

---

## 📜 Licença

Este projeto é livre para uso e modificação.