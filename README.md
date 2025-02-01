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

## **5. Verify the Setup**

- At this point, your VM should be set up with all the necessary dependencies. You can now proceed with the project-specific setup or development tasks.

---

## **Scripts Included in This Repository**

- `init.sh`: Installs essential dependencies (`make`, `python3.12-venv`, `tree`) and updates the package list.
- Additional scripts (if any) will be documented here.

---

## **Notes**

- The `sudo apt update` step is intentionally run manually at the beginning to ensure the VM is up to date before proceeding.
- The `init.sh` script includes `sudo apt update` again for consistency, but this can be optimized in future iterations.

---

## **Next Steps**

- Refer to the project documentation for further instructions on setting up and running the project.