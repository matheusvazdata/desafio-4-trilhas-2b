FROM python:3.10-slim

# Variáveis de ambiente para acelerar builds e reduzir tamanho
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Instala só o mínimo para o notebook rodar
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc g++ git curl \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Copia apenas requirements primeiro para aproveitar cache
COPY requirements.txt .

# Instala dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o restante do projeto, ignorando arquivos indesejados
COPY . .

# Expõe a porta do Jupyter
EXPOSE 8888

# Comando padrão
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]