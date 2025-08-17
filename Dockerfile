# --------------------------
# Step 1: Use official Python base image
# --------------------------
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# --------------------------
# Step 2: Install dependencies
# --------------------------
# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies (optional for some packages)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirement.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirement.txt

# --------------------------
# Step 3: Copy project files
# --------------------------
COPY . .

# Create uploads folder
RUN mkdir -p uploads

# --------------------------
# Step 4: Expose port for Cloud Run
# --------------------------
EXPOSE 8080

# --------------------------
# Step 5: Start FastAPI with uvicorn
# --------------------------
# Cloud Run requires listening on 0.0.0.0:$PORT
CMD exec uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}

