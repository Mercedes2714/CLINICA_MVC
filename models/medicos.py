from extensions import db
from datetime import datetime

class Medico(db.Model):
    """Modelo para almacenar información de médicos"""
    
    __tablename__ = 'medicos'
    
    id_medico = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(100), nullable=False, unique=True)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relación: Un médico tiene muchas consultas
    consultas = db.relationship('Consulta', backref='medico', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Medico {self.nombre} - {self.especialidad}>'
    
    def save(self):
        """Guarda el médico en la base de datos"""
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        """Elimina el médico de la base de datos"""
        db.session.delete(self)
        db.session.commit()