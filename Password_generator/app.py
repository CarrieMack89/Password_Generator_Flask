from flask import Flask, render_template, request
import random

app = Flask(__name__)


# function to generate password

def generate_password(length, use_upper, use_digits, use_special):

    # defining character sets
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    symbols = "?!@/_*&%"

# start with lowercase letters by default
    characters = lower

# add other character sets based on user preferences

    if use_upper:
        characters += upper
    if use_digits:
        characters += numbers
    if use_special:
        characters += symbols

# Generate password by randomly selecting characters from character set

    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to check password strength


def check_password_strength(password):
    length = len(password)

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in '?!@/_*&%' for c in password)

    strength = "Weak"

    if length >= 8 and ((has_lower and has_upper) or (has_lower and has_digit) or (has_lower and has_special)):
        strength = "Medium"
    if length >= 12 and has_lower and has_upper and has_digit and has_special:
        strength = "Strong"

    return strength


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        # Get from data
        length = int(request.form['length'])
        use_upper = 'use_upper' in request.form
        use_digits = 'use_digits' in request.form
        use_special = 'use_special' in request.form

# Generate Password
        password = generate_password(
            length, use_upper, use_digits, use_special)
        return render_template('index.html', password=password)

    return render_template('index.html', password=None)


if __name__ == '__main__':
    app.run(host="0.0.0.0.", port=5000, debug=True)
