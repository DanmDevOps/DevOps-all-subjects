output "aws_instance_ip" {
  value = aws_instance.app.public_ip
}

output "azure_vm_ip" {
  value = azurerm_linux_virtual_machine.app.public_ip_address
}
