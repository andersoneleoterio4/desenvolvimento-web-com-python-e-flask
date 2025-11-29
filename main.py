from flask import Flask
from routes.home import home_route
from routes.cliente import cliente_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix='/clientes')
#@app.route('/')
#def home_page():
    #titulo = "Cadastro de Alunos"
    #alunos = [
        #{"nome": "Pedro", "aluno_matriculado": True},
       # {"nome": "Sophia", "aluno_matriculado": True},
        #{"nome": "Vitor", "aluno_matriculado": False}
        #]
    #return render_template ("index.html", titulo=titulo, alunos=alunos)

app.run(debug=True)