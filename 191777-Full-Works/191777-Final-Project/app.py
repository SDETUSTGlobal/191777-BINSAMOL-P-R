from flask import Flask, render_template, request
from flask_mysqldb import MySQL
dbd = Flask(__name__)

dbd.config['MYSQL_HOST'] = 'localhost'
dbd.config['MYSQL_USER'] = 'root'
dbd.config['MYSQL_PASSWORD'] = 'root'
dbd.config['MYSQL_DB'] = 'sakila'

mysql = MySQL(dbd)


@dbd.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        info = request.form
        a = info['l']
        b = info['m']
        c = info['n']
        d = info['o']

        connect = mysql.connection.cursor()
        connect.execute("INSERT INTO loginust(fname,UID,Company_name,email) VALUES (%s,%s,%s,%s)", (a,b,c,d))
        mysql.connection.commit()
        connect.close()
        return render_template('submit.html',ena=a, fui=b,gco=c, coe=d)
    return render_template('login.html')

@dbd.route('/submit')
def page2():
    return render_template('submit.html')


if __name__ == '__main__':
    dbd.run()