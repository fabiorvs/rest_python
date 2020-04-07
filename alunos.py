from flask import jsonify, request
from flask_restful import Resource
from math import ceil
from flask_httpauth import HTTPTokenAuth
from banco import mysql
from funcoes import verificaToken, inserirLog

TOKEN = ""

class alunos(Resource):
    auth = HTTPTokenAuth('Bearer')
    
    @auth.verify_token
    def verify_token(self):
        global TOKEN
        if verificaToken(self):
            TOKEN = self
            return True
        else:
            return False

    @auth.login_required
    def get(self):
        global TOKEN
        inserirLog('GET',str(request.url),TOKEN,str(request.args.to_dict()),str(request.remote_addr))
        con = mysql.connect()
        cur = con.cursor()

        if 'perpage' in request.args:
            PERPAGE = request.args['perpage']
            if int(PERPAGE) > int(100):
                PERPAGE = 100
        else:
            PERPAGE = 10

        if 'page' in request.args:
            PAGE = request.args['page']
        else:
            PAGE = 0

        SQL = "SELECT COUNT(id) AS total FROM alunos"
        cur.execute(SQL)
        r = cur.fetchone()
        TOTAL = r[0]

        PAGE = (int(PERPAGE) * int(PAGE)) - int(PERPAGE)

        if PAGE < 0:
            PAGE = 0

        SQL = "SELECT * FROM alunos ORDER BY id ASC LIMIT {},{}".format(PAGE, PERPAGE)
        cur.execute(SQL)
        r = [dict((cur.description[i][0], value)
                for i, value in enumerate(row)) for row in cur.fetchall()]

        return jsonify({'alunos' : r})

    def post(self):
        return jsonify({'mensagem' : 'teste'})

class alunosId(Resource):
    auth = HTTPTokenAuth('Bearer')
    
    @auth.verify_token
    def verify_token(self):
        global TOKEN
        if verificaToken(self):
            TOKEN = self
            return True
        else:
            return False

    @auth.login_required
    def get(self,id):
        global TOKEN
        inserirLog('GET',str(request.url),TOKEN,str(request.args.to_dict()),str(request.remote_addr))
        con = mysql.connect()
        cur = con.cursor()

        SQL = "SELECT * FROM alunos WHERE id = '{}'".format(id)
        cur.execute(SQL)
        r = [dict((cur.description[i][0], value)
                for i, value in enumerate(row)) for row in cur.fetchall()]
        return jsonify({'alunos' : r})

class alunosCPF(Resource):
    auth = HTTPTokenAuth('Bearer')
    
    @auth.verify_token
    def verify_token(self):
        global TOKEN
        if verificaToken(self):
            TOKEN = self
            return True
        else:
            return False

    @auth.login_required

    def get(self,id):
        global TOKEN
        inserirLog('GET',str(request.url),TOKEN,str(request.args.to_dict()),str(request.remote_addr))
        con = mysql.connect()
        cur = con.cursor()

        SQL = "SELECT * FROM alunos WHERE cpf = '{}'".format(id)
        cur.execute(SQL)
        r = [dict((cur.description[i][0], value)
                for i, value in enumerate(row)) for row in cur.fetchall()]
        return jsonify({'alunos' : r})