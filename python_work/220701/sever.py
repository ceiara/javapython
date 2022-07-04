from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
            p::first-letter{font-size: 3em;}
            p::first-line{color: red;}
        </style>
    </head>
    <body>
        <h1>head</h1>
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nulla est, qui non ut modi quia ea omnis architecto itaque? Earum, minima. Nulla, laboriosam harum? Rerum nam nemo accusamus et voluptates!</p>
        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Molestiae exercitationem perspiciatis quod ullam laudantium pariatur provident ea asperiores nobis sint, nisi harum eius corrupti architecto impedit perferendis sit fuga doloremque.</p>
    </body>
    </html>'''

app.run(host="192.168.0.18",port=5000)