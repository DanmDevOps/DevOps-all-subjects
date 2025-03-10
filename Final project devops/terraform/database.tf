# הקמה של RDS ב-AWS + אפשרות ל-Azure SQL

# AWS RDS
resource "aws_db_instance" "rds" {
  allocated_storage    = 20
  engine              = "postgres"
  instance_class      = "db.t3.micro"
  db_name             = "mydatabase"
  username           = var.db_user
  password           = var.db_pass
  skip_final_snapshot = true
}

# Azure SQL Database
resource "azurerm_mssql_database" "sql" {
  name                = "mydatabase"
  resource_group_name = var.azure_rg
  location            = var.azure_location
  server_name         = var.azure_sql_server
}
