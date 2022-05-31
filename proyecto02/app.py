"""
    Tomado de https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
"""
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
basedir = os.path.abspath(os.path.dirname(__file__))
from config import enlace
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = enlace 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Matricula(db.Model):

    __tablename__ = 'matriculas'

    id = db.Column(db.Integer, primary_key=True)
    nombre_propietario = db.Column(db.String(200))
    placa_carro = db.Column(db.String(10))
    anio_matricula = db.Column(db.String(10), nullable=False) # este atributo no puede ser nulo
    costo_matricula = db.Column(db.String(100))

    def __repr__(self):
        return "Matricula: nombre propietario=%s placa carro=%s año matricula:%s costo matricula:%s" % (
                          self.nombre_propietario,
                          self.placa_carro,
                          self.anio_matricula,
                          self.costo_matricula)

# vista

@app.route('/')
def index():
    matricula = Matricula.query.all()
    return render_template('index.html', matricula=matricula)


@app.route('/<int:matricula_id>/')
def matricula(matricula_id):
    matricula = Matricula.query.get_or_404(matricula_id)
    return render_template('matricula.html', matricula=matricula)


@app.route('/add/matricula/', methods=('GET', 'POST'))
def crear():
    if request.method == 'POST':
        nombre_propietario = request.form['nombre']
        placa_carro = request.form['placa']
        anio_matricula = request.form['anio']
        costo_matricula = request.form['costo']
        matricula = Matricula(nombre_propietario=nombre_propietario,
                          placa_carro=placa_carro,
                          anio_matricula=anio_matricula,
                          costo_matricula= costo_matricula,
                          )
        db.session.add(matricula)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('crear.html')


@app.route('/editar/matricula/<int:matricula_id>/', methods=('GET', 'POST'))
def editar(docente_id):
    matricula = Matricula.query.get_or_404(docente_id)

    if request.method == 'POST':
        nombre_propietario = request.form['nombre']
        placa_carro = request.form['placa']
        anio_matricula = request.form['anio']
        costo_matricula = request.form['costo']


        matricula.nombre_propietario = nombre_propietario
        matricula.placa_carro = placa_carro
        matricula.anio_matricula = anio_matricula
        matricula.costo_matricula = costo_matricula

        db.session.add(matricula)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('editar.html', docente=matricula)
