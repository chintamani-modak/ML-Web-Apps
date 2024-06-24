# Use Python 3.10 image from Docker Hub as the base image
FROM python:3.10

# Expose port 8080 for the application
EXPOSE 8080

# Set the working directory in the container to /app
WORKDIR /app

# Install Python dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy the entire application from the current directory to the /app directory in the container
COPY . .

# Command to run the Flask application
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080"]