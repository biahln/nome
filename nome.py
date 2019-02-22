from flask import Flask, request

#Objeto flask

app = Flask(__name__)


#rota para /
@app.route('/')
def principal():
    return '<html><head>' \
           '<title>Página Inicial</title>' \
           '</head>' \
           '<body>' \
           '<h1><a href=''/nome''>Nome</a>' \
           '<h1><a href=''/exibir?nome=Joao&sobrenome=Silva''>Exibir</a>' \
           '</body></html>'

#rota para /nome -- chama o flask e manda criar uma rota(chamando uma funcao que ja existe)

@app.route('/nome')
@app.route('/meuNome')
def nome ():
    metodo = request.method
    return 'Bia'

#rota para /exibir
@app.route('/exibir')
def exibir():
    nome = request.args.get('nome', default='Nome não informado')
    sobrenome= request.args.get('sobrenome', default='Sobrenome não informado')
    return nome + ' ' + sobrenome

#iniciar a app
if __name__  == '__main__':
    app.run(debug=True)

