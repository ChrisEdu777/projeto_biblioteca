from flask import Flask
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)

def conectar():
    return mysql.connector.connect(**DB_CONFIG)

@app.route("/")
def index():
    try:
        conexao = conectar()
        if conexao.is_connected():
            mensagem = "Conexão com MySQL realizada com sucesso!"
        conexao.close()
    except Exception as erro:
        mensagem = f"Erro ao conectar: {erro}"
    return mensagem

if __name__ == "__main__":
    app.run(debug=True)