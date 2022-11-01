from flask import Flask, request, render_template
from markupsafe import escape

clickart = Flask(__name__)

@clickart.route('/index')
def principal():
    return render_template('index.html')

@clickart.route('/obras')
def obras():
    return render_template('obras.html')

@clickart.route('/poemas')
def poemas():
    return render_template('poemas.html')

@clickart.route('/fotografias')
def fotografias():
    return render_template('fotografias.html')

@clickart.route('/musicas')
def musicas():
    return render_template('musicas.html')

@clickart.route('/contato')
def contato():
    return render_template('contato.html')

@clickart.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == "__main__":
    clickart.run(debug=True)

    #Emerson, Pablo, Sócrates e Karoll