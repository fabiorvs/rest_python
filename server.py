from flask import Flask
from flask_restful import Api
from alunos import alunos, alunosId, alunosCPF

app = Flask(__name__)
api = Api(app)

api.add_resource(alunos, '/alunos/')
api.add_resource(alunosId, '/alunos/<id>')
api.add_resource(alunosCPF, '/alunos/cpf/<id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)