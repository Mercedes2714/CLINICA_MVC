from flask import render_template
from models.medicos import Medico
from models.pacientes import Paciente

def list(consultas):
    """Retorna la vista de lista de consultas"""
    return render_template('consultas/index.html', consultas=consultas)

def create():
    """Retorna el formulario de creación con médicos y pacientes"""
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    return render_template('consultas/create.html', medicos=medicos, pacientes=pacientes)

def edit(consulta):
    """Retorna el formulario de edición"""
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    return render_template('consultas/edit.html', consulta=consulta, medicos=medicos, pacientes=pacientes)

def show(consulta):
    """Retorna el detalle de la consulta"""
    return render_template('consultas/show.html', consulta=consulta)