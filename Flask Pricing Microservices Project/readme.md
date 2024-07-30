### Building and Deploying a Flask Microservice with Machine Learning on GCP

In this project, We'll use the DummyJSON API for our product data and deploy the application to Google Cloud Platform using App Engine. This project demonstrates how to combine web development, machine learning, and cloud deployment – essential skills for any aspiring data scientist or software engineer. We'll start by setting up our development environment, then move on to developing our Flask application. Next, we'll integrate a simple machine learning model using Scikit-Learn. Finally, we'll deploy our application to Google Cloud Platform and test the deployed endpoints.

Let's dive in!

### API used: DummyJSON API

How to deploy Flask Microservice with Machine Learning on GCP
The model can be ran either in a regular mode or inside a Docker container.

All the main logic sits inside pricing.py file within Services folder. It trains and serialises the model using pickle module.

Using Postman to test the API endpoints involves sending HTTP requests to your Flask server and verifying the responses

Endpoints
### 1. Test Home Endpoint
Endpoint: GET /
Description: Verifies the server is running.
Postman Request:
Open Postman.
Create a new GET request.
Enter the URL: http://localhost:8080/
Click Send.
### 2. Test External Products Endpoint
Endpoint: GET /external-products
Description: Fetches product data from the DummyJSON API.
Postman Request:
Create a new GET request.
Enter the URL: http://localhost:8080/external-products
Click Send.
### 3. Test Train Model Endpoint
Endpoint: POST /train-model
Description: Trains the machine learning model with provided data.
Postman Request:
Create a new POST request.
Enter the URL: http://localhost:8080/train-model
Go to the Body tab.
Select raw and JSON format.
Enter the JSON body with training data, e.g.:
json
Copy code
[
    {"discountPercentage": 12.96, "rating": 4.69, "stock": 94, "price": 549},
    {"discountPercentage": 17.49, "rating": 4.44, "stock": 34, "price": 899},
    {"discountPercentage": 10.00, "rating": 4.30, "stock": 50, "price": 799}
]
Click Send.
### 4. Test Predict Endpoint
Endpoint: POST /predict
Description: Predicts the price based on provided features.
Postman Request:
Create a new POST request.
Enter the URL: http://localhost:8080/predict
Go to the Body tab.
Select raw and JSON format.
Enter the JSON body with feature data, e.g.:
json
Copy code
{
    "discountPercentage": 12.96,
    "rating": 4.69,
    "stock": 94
}
Click Send.
### 5. Test Create Product Endpoint
Endpoint: POST /products
Description: Adds a new product to the list.
Postman Request:
Create a new POST request.
Enter the URL: http://localhost:8080/products
Go to the Body tab.
Select raw and JSON format.
Enter the JSON body with product data, e.g.:
json
Copy code
{
    "name": "Example Product",
    "discountPercentage": 10.00,
    "rating": 4.5,
    "stock": 100,
    "price": 500
}
Click Send.
### 6. Test Get All Products Endpoint
Endpoint: GET /products
Description: Retrieves the list of all products.
Postman Request:
Create a new GET request.
Enter the URL: http://localhost:8080/products
Click Send.
### 7. Test Get Product by ID Endpoint
Endpoint: GET /products/{product_id}
Description: Retrieves a product by its ID.
Postman Request:
Create a new GET request.
Enter the URL: http://localhost:8080/products/1 (Replace 1 with the actual product ID).
Click Send.
### 8. Test Update Product by ID Endpoint
Endpoint: PUT /products/{product_id}
Description: Updates a product by its ID.
Postman Request:
Create a new PUT request.
Enter the URL: http://localhost:8080/products/1 (Replace 1 with the actual product ID).
Go to the Body tab.
Select raw and JSON format.
Enter the JSON body with updated product data, e.g.:
json
Copy code
{
    "name": "Updated Product",
    "discountPercentage": 15.00,
    "rating": 4.7,
    "stock": 80,
    "price": 600
}
Click Send.
### 9. Test Delete Product by ID Endpoint
Endpoint: DELETE /products/{product_id}
Description: Deletes a product by its ID.
Postman Request:
Create a new DELETE request.
Enter the URL: http://localhost:8080/products/1 (Replace 1 with the actual product ID).
Click Send.

### Web App Deployment Steps
### 1) Create the pricing-flask-artifact-registry repository in Google Cloud Platform. We can use its URI in your deployment configurations by following these steps:
1. Locate the Repository URI
First, we need to find the URI of your newly created repository. We can find this in the Google Cloud Console under Artifact Registry. The URI typically looks like this:

Copy code
asia.gcr.io/project-id/pricing-flask-artifact-registry
Replace project-id with your actual Google Cloud project ID.

### 2) Update Deployment Scripts
Use this URI in our deployment scripts where we define the Docker image to be pushed. Here’s how we might adjust our Docker commands:

### 3) Building & Pushing our Docker image:

Copy code
docker build -t asia.gcr.io/project-id/pricing-flask-artifact-registry:latest .
Pushing our Docker image to the repository:


Copy code
docker push asia.gcr.io/project-id/pricing-flask-artifact-registry:latest
Make sure to replace project-id with your actual Google Cloud project ID and specify the correct tag (in this case, latest).

### 4) To deploy your Docker image on Google Cloud Platform using App Engine and Cloud Build with the newly pushed Docker image URI, follow these steps:

### Step 1: Prepare Your App Engine Environment
Ensure that your app.yaml file is correctly set up for a custom environment that will use the Docker image. Here's a sample configuration:

cloudbuild.yaml script:

runtime: custom
env: flex

manual_scaling:
  instances: 1

resources:
  cpu: 1
  memory_gb: 4
  disk_size_gb: 10

network: {}

### Step 2: Configure Cloud Build
Create a cloudbuild.yaml file in your project directory. This file will instruct Cloud Build on how to build and deploy your application using your Docker image.

yaml
Copy code
steps:
- name: 'gcr.io/cloud-builders/docker'
  args: ['pull', 'asia.gcr.io/flask-pricing-microservices4/pricing-flask-artifact-registry:latest']
- name: 'gcr.io/cloud-builders/gcloud'
  args: ['app', 'deploy']
timeout: '1600s'
Above configuration does the following:
- Pulls the latest version of your Docker image.
- Deploys the application to App Engine.
   
### Step 3: Trigger the Build
To trigger the build and deployment process, you need to submit this build to Cloud Build. Run the following command in your project directory where the cloudbuild.yaml file is located:


Copy code
gcloud builds submit --config cloudbuild.yaml
This command will start the Cloud Build process, which pulls our Docker image and deploys it to App Engine according to our specifications.

### Step 4: Verify Deployment
Once the build and deployment process is complete, we can check the status and view our application by accessing the App Engine URL provided in the GCP Console under App Engine > Dashboard.









