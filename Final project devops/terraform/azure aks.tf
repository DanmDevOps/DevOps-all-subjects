provider "azurerm" {
  features {}
}

resource "azurerm_kubernetes_cluster" "aks" {
  name                = "flask-aks-cluster"
  location            = "East US"
  resource_group_name = "myResourceGroup"
  dns_prefix          = "flaskapp"

  default_node_pool {
    name    = "default"
    node_count = 2
  }
}

output "aks_cluster_name" {
  value = azurerm_kubernetes_cluster.aks.name
}
