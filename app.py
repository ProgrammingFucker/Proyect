from MySQLdb.cursors import Cursor
from tempfile import template
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Rolex.b1'
app.config['MYSQL_DB'] = ''

mysql = MySQL(app)
app.secret_key = ["mysecretkey"]


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
def home():
    return redirect(url_for('index'))


# Formulario de registro
@app.route('/register', methods=['POST'])
def register():
    msg = ''
    if request.method == 'POST':
        nombres = request.form['txtnombre']
        apellidos = request.form['txtapellido']
        telefono = request.form['contact_phone']
        correo = request.form['txtusurio']
        nombre_u = request.form['txtnameuse']
        contraseña = request.form['txtpassword']
        estado = request.form['id_estado']
        hora = ['txtfecha']
        datos = [nombres, apellidos, telefono,
                 correo, nombre_u, contraseña, hora]
        # Comprobar si el email existe
        cursor = mysql.connection.cursor()
        cursor.execute(
            'SELECT * FROM usuario WHERE correo = %s', [str(correo)])
        emails = cursor.fetchone()
        cursor.close()
        if emails:
            msg = "Ya existe un usuario registrado con el correo indicado"
            return render_template('register.html', datos=datos, msg=msg)

        # guardar en la BD

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO usuario (usuario, password, tipo, nombre, apellido, telefono, correo, id_estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                       (nombre_u, contraseña, 3, nombres, apellidos, telefono, correo, estado))
        mysql.connection.commit()
        msg = 'Se ha creado la cuenta correctamente'
        return render_template('login.html', msg=msg)



if __name__ == '__main__':
    app.run(port=5000, debug=True)
