variable "aws_region" {
  description = "The AWS region to deploy resources in"
  default     = "us-east-1"
}

variable "azure_location" {
  description = "The Azure location to deploy resources in"
  default     = "East US"
}

variable "bucket_name" {
  description = "The name of the S3 bucket"
  default     = "my-terraform-bucket"
}

.