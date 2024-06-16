# Kapehans Cafe - Website Setup Guide

Welcome to the Kapehans Cafe - Website Setup Guide! This guide will walk you through the process of setting up and running your Django application step by step.

## Prerequisites

Before we start, make sure you have the following installed on your computer:
1. **Python**: Download and install Python from the official website: [python.org](https://www.python.org/). During installation, make sure to check the box that says "Add Python to PATH".

2. **Visual Studio Code (VS Code)** or any other Integrated Development Environment (IDE): Download and install VS Code from the official website: [code.visualstudio.com](https://code.visualstudio.com/).

3. **Git (Version Control)** and install the latest version.

## Step 1: Install Python

1. **Download Python**:
   - Go to [python.org](https://www.python.org/downloads/).
   - Download the latest version for your operating system.

2. **Install Python**:
   - Run the installer and follow the on-screen instructions.
   - Make sure to check the box that says "Add Python to PATH" during the installation process.

3. **Verify Installation**:
   - Open a command prompt (Windows) or terminal (macOS/Linux).
   - Type `python --version` and press Enter. You should see the Python version number if the installation was successful.

## Step 2: Install VS Code

1. **Download VS Code**:
   - Go to [code.visualstudio.com](https://code.visualstudio.com/Download).
   - Download the version for your operating system.

2. **Install VS Code**:
   - Run the installer and follow the on-screen instructions.

## Step 3: Cloning the Repo
1. **Open your terminal in Visual Studio Code**:
   - On Windows: Press `Ctrl + Shift + ~`, type `cmd`, and press Enter.
   - On macOS/Linux: Open the Terminal from your Applications or use a shortcut like `Ctrl + Alt + T`.

2. **Navigate to your project directory**:
   ```sh
   cd C:/Users/YOURNAME/Desktop

3. **Clone the GitHub repository**
   - Run this command to copy all the files from the GitHub repository to your preferred destination (ex. Desktop) 
    ```sh
    git clone https://github.com/floodro/Kapehans.git

## Step 4: Activate your Virtual Environment


**1. Open Visual Studio Code's terminal again and navigate to your project directory:**
   - On Windows: Press `Ctrl + Shift + ~`, type `cmd`, and press Enter.

**3. Create a Virtual Environment:**
   python -m venv env

**4. Activate the Virtual Environment:**
   - On Windows:
   
   .\env\Scripts\activate'
   - On macOS/Linux:
     source env/bin/activate

   You should see `(env)` at the beginning of your terminal prompt, indicating that the virtual environment is active.


## Step 4: Install Dependencies

1. Install dependencies using `requirements.txt`:
   ```sh
   pip install requirements.txt

## Step 5: Running the Django application
**1. Apply database migrations:**
   python manage.py migrate

**2. Create a superuser (admin user):**
   python manage.py createsuperuser
   Follow the prompts to set up your admin username, email, and password.

**3. Run the development server:**
   python manage.py runserver

**4. Go to browser:**
   Open your browser and go to **`http://127.0.0.1:8000/`** to see your Django application running
   