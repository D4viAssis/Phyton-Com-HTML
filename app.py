from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    nome = "Turma de programação"
    curso = "Phyton & HTML"

    return render_template (
        'index.html',
        nome = nome,
        curso = curso
    )

@app.route('/sobre')
def sobre():
    return """
    <h1>Sobre a turma</h1>
    <p>Esse projeto foi criado utilizando Python e HTML.</p>
    <a href="/">Voltar para o inicio</a>
    """

    if __name__ == '__main __':
        app.run(host='0.0.0.0.' port=3000, debug=true)
    
    

    