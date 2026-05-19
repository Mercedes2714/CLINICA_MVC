from flask import render_template

def list(pacientes):
    """Retorna la vista de lista de pacientes"""
    return render_template('pacientes/index.html', pacientes=pacientes)

def create():
    """Retorna el formulario de creación"""
    return render_template('pacientes/create.html')

def edit(paciente):
    """Retorna el formulario de edición"""
    return render_template('pacientes/edit.html', paciente=paciente)

def show(paciente):
    """Retorna el detalle del paciente con su historial médico (EXTRA)"""
    return render_template('pacientes/show.html', paciente=paciente)