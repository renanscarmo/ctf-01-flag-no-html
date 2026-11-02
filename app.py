from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
      <head>
        <title>Cofre Secreto</title>
      </head>
      <body>
        <h1>Cofre Secreto</h1>
        <p>A flag esta guardada aqui. Consegue achar?</p>
        <!-- FLAG{achei_a_falha_no_html} -->
      </body>
    </html>
    """


if __name__ == "__main__":
    app.run()