# Social Insecurity

## About the project
This project defines a social media web application lacking many key security features. The goal is to identify as many of these as possible, and then proceed to patch them. It can also be used for practice from the perspective of an attacker.

There are also some comments around the code from the “previous developers” that didn’t have time to focus on security while developing the application. These may point in a possible direction to improve security, but of course you are free to choose your own path and implementation.

## Getting started

### Prerequisites
- Python 3.9 or greater
- [PDM](https://daobook.github.io/pdm/) (Python Development Master)

This project uses PDM as a package manager, which is similar to pip, but with more modern features. To install PDM for your operating system, follow the instructions on the [PDM website](https://daobook.github.io/pdm/#installation).

### Installing

Within the root folder of this application, there is a `pyproject.toml` file, which lists all the Python requirements necessary to run the application.

The following command will install all required production and development dependencies in a virtual environment within the project’s root folder:

```sh
pdm install
```

Modern IDEs such as Visual Studio Code, PyCharm, etc. should automatically detect the virtual environment created by PDM within the project’s root folder, and use it for the project. If not, you can manually select the virtual environment by following the instructions found on your IDE’s support pages.

### Structure

```sh
social-insecurity
├── app
│   ├── static
│   │   └── css
│   │       └── general.css
│   ├── templates
│   │   ├── base.html.j2
│   │   ├── comments.html.j2
│   │   ├── friends.html.j2
│   │   ├── index.html.j2
│   │   ├── profile.html.j2
│   │   └── stream.html.j2
│   ├── __init__.py
│   ├── database.py
│   ├── forms.py
│   ├── routes.py
│   └── schema.sql
├── LICENSE.md
├── README.md
├── config.py
├── pdm.lock
├── pyproject.toml
└── socialinsecurity.py
```

The most important files and directories:
- `app/`: This directory is the root of the application, this is from where the pages are served.
- `__init__.py`: Initializes the application.
- `database.py`: Contains the database connection and functions for interacting with the database.
- `forms.py`: Defines the forms that the users will use to input information.
- `routes.py`: Implements the routing between different pages, handles form input and database calls.
- `schema.sql`: Defines the database tables, and their relations.
- `app/static/`: Static content, such as CSS, JavaScript and images can be stored and accessed here from anywhere in the application.
- `app/templates/`: Contains all the HTML in a template format. This allows the Flask backend to display content dynamically, by integrating logical operators and variables into HTML. These are populated once the user requests one of the sites.
- `config.py`: Contains the configuration for the application.
- `pyproject.toml`: Contains the dependencies for the application.
- `socialinsecurity.py`: The entry point for the application.

## Usage
### Starting the application
Run the following command to start the Flask application in debug mode:

```sh
pdm run flask --debug run
```

You should now be able to access the application through your web browser by accessing [localhost:5000](http://localhost:5000) in the address bar.

### Adding dependencies
To install a new dependency, run the following command:

```sh
pdm add <package>
```

### Removing dependencies
To remove a dependency, run the following command:

```sh
pdm remove <package>
```

### Updating dependencies
To update all dependencies, run the following command:

```sh
pdm update
```

## Useful resources
### Tutorials
- [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [The Flask Quickstart guide](https://flask.palletsprojects.com/en/2.2.x/quickstart/)
- [Reference and tutorial for SQL](https://www.w3schools.com/sql/)
- [Git and GitHub tutorial - Useful for collaborating with your team](https://towardsdatascience.com/getting-started-with-git-and-github-6fcd0f2d4ac6)

### Documentation
- [Flask documentation](https://flask.palletsprojects.com/)
- [Flask-WTF documentation](https://flask-wtf.readthedocs.io/)
- [Flask-Login documentation](https://flask-login.readthedocs.io/)
- [Flask-Bcrypt documentation](https://flask-bcrypt.readthedocs.io/)
- [PDM documentation](https://daobook.github.io/pdm/)

## Questions
If you have any questions or problems, don't hesitate to contact me, and I will get back to you as soon as possible.
