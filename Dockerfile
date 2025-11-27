FROM python:3.8-slim

WORKDIR /app

# Install system dependencies needed by numpy/pandas/scipy
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    g++ \
    gcc \
    libatlas-base-dev \
    liblapack-dev \
    gfortran \
    graphviz \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all project files
COPY . /app

EXPOSE 8501
ENV PORT=8501

CMD ["streamlit", "run", "app.py", "--server.port=${PORT}", "--server.address=0.0.0.0"]
