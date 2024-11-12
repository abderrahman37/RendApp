from flask import Flask, render_template_string, url_for

app = Flask(__name__)

@app.route('/')
def birthday_message():
    # HTML template with image and extended birthday message
    html = '''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Birthday Message</title>
        <style>
            body {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f5f5dc;
                font-family: Arial, sans-serif;
                text-align: center;
            }
            img {
                width: 60%;
                max-width: 500px;
                max-height: 500px;
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }
            h1, h2 {
                color: #FF69B4;
                margin-top: 20px;
            }
            h1 {
                font-size: 2em;
            }
            h2 {
                font-size: 1.5em;
                font-weight: normal;
                color: #FF69B4;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <!-- Display image -->
        <img src="{{ url_for('static', filename='birthday_image.jpg') }}" alt="Birthday Image">
        <!-- Display birthday messages -->
        <h1>HAPPY BIRTHDAY MY DIAMANDA</h1>
        <h2>You're the most beautiful, kindest best girlfriend ever. I lOVE YOU SO MUCH !</h2>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
