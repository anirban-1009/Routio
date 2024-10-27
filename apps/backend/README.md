# Backend for Routio Project

This is the backend service for the **Routio** project, built using Django. It provides a suite of API endpoints to power the Routio application, handling core functionalities such as data management and business logic.

## Dependencies

To run this application in a development environment, you will need some tools such as **Poetry** and **PyEnv** to manage Python versions and dependencies efficiently.

### Prerequisites

- **Poetry**: A tool to manage Python packages and virtual environments.
- **PyEnv**: A simple Python version management tool that allows switching between multiple Python versions easily.

## Setup Instructions

### 1. Install PyEnv

PyEnv is required to ensure the correct Python version (3.12) is being used.

Refer to the official [PyEnv documentation](https://github.com/pyenv/pyenv/blob/master/README.md) for installation instructions.

Once installed, run the following commands:

```bash
pyenv install 3.12
pyenv local 3.12
```

This will install Python 3.12 and set it as the local Python version for this project.

### 2. Install Poetry

To manage the project dependencies, you will need **Poetry**. Install it using the following command (for Fedora-based systems):

```bash
sudo dnf install poetry
```

Alternatively, check the [official Poetry documentation](https://python-poetry.org/docs/) for installation instructions on other operating systems.

Once installed, navigate to the project directory and install the dependencies:

```bash
poetry install
```

Activate the virtual environment using:

```bash
poetry shell
```

This will drop you into a shell with all dependencies installed and ready for use.

### 3. Django Database Migration

After setting up your development environment and installing all dependencies, you will need to apply database migrations to set up the database schema.

Run the following commands:

```bash
python manage.py migrate
```

This will apply all existing migrations to the database.

If you've made changes to the models and need to create new migrations, run:

```bash
python manage.py makemigrations
```

Then, apply the migrations using:

```bash
python manage.py migrate
```

### 4. Running the Django Development Server

To start the development server and test the API endpoints locally, run:

```bash
python manage.py runserver
```

This will start the Django development server at `http://127.0.0.1:8000/`. You can now access the API and test the backend functionality.


## Testing

Head to [https://manage.auth0.com/dashboard/us/dev-v8l73w5o4qropczv/apis/6693d7d137da4085befd8ded/test](https://manage.auth0.com/dashboard/us/dev-v8l73w5o4qropczv/apis/6693d7d137da4085befd8ded/test) to get the access token, and set it in the `.env` file as `AUTH0_ACCESS_TOKEN` environment variable to make the test calls work.

**Coverage** of the unittests can be computed by the `pytest --cov us` command.