# הגדרת S3/Azure Blob Storage

# AWS S3 Bucket
resource "aws_s3_bucket" "app_bucket" {
  bucket = "my-app-storage-bucket"
  acl    = "private"

  versioning {
    enabled = true
  }

  lifecycle_rule {
    id      = "log"
    enabled = true
    expiration {
      days = 30
    }
  }

  tags = {
    Name        = "MyAppS3Bucket"
    Environment = "Production"
  }
}

# Azure Storage Account
resource "azurerm_storage_account" "app_storage" {
  name                     = "myappstorage123"
  resource_group_name      = var.azure_rg
  location                 = var.azure_location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = {
    environment = "Production"
  }
}

# Azure Blob Storage Container
resource "azurerm_storage_container" "app_container" {
  name                  = "app-blob-container"
  storage_account_name  = azurerm_storage_account.app_storage.name
  container_access_type = "private"
}
