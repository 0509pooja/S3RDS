provider "aws" {
  region = "us-east-1"

}



# EC2 Instance for Application
resource "aws_instance" "app_instance" {
  ami           = "ami-0e2c8caa4b6378d8c" # Replace with a valid AMI ID
  instance_type = "t2.micro"
  tags = {
    Name = "projecttt"
  }
}

# S3 Bucket for Data
resource "aws_s3_bucket" "app_bucket" {
  bucket = "pooja23-12"
}



# ECR Repository for Docker Image
resource "aws_ecr_repository" "app_ecr" {
  name = "test"
}

# RDS Instance for MySQL Database
resource "aws_db_instance" "app_db" {
  allocated_storage    = 20
  engine               = "mysql"
  engine_version       = "8.0.39"
  instance_class       = "db.t3.micro"
  db_name              = "database1"
  username             = var.rds_username
  password             = var.rds_password
  publicly_accessible  = true
  skip_final_snapshot  = true
}
