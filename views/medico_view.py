from flask import render_template

def list(medicos):
    """Retorna la vista de lista de médicos"""
    return render_template('medicos/index.html', medicos=medicos)

def create():
    """Retorna el formulario de creación"""
    return render_template('medicos/create.html')

def edit(medico):
    """Retorna el formulario de edición"""
    return render_template('medicos/edit.html', medico=medico)

def show(medico):
    """Retorna el detalle del médico"""
    return render_template('medicos/show.html', medico=medico)