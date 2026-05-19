from flask import Blueprint, request, redirect, url_for, flash
from extensions import db
from models.pacientes import Paciente
from views import paciente_view

paciente_bp = Blueprint('paciente', __name__, url_prefix='/pacientes')

@paciente_bp.route('/')
def index():
    """Lista todos los pacientes"""
    pacientes = Paciente.query.all()
    return paciente_view.list(pacientes)

@paciente_bp.route('/create', methods=['GET', 'POST'])
def create():
    """Crea un nuevo paciente"""
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        edad = request.form.get('edad')
        direccion = request.form.get('direccion')
        telefono = request.form.get('telefono')
        
        # Validar
        if not all([nombre, edad, direccion, telefono]):
            flash('Todos los campos son obligatorios', 'error')
            return redirect(url_for('paciente.create'))
        
        try:
            edad = int(edad)
            if edad < 0 or edad > 150:
                raise ValueError
        except ValueError:
            flash('Edad inválida', 'error')
            return redirect(url_for('paciente.create'))
        
        nuevo_paciente = Paciente(
            nombre=nombre,
            edad=edad,
            direccion=direccion,
            telefono=telefono
        )
        nuevo_paciente.save()
        
        flash('Paciente registrado exitosamente', 'success')
        return redirect(url_for('paciente.index'))
    
    return paciente_view.create()

@paciente_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    """Edita un paciente"""
    paciente = Paciente.query.get_or_404(id)
    
    if request.method == 'POST':
        paciente.nombre = request.form.get('nombre')
        paciente.edad = request.form.get('edad')
        paciente.direccion = request.form.get('direccion')
        paciente.telefono = request.form.get('telefono')
        
        if not paciente.nombre:
            flash('El nombre es obligatorio', 'error')
            return redirect(url_for('paciente.edit', id=id))
        
        db.session.commit()
        flash('Paciente actualizado exitosamente', 'success')
        return redirect(url_for('paciente.index'))
    
    return paciente_view.edit(paciente)

@paciente_bp.route('/delete/<int:id>')
def delete(id):
    """Elimina un paciente"""
    paciente = Paciente.query.get_or_404(id)
    try:
        paciente.delete()
        flash('Paciente eliminado exitosamente', 'success')
    except Exception as e:
        flash('Error al eliminar: ' + str(e), 'error')
    
    return redirect(url_for('paciente.index'))

@paciente_bp.route('/show/<int:id>')
def show(id):
    """Muestra detalle del paciente con historial médico (EXTRA)"""
    paciente = Paciente.query.get_or_404(id)
    return paciente_view.show(paciente)