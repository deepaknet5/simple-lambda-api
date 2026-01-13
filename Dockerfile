# Use the official Python slim image as the base image
FROM python:3.9-slim as base

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user
RUN useradd -m appuser
USER appuser

# Copy the application code
COPY . .

# Build the final image
FROM base as final

# Set the working directory
WORKDIR /app

# Copy the application code from the previous stage
COPY --chown=appuser:appuser --from=base /app .

# Set the entrypoint to run the application
ENTRYPOINT ["python", "main.py"]