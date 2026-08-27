from flask import Flask
import mysql.connector
from config import DB_CONFIG


app = Flask(__name__)


def conectar():
    return mysql.connector.connect(**DB_CONFIG)


@app.route("/")
def index():
    return """
    <h1>Sistema Biblioteca Escolar</h1>
    <p>Projeto iniciado com Python, Flask e MySQL.</p>
    <a href="/alunos">Ver alunos cadastrados</a>
    """


@app.route("/alunos")
def listar_alunos():
    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)


        cursor.execute("SELECT * FROM aluno")
        alunos = cursor.fetchall()


        cursor.close()
        conexao.close()


        html = """
        <h1>Alunos Cadastrados</h1>
        <a href="/">Voltar</a>
        <br><br>


        <table border="1" cellpadding="8">
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Série</th>
                <th>Turma</th>
                <th>Telefone</th>
            </tr>
        """


        for aluno in alunos:
            html += f"""
            <tr>
                <td>{aluno['id_aluno']}</td>
                <td>{aluno['nome']}</td>
                <td>{aluno['serie']}</td>
                <td>{aluno['turma']}</td>
                <td>{aluno['telefone']}</td>
            </tr>
            """


        html += "</table>"


        return html


    except Exception as erro:
        return f"Erro ao listar alunos: {erro}"


if __name__ == "__main__":
    app.run(debug=True)
