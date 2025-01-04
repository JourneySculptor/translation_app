# Use the official Python 3.13 slim image as the base image
FROM python:3.13-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install Python dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project code into the container
COPY . /app/

# Command to run the application using Uvicorn
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}"]

# Expose the port 8080 for Cloud Run
EXPOSE 8080
