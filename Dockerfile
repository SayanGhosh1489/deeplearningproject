FROM python:3.8-slim-buster

EXPOSE 8501

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy application files and requirements
COPY . /app
COPY requirements.txt /app/

# Install Python dependencies
RUN pip3 install -r /app/requirements.txt

# Set the entry point
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
