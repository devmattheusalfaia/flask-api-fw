# Dockerfile
FROM python:3.12-slim

# Evita buffer de stdout/stderr e cria diretório
ENV PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Dependências do sistema (se precisar add mais depois)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Instala dependências Python primeiro (melhor cache)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia o resto do projeto
COPY . .

# Porta do Flask dev
EXPOSE 5000
# Porta do Gunicorn (prod)
EXPOSE 8000

# Por padrão: dev (pode ser sobrescrito no compose)
CMD ["python", "run.py"]