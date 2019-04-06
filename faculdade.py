'''Beatriz Helena dos Santos - 21805492'''
from flask import Flask,render_template
from flaskext.mysql import MySQL
from bd import *

app=Flask(__name__)

mysql = MySQL()

mysql.init_app(app)

app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_DB']='faculdade'

@app.route('/')
def professores():
    cursor = mysql.get_db().cursor()

    return render_template('principal.html',nome=get_nome(cursor,nome))


@app.route('/exibir')
def sobre():
    cursor = mysql.get_db().cursor()
    return render_template('sobre.html',detalhes=get_detalhes(cursor))



if __name__ == '__main__':
    app.run(debug=True)
