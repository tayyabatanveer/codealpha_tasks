
# CodeAlpha-Task 1 : URL Shortener

## Description:
This project is a simple URL shortener built with Flask. It allows users to shorten long URLs and access them via short links.
## Prerequisites

Make sure you have the following installed on your system:
- Python (version 3.6 or higher)
- pip (Python package installer
## How to Run
1. Ensure that python and pip are installed on your device.
2. Clone the Repository.
3. Navigate to the project directory.
4. Set up a virtual environment for flask by running the following commands in your terminal:
- pip install virtualenv
- virtualenv env
- env/Scripts/activate
5. Install flask and SQLAlchemy with the following commands in your terminal:
- pip install flask
- pip install Flask Flask-SQLAlchemy
6. Once you have ensured that the virtual environment has been created, database is connected, then use the command : flask run to check the application.
7. Access the application-Open your web browser and go to http://127.0.0.1:5000/.

## Features:
- Shorten long URLs into shorter, more manageable links.
- Redirect short URLs to the original long URLs.
- Validate URLs to ensure they are properly formatted.

## Project Structure
- app.py: The main Flask application file.
- templates/: Directory containing the HTML templates (home.html, shorturl.html, base.html).
- env/: The virtual environment directory (created after setting up the virtual environment).
- instance: urls.database- The SQLite database file.


