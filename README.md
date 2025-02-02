# CNN Chicken classification

## Workflow

1. Update config.yaml
2. Update secrets.yaml [optional] (eg. if we have a database which has to be kept secret)
3. Update params.yaml
4. Update the entity - create config_entity.py and update
5. Update the configuration manager in src config (configuration.py)
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

# How to run?
STEPS:
Clone the repository

https://github.com/entbappy/Chicken-Disease-Classification--Project

STEP 01- Create a conda environment after opening the repository
conda create -n cnncls python=3.8 -y
conda activate cnncls

STEP 02- install the requirements
pip install -r requirements.txt

# Finally run the following command
python app.py

Now,
open up you local host and port

# DVC cmd
dvc init
dvc repro
dvc dag

# AWS-CICD-Deployment-with-Github-Actions

# 1. Login to AWS console.

# 2. Create IAM user for deployment

#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess

# 3. Create ECR repo to store/save docker image

- Save the URI: 352805769786.dkr.ecr.us-east-1.amazonaws.com/chicken_project

# 4. Create EC2 machine (Ubuntu)

# 5. Open EC2 and Install docker in EC2 Machine:

#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

# 6. Configure EC2 as self-hosted runner:

setting>actions>runner>new self hosted runner> choose os> then run command one by one

# 7. Setup github secrets:

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app


# AZURE-CICD-Deployment-with-Github-Actions
# Save pass:



# Run from terminal:
docker build -t chickenapp.azurecr.io/chicken:latest .

docker login chickenapp.azurecr.io

docker push chickenapp.azurecr.io/chicken:latest

# Deployment Steps:

Build the Docker image of the Source Code
Push the Docker image to Container Registry
Launch the Web App Server in Azure
Pull the Docker image from the container registry to Web App server and run


