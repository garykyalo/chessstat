# Use an official Python image as base
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy application files (excluding Stockfish)
COPY . /app

# Download and extract Stockfish
RUN wget -O stockfish.tar "https://github.com/official-stockfish/Stockfish/releases/download/sf_16/stockfish-ubuntu-x86-64-avx2.tar" && \
    mkdir -p /app/stockfish && \
    tar -xvf stockfish.tar -C /app/stockfish --strip-components=1 && \
    rm stockfish.tar

# Ensure Stockfish is executable
RUN chmod +x /app/stockfish/stockfish-ubuntu-x86-64-avx2

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI default port
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
