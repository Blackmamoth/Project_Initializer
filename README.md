# Project Initializer (CURRENTLY ONLY SUPPORTED FOR UNIX/LINUX Platforms)

Project Initializer is a command-line utility written in Python that helps you create basic boilerplate for frameworks that don't have CLI support. It simplifies the process of setting up a new project by generating the necessary files and directory structure for your chosen language and framework.

## Installation

1. Clone the repository:

   ```shell
    git clone https://github.com/your-username/project-initializer.git
    ```
2. Create virtual environment
    ```shell
    python3 -m venv venv
    ```
3. Activate the virtual environment
    Linux:
    ```shell
    source venv/bin/activate
    ```
    Windows
      ```shell
    venv\Scripts\activate
    ```
4. Install dependencies
    ```shell
    pip install -r requirements.txt
    ```

# Usage
### To use Project Initializer, run the project-init command with the following arguments:

1. --language: Specify the programming language you want to use (e.g., Python, JavaScript).
2. --framework: Specify the framework you want to set up (e.g., Flask, Express).
3. --path: Specify the path where you want to create the project files.
4.  Here's an example of how to create a new project using Project Initializer:

    ```shell
    python initializer --language js --framework express --path /path/to/project
    ```

