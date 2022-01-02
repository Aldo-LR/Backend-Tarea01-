from flask import Flask,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']='b1bsbmalzc8b8ynobtum-mysql.services.clever-cloud.com'
app.config['MYSQL_USER']='uhims5ergrswp3ts'
app.config['MYSQL_PASSWORD'] = 'Jdfqc0E0nwmkQFpCxQeW'
app.config['MYSQL_DB'] = 'b1bsbmalzc8b8ynobtum'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute('select codigo,nombre,fechahora from asistencia')
    data = cursor.fetchall()
    cursor.close()
    print(data)
    
    context = {
        'data':data
    }
    
    return render_template('index.html',**context)
app.run(debug=True,port=4000)
