from flask import Flask

app = Flask(__name__)

titulo_home = "Currículo de Rayanne"
texto_home = "Bem-vindo(a) ao meu currículo."

titulo_sobre = "Sobre Mim"
texto_sobre = "Meu nome é Rayanne Oliveira dos Santos. Sou acadêmica de Sistemas de Informação"

titulo_experiencia = "Experiência Profissional"
texto_experiencia = "Possuo experiência em Assistência Informática: Formatação, Manutenção e Suporte."
titulo_formacao = "Formação Acadêmica"
texto_formacao = "Sou acadêmica do 5º semestre do Bacharelado em Sistemas de Informação | Técnica em Redes de Computadores | Possuo diversos cursos na área"

titulo_contato = "Contato"
texto_contato = "rayanne.oliveira.santos61@aluno.ifce.edu.br | (XX)X.XXXX-XXXX."

@app.route("/")
def home():
    links = ""
    links += f"<li><a href='/sobre'>{titulo_sobre}</a></li>"
    links += f"<li><a href='/experiencia'>{titulo_experiencia}</a></li>"
    links += f"<li><a href='/formacao'>{titulo_formacao}</a></li>"
    links += f"<li><a href='/contato'>{titulo_contato}</a></li>"
    return f"<h1>{titulo_home}</h1><p>{texto_home}</p><ul>{links}</ul>"

@app.route("/sobre")
def sobre():
    return f"<h1>{titulo_sobre}</h1><p>{texto_sobre}</p>"

@app.route("/experiencia")
def experiencia():
    return f"<h1>{titulo_experiencia}</h1><p>{texto_experiencia}</p>"

@app.route("/formacao")
def formacao():
    return f"<h1>{titulo_formacao}</h1><p>{texto_formacao}</p>"

@app.route("/contato")
def contato():
    return f"<h1>{titulo_contato}</h1><p>{texto_contato}</p>"

if __name__ == '__main__':
    app.run(debug=True)