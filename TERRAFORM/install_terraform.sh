#!/bin/bash

# Set Terraform version
TERRAFORM_VERSION="1.5.7"
TERRAFORM_URL="https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_windows_amd64.zip"

# Temporary download directory
TEMP_DIR="/tmp/terraform_install"
INSTALL_DIR="/c/terraform"

# Create directories
mkdir -p "$TEMP_DIR"
mkdir -p "$INSTALL_DIR"

# Download Terraform
echo "Downloading Terraform $TERRAFORM_VERSION..."
curl -fsSL -o "$TEMP_DIR/terraform.zip" "$TERRAFORM_URL"

# Unzip Terraform
echo "Unzipping Terraform..."
unzip -q "$TEMP_DIR/terraform.zip" -d "$INSTALL_DIR"

# Add Terraform to PATH (Windows compatible)
echo "Adding Terraform to PATH..."
export PATH="$INSTALL_DIR:$PATH"
echo 'export PATH="/c/terraform:$PATH"' >> ~/.bashrc

# Cleanup
echo "Cleaning up..."
rm -rf "$TEMP_DIR"

# Verify installation
echo "Verifying installation..."
terraform --version && echo "Terraform $TERRAFORM_VERSION installed successfully!" || echo "Terraform installation failed."
