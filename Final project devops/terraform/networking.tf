# הגדרת תתי רשתות

# AWS VPC
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

# Azure Virtual Network
resource "azurerm_virtual_network" "main" {
  name                = "main-vnet"
  address_space       = ["10.1.0.0/16"]
  location            = var.azure_location
  resource_group_name = var.azure_rg
}
