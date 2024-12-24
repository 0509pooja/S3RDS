 Certainly! Below is a professional README file with bold subtitles that reflects the tasks you completed, excluding the use of Jenkins:

---

# AWS Lambda & Docker CI/CD Pipeline for S3 to RDS/Glue ETL

## **Overview**

This repository implements an automated ETL (Extract, Transform, Load) pipeline that reads data from an S3 bucket, processes it, and then pushes the data to an RDS database or Glue database if RDS is unavailable. The entire process is containerized using Docker, and an AWS Lambda function is utilized to run the task. 

The infrastructure and resources required for this project are created using Terraform. The goal is to demonstrate the use of Docker, AWS services (S3, RDS, Glue, Lambda), and Terraform for efficient automation.

---

## **Task Breakdown**

### **1. GitHub Repository Setup**
A GitHub repository was created to store the code, Dockerfile, and Terraform scripts required for this project. All necessary files are committed to the repository.

### **2. Dockerfile Creation**
A Dockerfile was developed to create a Docker image that performs the following tasks:
- Reads data from an S3 bucket.
- Attempts to push the data to an RDS instance.
- If RDS fails, it pushes the data to an AWS Glue database.

The Dockerfile uses Python to process the data, and the image is pushed to AWS Elastic Container Registry (ECR).

### **3. Deploy Docker Image to AWS ECR**
The created Docker image is deployed to AWS ECR for future use in an AWS Lambda function. The process is manual but well documented for reproducibility.

### **4. Lambda Function Creation**
An AWS Lambda function is created to execute the ETL process. This function utilizes the Docker image deployed to AWS ECR and is triggered by events from an S3 bucket.

### **5. Terraform Configuration**
Terraform is used to provision the necessary AWS resources, including:
- **S3 bucket**: Used for storing input data.
- **RDS instance**: For storing processed data (if applicable).
- **Glue database**: Fallback storage when RDS is unavailable.
- **Lambda function**: To run the ETL task.
- **IAM roles**: To grant the necessary permissions to interact with AWS resources.

### **6. Documentation**
Screenshots of the Terraform resource creation process, Lambda function execution, and outputs from the AWS Management Console are included in this repository.

---

## **Repository Structure**

```
.
├── docker
│   ├── Dockerfile              # Dockerfile to build the image
│   ├── app.py                 # Python code for ETL process
│   └── requirements.txt       # Python dependencies
├── terraform
│   ├── main.tf                # Terraform configuration for AWS resources
│   ├── variables.tf           # Variables to configure AWS resources
│   └── outputs.tf             # Terraform outputs for resource details
├── screenshots                # Folder with screenshots of the output
├── README.md                  # This file
└── .gitignore                 # Git ignore file for unnecessary files
```

---

## **Setup Instructions**

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/repo-name.git
cd repo-name
```

### **2. Dockerfile Creation**

The Dockerfile is used to create the image that performs the S3 to RDS/Glue ETL operation. Here's a simplified version of the Dockerfile:

```dockerfile
FROM python:3.8-slim

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Add the Python application
COPY app.py /app/

WORKDIR /app

CMD ["python", "app.py"]
```

The Python script `app.py` contains logic to:
- Fetch data from an S3 bucket.
- Push data to an RDS instance.
- Push data to a Glue database if RDS is not available.

### **3. Building and Pushing the Docker Image to AWS ECR**

To build and push the Docker image to AWS ECR:
1. Build the Docker image:
   ```bash
   docker build -t my-image .
   ```
2. Tag the Docker image for ECR:
   ```bash
   docker tag my-image:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/my-repo:latest
   ```
3. Authenticate Docker with ECR:
   ```bash
   aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com
   ```
4. Push the image to ECR:
   ```bash
   docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/my-repo:latest
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

The Lambda function is automatically deployed using Terraform. It uses the Docker image stored in ECR to perform the ETL task when triggered by events from the S3 bucket.

---

## **Screenshots**

All screenshots related to the following processes are included in the `screenshots/` folder:
- Terraform resource creation and output.
- Lambda function execution results.
- Outputs from the AWS Management Console showing the status of the resources.

---

## **Notes**

- **Terraform** is used to automate the creation of AWS resources such as S3, RDS, Glue, Lambda, and IAM roles.
- **Docker** is used to containerize the Python application, which handles the ETL process.
- **AWS Lambda** is used to run the ETL task triggered by S3 events.
- **ECR** is used to store and manage the Docker image.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## **Contact**

For further inquiries or assistance, feel free to contact me at **tushar.patil@godigitaltc.com**.

---

This updated README file is structured professionally, excluding the use of Jenkins as per your requirements. Let me know if you'd like to add or modify any section!
