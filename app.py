from config import DB_CONFIG
from flask import Flask
import mysql.connector

app = Flask(__name__)


def conectar():
    return mysql.connector.connect(**DB_CONFIG)


@app.route("/")
def index():
    conexao = None
    try:
        conexao = conectar()

        if conexao.is_connected():
            mensagem = "Conexão com MySQL realizada com sucesso!!"
    except mysql.connector.Error as erro:
        mensagem = f"Erro ao conectar com o banco de dados: {erro}"
    except Exception as erro:
        mensagem = f"Erro inesperado: {erro}"
    finally:
        # Garante que a conexão seja fechada apenas se tiver sido criada com sucesso
        if conexao and conexao.is_connected():
            conexao.close()

    return mensagem


if __name__ == "__main__":
    app.run(debug=True)
