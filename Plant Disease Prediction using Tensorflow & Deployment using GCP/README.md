# ML-based tool for predicting car price
Dataset used: https://www.kaggle.com/code/mohaiminul101/car-price-prediction/data

Production-level examples with similar ML model: 
https://www.autotrader.ca/a/honda/accord%20sedan/toronto/ontario/5_55980460_on20080611094525059/?showcpo=ShowCpo&ncse=no&ursrc=pl&urp=3&urm=8&sprx=100 

- wrapped into Streamlit App
- basic logging with Loguru
- Containerized with Docker: deploy anywhere!

## Running sequence

1.Build the image locally

`docker build -t carpricing:latest . -f Dockerfile`

For m1/m2 Macs to later deploy to Linux server:

`docker buildx build --platform=linux/arm64 . -t carpricing:latest`

2. Run & test locally

`docker run -p 8501:8501 carpricing:latest`

3. Set up the `gcloud` CLI

4. Change into directory with all the files

5. Deploy to GoogleCloud
`gcloud app delploy app.yaml`

6. Open the app in browser
`gcloud app browse`

7. Switch off the app in UI
