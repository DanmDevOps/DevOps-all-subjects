output "s3_bucket_name" {
  description = "The name of the S3 bucket"
  value       = aws_s3_bucket.example.bucket
}

output "azure_resource_group_name" {
  description = "The name of the Azure resource group"
  value       = azurerm_resource_group.example.name
}

.
