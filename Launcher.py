from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ярик Привет</title>
            <style>
                body {
                    margin: 0;
                    height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    background-color: #f0f0f0;
                }
                h1 {
                    color: #FF1493; /* Яркий розовый */
                    font-size: 5em;
                }
            </style>
        </head>
        <body>
            <h1>Мыша Привеееет</h1>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
