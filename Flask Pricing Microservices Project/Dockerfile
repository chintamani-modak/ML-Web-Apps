# Use the official Python image.
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the FLASK_APP environment variable
ENV FLASK_APP=services.pricing

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run gunicorn server when the container launches
CMD ["gunicorn", "-b", ":8080", "services.pricing:app"]