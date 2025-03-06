
provider "aws" {
  region = "us-east-1"
}

provider "azurerm" {
  features {}
}


resource "aws_s3_bucket" "example" {
  bucket = "my-terraform-bucket"
  acl    = "private"
}


resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "East US"
}


resource "azurerm_storage_account" "example" {
  name                     = "mystorageaccount"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

.