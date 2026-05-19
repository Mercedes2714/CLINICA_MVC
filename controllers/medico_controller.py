from flask import Blueprint, request, redirect, url_for, flash
from extensions import db
from models.medicos import Medico
from views import medico_view

# Crear Blueprint
medico_bp = Blueprint('medico', __name__, url_prefix='/medicos')

@medico_bp.route('/')
def index():
    """Lista todos los médicos"""
    medicos = Medico.query.all()
    return medico_view.list(medicos)

@medico_bp.route('/create', methods=['GET', 'POST'])
def create():
    """Crea un nuevo médico"""
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form.get('nombre')
        especialidad = request.form.get('especialidad')
        telefono = request.form.get('telefono')
        correo = request.form.get('correo')
        
        # Validar campos obligatorios
        if not nombre or not especialidad or not telefono or not correo:
            flash('Todos los campos son obligatorios', 'error')
            return redirect(url_for('medico.create'))
        
        # Verificar si el correo ya existe
        if Medico.query.filter_by(correo=correo).first():
            flash('El correo ya está registrado', 'error')
            return redirect(url_for('medico.create'))
        
        # Crear y guardar médico
        nuevo_medico = Medico(
            nombre=nombre,
            especialidad=especialidad,
            telefono=telefono,
            correo=correo
        )
        nuevo_medico.save()
        
        flash('Médico registrado exitosamente', 'success')
        return redirect(url_for('medico.index'))
    
    return medico_view.create()

@medico_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    """Edita un médico existente"""
    medico = Medico.query.get_or_404(id)
    
    if request.method == 'POST':
        # Actualizar datos
        medico.nombre = request.form.get('nombre')
        medico.especialidad = request.form.get('especialidad')
        medico.telefono = request.form.get('telefono')
        medico.correo = request.form.get('correo')
        
        # Validar
        if not medico.nombre or not medico.especialidad:
            flash('Nombre y especialidad son obligatorios', 'error')
            return redirect(url_for('medico.edit', id=id))
        
        db.session.commit()
        flash('Médico actualizado exitosamente', 'success')
        return redirect(url_for('medico.index'))
    
    return medico_view.edit(medico)

@medico_bp.route('/delete/<int:id>')
def delete(id):
    """Elimina un médico"""
    medico = Medico.query.get_or_404(id)
    try:
        medico.delete()
        flash('Médico eliminado exitosamente', 'success')
    except Exception as e:
        flash('Error al eliminar: ' + str(e), 'error')
    
    return redirect(url_for('medico.index'))

@medico_bp.route('/show/<int:id>')
def show(id):
    """Muestra el detalle de un médico"""
    medico = Medico.query.get_or_404(id)
    return medico_view.show(medico)