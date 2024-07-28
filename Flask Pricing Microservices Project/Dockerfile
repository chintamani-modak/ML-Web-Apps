# Use the official Python image.
FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -U pip
RUN pip install h5py --only-binary h5py
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
# RUN pip install --upgrade numpy

# Make port 8080 available to the world outside this container
EXPOSE 8080

CMD ["python", "./services/pricing.py"]
