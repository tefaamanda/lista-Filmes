from urllib import request
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

#Lista
filmes = []

#Rota para definir a página inicial
@app.route('/')
def index():
    return render_template('index.html', filmes=filmes)

#Rota para adicionar filmes
@app.route('/adicionar_filme', methods=['GET', 'POST'])
def adicionar_filme():
    if request.method == 'POST':
        nomefilme = request.form['nome']
        datafilme = request.form['data']
        produtor = request.form['produtor']
        codigo = len(filmes)
        filmes.append([codigo, nomefilme, datafilme, produtor])
        return redirect('/')
    else:
        return render_template('adicionar_filme.html')

#Rota para editar filmes
@app.route('/editar_filme/<int:codigo>', methods=['GET', 'POST'])
def editar_filme(codigo):
    if request.method == 'POST':
        nomefilme = request.form['nome']
        datafilme = request.form['data']
        produtor = request.form['produtor']
        filmes[codigo] = [codigo, nomefilme, datafilme, produtor]
        return redirect('/')
    else:
        filme = filmes[codigo]
        return render_template('editar_filme.html', filme=filme)

#Rota para apagar filmes
@app.route('/apagar_filme/<int:codigo>')
def apagar_filme(codigo):
    del filmes[codigo]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)