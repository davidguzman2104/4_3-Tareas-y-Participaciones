from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('db_alumno.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    alumnos = conn.execute('SELECT * FROM calificacion').fetchall()
    conn.close()
    return render_template('index.html', alumnos=alumnos)

@app.route('/agregar', methods=('GET', 'POST'))
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo_electronico']
        calificacion1 = request.form['calificacion1']
        calificacion2 = request.form['calificacion2']
        calificacion3 = request.form['calificacion3']
        promedio = (float(calificacion1) + float(calificacion2) + float(calificacion3)) / 3

        conn = get_db_connection()
        conn.execute('INSERT INTO calificacion (nombre, correo_electronico, calificacion1, calificacion2, calificacion3, promedio) VALUES (?, ?, ?, ?, ?, ?)', 
                     (nombre, correo, calificacion1, calificacion2, calificacion3, promedio))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('agregar.html')

@app.route('/actualizar/<int:id>', methods=('GET', 'POST'))
def actualizar(id):
    conn = get_db_connection()
    alumno = conn.execute('SELECT * FROM calificacion WHERE id = ?', (id,)).fetchone()
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo_electronico']
        calificacion1 = request.form['calificacion1']
        calificacion2 = request.form['calificacion2']
        calificacion3 = request.form['calificacion3']
        promedio = (float(calificacion1) + float(calificacion2) + float(calificacion3)) / 3

        conn.execute('UPDATE calificacion SET nombre = ?, correo_electronico = ?, calificacion1 = ?, calificacion2 = ?, calificacion3 = ?, promedio = ? WHERE id = ?', 
                     (nombre, correo, calificacion1, calificacion2, calificacion3, promedio, id))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('actualizar.html', alumno=alumno)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM calificacion WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)