docker build -f dockerfile -t plant_disease:latest .
docker run -p 8501:8501 plant_disease:latest