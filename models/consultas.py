from extensions import db
from datetime import datetime

class Consulta(db.Model):
    """Modelo para registrar consultas médicas"""
    
    __tablename__ = 'consultas'
    
    id_consulta = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    diagnostico = db.Column(db.Text, nullable=False)
    tratamiento = db.Column(db.Text, nullable=False)
    
    # Claves foráneas
    id_medico = db.Column(db.Integer, db.ForeignKey('medicos.id_medico'), nullable=False)
    id_paciente = db.Column(db.Integer, db.ForeignKey('pacientes.id_paciente'), nullable=False)
    
    def __repr__(self):
        return f'<Consulta {self.id_consulta} - {self.fecha.strftime("%d/%m/%Y")}>'
    
    def save(self):
        """Guarda la consulta en la base de datos"""
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        """Elimina la consulta de la base de datos"""
        db.session.delete(self)
        db.session.commit()