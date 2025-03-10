 # חוקי אבטחה 

 # AWS Security Group
resource "aws_security_group" "allow_http" {
  name        = "allow_http"
  description = "Allow HTTP inbound traffic"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Azure Network Security Group
resource "azurerm_network_security_group" "allow_http" {
  name                = "allow_http"
  location            = var.azure_location
  resource_group_name = var.azure_rg

  security_rule {
    name                   = "Allow_HTTP"
    priority               = 100
    direction              = "Inbound"
    access                 = "Allow"
    protocol               = "Tcp"
    source_port_range      = "*"
    destination_port_range = "80"
    source_address_prefix  = "*"
    destination_address_prefix = "*"
  }
}
