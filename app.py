from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import urlparse
import string
import random

app = Flask(__name__)

# Configuring SQLAlchemy to use SQLite database stored in 'urls.database'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# SQLAlchemy model definition for URL storage
class Urls(db.Model):
    id_ = db.Column("CorrespondingID", db.Integer, primary_key=True)
    long = db.Column("longURL", db.String(), nullable=False)
    short = db.Column("shortURL", db.String(6), unique=True, nullable=False)

    def __init__(self, long, short):
        self.long = long
        self.short = short

# Create database tables before the first request
@app.before_request
def create_tables():
    db.create_all()

# Function to generate a random 6-character short URL
def shorten_url():
    characters = string.ascii_letters + string.digits
    while True:
        random_str = ''.join(random.choices(characters, k=6))
        short_url = Urls.query.filter_by(short=random_str).first()
        if not short_url:
            return random_str

# Flask route for the home page, handling URL shortening and redirection
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        initial_url = request.form["URL"]
        
        # Validate if the entered URL is valid
        if not validate_url(initial_url):
            return "Invalid URL", 400

        # Check if the URL already exists in the database
        found_url = Urls.query.filter_by(long=initial_url).first()
        if found_url:
            return redirect(url_for("display_short_url", url=found_url.short))
        else:
            # Generate a new short URL and add to the database
            short_url = shorten_url()
            new_url = Urls(long=initial_url, short=short_url)
            db.session.add(new_url)
            db.session.commit()
            return redirect(url_for("display_short_url", url=short_url))
    
    # Render the home.html template for GET requests
    return render_template("home.html")

# Flask route to display the original and short URLs
@app.route('/<url>')
def display_short_url(url):
    url_data = Urls.query.filter_by(short=url).first_or_404()
    return render_template('shorturl.html', long_url=url_data.long, short_url_display=url_data.short)

# Flask route to handle redirection to the original URL
@app.route('/r/<short_url>')
def redirection(short_url):
    long_url = Urls.query.filter_by(short=short_url).first()
    if long_url:
        return redirect(long_url.long)
    else:
        return '<h1>URL not found</h1>'

# Function to validate URL format
def validate_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
