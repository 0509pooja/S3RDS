## **Overview**

This repository implements that reads data from an S3 bucket, processes it, and then pushes the data to an RDS database. The entire process is containerized using Docker, and an AWS Lambda function is utilized to run the task. 

The infrastructure and resources required for this project are created using Terraform. The goal is to demonstrate the use of Docker, AWS services (S3, RDS, Lambda), and Terraform for efficient automation.

---

## **Task Breakdown**

### **1. GitHub Repository Setup**
A GitHub repository was created to store the code, Dockerfile, and Terraform scripts required for this project. All necessary files are committed to the repository.

### **2. Dockerfile Creation**
A Dockerfile was developed to create a Docker image that performs the following tasks:
- Reads data from an S3 bucket.
- Attempts to push the data to an RDS instance.
 
The Dockerfile uses Python to process the data, and the image is pushed to AWS Elastic Container Registry (ECR).

### **3. Deploy Docker Image to AWS ECR**
The created Docker image is deployed to AWS ECR for future use in an AWS Lambda function. The process is manual but well documented for reproducibility.

### **4. Lambda Function Creation**
An AWS Lambda function is created to execute the ETL process. This function utilizes the Docker image deployed to AWS ECR.

### **5. Terraform Configuration**
Terraform is used to provision the necessary AWS resources, including:
- **S3 bucket**: Used for storing input data.
- **RDS instance**: For storing processed data.
- **IAM roles**: To grant the necessary permissions to interact with AWS resources.

### **6. Documentation**
Screenshots of the Terraform resource creation process, Lambda function execution, and outputs from the AWS Management Console are included in this repository.

## **Setup Instructions**

### **1. Clone the Repository**

```bash
git clone https://github.com/0509pooja/S3RDS
 
```

### **2. Dockerfile Creation**

The Dockerfile is used to create the image that performs the S3 to RDS operation. Here's a simplified version of the Dockerfile:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY app.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
```

The Python script `app.py` contains logic to:
- Fetch data from an S3 bucket.
- Push data to an RDS instance.
-  
### **3. Building and Pushing the Docker Image to AWS ECR**

To build and push the Docker image to AWS ECR:
1. Build the Docker image:
   ```bash
   docker build -t my-image .
   ```
2. Tag the Docker image for ECR:
   ```bash
   
   ```
3. Authenticate Docker with ECR:
   ```bash
   
   ```
4. Push the image to ECR:
   ```bash
   
   ```

### **4. Applying Terraform Configuration**

To provision the required AWS resources, you need to apply the Terraform configuration:

1. Navigate to the `terraform/` directory:
   ```bash
   cd terraform
   ```
2. Initialize Terraform:
   ```bash
   terraform init
   ```
3. Apply the configuration:
   ```bash
   terraform apply
   ```

This will create the necessary AWS resources including the S3 bucket, RDS instance, Glue database, IAM roles, and Lambda function.

### **5. Deploy Lambda Function**

. It uses the Docker image stored in ECR to perform the ETL task when triggered by events from the S3 bucket.

---

## **Screenshots**

All screenshots related to the following processes are included in the repo:
- Terraform resource creation and output.
- Lambda function execution results.
- Outputs from the AWS Management Console showing the status of the resources.

---

## **Notes**

- **Terraform** is used to automate the creation of AWS resources such as S3, RDS, Lambda, and IAM roles.
- **Docker** is used to containerize the Python application, which handles the ETL process.
- **AWS Lambda** is used to run the ETL task triggered by S3 events.
- **ECR** is used to store and manage the Docker image.

---

 
