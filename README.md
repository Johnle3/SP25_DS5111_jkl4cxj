# Project Setup Guide

This guide will walk you through the steps to set up a new VM for this project. Follow the instructions below to ensure your environment is ready.

---

## **1. Initial VM Setup**

1. **Update the Package List**:
   - Run the following command to ensure your VM is up to date:
     ```bash
     sudo apt update
     ```

2. **Install Git** (if not already installed):
   - Install Git using the following command:
     ```bash
     sudo apt install git -y
     ```

---

## **2. Set Up Git Credentials and SSH Key**

1. **Configure Git Credentials**:
   - Set your Git username and email:
     ```bash
     git config --global user.name "Your Name"
     git config --global user.email "your.email@example.com"
     ```

2. **Generate an SSH Key**:
   - Run the following command to generate a new SSH key:
     ```bash
     ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
     ```
   - Press `Enter` to accept the default file location and passphrase (or set a passphrase if desired).

3. **Add the SSH Key to Your Git Provider**:
   - Copy the contents of your public key:
     ```bash
     cat ~/.ssh/id_rsa.pub
     ```
   - Paste the key into your Git provider's SSH key settings (e.g., GitHub, GitLab, Bitbucket).

---

## **3. Clone the Repository**

1. **Clone the Repository**:
   - Run the following command to clone the repository:
     ```bash
     git clone git@github.com:your-username/your-repo.git
     ```
   - Replace `your-username` and `your-repo` with your actual GitHub username and repository name.

2. **Navigate to the Repository**:
   - Change into the repository directory:
     ```bash
     cd your-repo
     ```

---

## **4. Run the Initialization Script**

1. **Make the Script Executable**:
   - Ensure the `init.sh` script is executable:
     ```bash
     chmod +x init.sh
     ```

2. **Run the Script**:
   - Execute the script to install dependencies:
     ```bash
     ./init.sh
     ```

---

## **5. Set Up the Virtual Environment with `make update`**

The `Makefile` includes a target called `update` to set up and configure the virtual environment. This target installs the required Python dependencies listed in `requirements.txt`.

### **Steps to Set Up the Virtual Environment**

1. **Run the `update` Target**:
   Execute the following command to set up the virtual environment:
   ```bash
   make update

2. **Run the `ygainers.csv` Target**:
   Run a headless browser session and generate a CSV file from scraped data:
   ```bash
   make ygainers.csv

## **6. Testing and Linting **

The `Makefile` includes a target called `update` to set up and configure the virtual environment. This target installs the required Python dependencies listed in `requirements.txt`.


1. **Run the Test**:
   Test your application to ensure everything works as expected:
   ```bash
   make test
