from banco import mysql
def verificaToken(token):
    con = mysql.connect()
    cur = con.cursor()
    SQL = "SELECT COUNT(id) AS total FROM token WHERE token = '{}'".format(token)
    cur.execute(SQL)
    r = cur.fetchone()
    if r[0] > 0:
        return True
    else:
        return False

def inserirLog(metodo,url,token,parametros,ip):
    con = mysql.connect()
    cur = con.cursor()
    parametros = parametros.replace("'","")
    parametros = parametros.replace("u","")
    SQL = 'INSERT INTO log (metodo,url,token,parametros,ip) values("{}","{}","{}","{}","{}")'.format(metodo,url,token,parametros,ip)
    cur.execute(SQL)
    con.commit()