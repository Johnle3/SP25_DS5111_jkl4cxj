#!/bin/bash

# Update the package list to bring the VM snapshot up to date
echo "Updating package list..."
sudo apt update

# Install make to use makefiles
echo "Installing make..."
sudo apt install make -y

# Install python3.12-venv to create Python virtual environments
echo "Installing python3.12-venv..."
sudo apt install python3.12-venv -y

# Install tree for listing files in a tree structure
echo "Installing tree..."
sudo apt install tree -y

echo "All dependencies installed successfully!"