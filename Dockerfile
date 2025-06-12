FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Optional: for healthcheck, etc.
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Create app user using useradd
RUN useradd -m -d /home/appuser -s /bin/bash appuser
ENV HOME=/home/appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY Data/aggregated_df.csv /app/Data/aggregated_df.csv

USER appuser

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

ENTRYPOINT ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]