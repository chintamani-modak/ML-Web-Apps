FROM python:3.10

EXPOSE 8501

WORKDIR /app

# ENV CPATH="/opt/homebrew/include/"
# ENV HDF5_DIR=/opt/homebrew/

COPY requirements.txt ./requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -U pip
RUN pip install h5py --only-binary h5py
RUN pip install -r requirements.txt

COPY . .

CMD streamlit run main_app.py --server.port 8080