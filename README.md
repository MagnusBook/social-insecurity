# social-insecurity

This project defines a social media web application lacking many key security features. The goal is to identify as many of these as possible, and then proceed to patch them. It can also be used for practice from the perspective of an attacker.

There are also some comments around the code from the "previous developers" that didn't have time to focus on security while developing the application. These may point in a possible direction to improve security, but of course you are free to choose your own path and implementation.

## Installing dependencies
Within the root folder of this application, ther is a `requirements.txt` file, which lists all the python requirements necessary to run the application. If you do not have pyhon installed, I would recommend installing  [anaconda](https://www.anaconda.com/distribution/), since it comes with many packages pre-installed, as well as some other useful tools.

It should be noted that this application has only been run in a python 3.7 environment so far, but other python 3 versions will likely work as well.

The following command install all required dependencies:

```
pip install -r requirements.txt
```

## Starting the application
Run the following command to start the Flask application:

```
flask run
```

You should now be able to access the application through your web browser by accessing [localhost:5000](http://localhost:5000) in the address bar.

## Common issues
Some installations show an error similar to this when starting the application for the first time: 

```
sqlite3.OperationalError: near "FOREIGN": syntax error
```

This can be safely ignored, since the most important parts of the database have been prepared by this point.

## Structure
```
social-insecurity
│   .flaskenv
|   config.py
│   README.md
│   requirements.txt
│   socialinsecurity.py
│
└───app
│   │   __init__.py
│   │   forms.py
│   │   routes.py
│   │   schema.sql
│   │
│   └───static
│   |   │   css
│   |   │   js
│   |   │   uploads
|   |
|   |___templates
│       │   base.html
│       │   comments.html
│       │   friends.html
│       │   index.html
│       │   profile.html
│       │   stream.html
```

Most important files/directories:
- `config.py`: Contains configuration for the application.
- `app/`: This directory is the root of the application, this is from where the pages are served.
- `__init__.py`: Initializes the application and the database.
- `forms.py`: Defines the forms that the users will use to input information
- `routes.py`: Implements the routing between different pages, and handles form input.
- `schema.sql`: Defines the database tables, and their relations.
- `static/`: Static content, such as css, JavaScript and images can be stored and accessed here from anywhere in the application.
- `templates`: Contains all the HTML in a template format. This allows the Flask backend to display content dynamically, by integrating logical operators and variables into HTML. These are populated once the user requests one of the sites.

## Useful resources
- [Good tutorial for flask](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Reference and tutorial for SQL](https://www.w3schools.com/sql/default.asp)
- [Git and GitHub tutorial - Useful for collaborating with your team](https://towardsdatascience.com/getting-started-with-git-and-github-6fcd0f2d4ac6)
- [JavaScript tutorial and reference](https://www.w3schools.com/js/default.asp)

## Questions
If you have any questions or problems, don't hesitate to contact me, and I will get back to you as soon as possible.
