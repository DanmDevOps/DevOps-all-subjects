# יצירת שרתי EC2 או Azure VM

# AWS EC2
resource "aws_instance" "app" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
  subnet_id     = aws_subnet.public.id
}

# Azure VM
resource "azurerm_linux_virtual_machine" "app" {
  name                = "app-vm"
  resource_group_name = var.azure_rg
  location            = var.azure_location
  size                = "Standard_B1s"
  admin_username      = "adminuser"
}
