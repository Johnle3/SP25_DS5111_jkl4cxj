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
