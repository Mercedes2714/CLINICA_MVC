from flask import Blueprint, request, redirect, url_for, flash
from datetime import datetime
from extensions import db
from models.consultas import Consulta
from views import consulta_view

consulta_bp = Blueprint('consulta', __name__, url_prefix='/consultas')

@consulta_bp.route('/')
def index():
    """Lista todas las consultas ordenadas por fecha"""
    consultas = Consulta.query.order_by(Consulta.fecha.desc()).all()
    return consulta_view.list(consultas)

@consulta_bp.route('/create', methods=['GET', 'POST'])
def create():
    """Crea una nueva consulta"""
    if request.method == 'POST':
        id_medico = request.form.get('id_medico')
        id_paciente = request.form.get('id_paciente')
        fecha_str = request.form.get('fecha')
        diagnostico = request.form.get('diagnostico')
        tratamiento = request.form.get('tratamiento')
        
        # Validar campos obligatorios
        if not all([id_medico, id_paciente, fecha_str, diagnostico, tratamiento]):
            flash('Todos los campos son obligatorios', 'error')
            return redirect(url_for('consulta.create'))
        
        try:
            # Convertir fecha string a datetime
            fecha = datetime.strptime(fecha_str, '%Y-%m-%dT%H:%M')
        except ValueError:
            flash('Formato de fecha inválido', 'error')
            return redirect(url_for('consulta.create'))
        
        nueva_consulta = Consulta(
            id_medico=int(id_medico),
            id_paciente=int(id_paciente),
            fecha=fecha,
            diagnostico=diagnostico,
            tratamiento=tratamiento
        )
        nueva_consulta.save()
        
        flash('Consulta registrada exitosamente', 'success')
        return redirect(url_for('consulta.index'))
    
    return consulta_view.create()

@consulta_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    """Edita una consulta"""
    consulta = Consulta.query.get_or_404(id)
    
    if request.method == 'POST':
        consulta.id_medico = int(request.form.get('id_medico'))
        consulta.id_paciente = int(request.form.get('id_paciente'))
        fecha_str = request.form.get('fecha')
        consulta.diagnostico = request.form.get('diagnostico')
        consulta.tratamiento = request.form.get('tratamiento')
        
        try:
            consulta.fecha = datetime.strptime(fecha_str, '%Y-%m-%dT%H:%M')
        except ValueError:
            flash('Formato de fecha inválido', 'error')
            return redirect(url_for('consulta.edit', id=id))
        
        db.session.commit()
        flash('Consulta actualizada exitosamente', 'success')
        return redirect(url_for('consulta.index'))
    
    return consulta_view.edit(consulta)

@consulta_bp.route('/delete/<int:id>')
def delete(id):
    """Elimina una consulta"""
    consulta = Consulta.query.get_or_404(id)
    try:
        consulta.delete()
        flash('Consulta eliminada exitosamente', 'success')
    except Exception as e:
        flash('Error al eliminar: ' + str(e), 'error')
    
    return redirect(url_for('consulta.index'))

@consulta_bp.route('/show/<int:id>')
def show(id):
    """Muestra detalle de una consulta"""
    consulta = Consulta.query.get_or_404(id)
    return consulta_view.show(consulta)

# EXTRA: Filtro de consultas por fecha
@consulta_bp.route('/filter')
def filter_by_date():
    """Filtra consultas por rango de fechas (EXTRA)"""
    fecha_inicio = request.args.get('fecha_inicio')
    fecha_fin = request.args.get('fecha_fin')
    
    if fecha_inicio and fecha_fin:
        try:
            inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
            fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
            consultas = Consulta.query.filter(
                Consulta.fecha >= inicio,
                Consulta.fecha <= fin
            ).order_by(Consulta.fecha.desc()).all()
            
            flash(f'Mostrando consultas del {fecha_inicio} al {fecha_fin}', 'info')
        except ValueError:
            flash('Fechas inválidas', 'error')
            return redirect(url_for('consulta.index'))
    else:
        consultas = Consulta.query.all()
    
    return consulta_view.list(consultas)