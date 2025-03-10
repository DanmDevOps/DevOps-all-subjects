# משתנים גמישים לכל הסביבה

variable "aws_region" {
  default = "us-east-1"
}

variable "azure_location" {
  default = "East US"
}

variable "azure_rg" {
  default = "myResourceGroup"
}

variable "db_user" {
  default = "admin"
}

variable "db_pass" {
  default = "P@ssw0rd123"
}
