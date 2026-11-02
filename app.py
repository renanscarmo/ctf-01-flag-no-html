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
        <p>Nada de segredos aqui. O que e secreto fica no servidor.</p>
      </body>
    </html>
    """
  


if __name__ == "__main__":
    app.run()