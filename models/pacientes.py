from extensions import db
from datetime import datetime

class Paciente(db.Model):
    """Modelo para almacenar información de pacientes"""
    
    __tablename__ = 'pacientes'
    
    id_paciente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relación: Un paciente tiene muchas consultas
    consultas = db.relationship('Consulta', backref='paciente', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Paciente {self.nombre} - {self.edad} años>'
    
    def save(self):
        """Guarda el paciente en la base de datos"""
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        """Elimina el paciente de la base de datos"""
        db.session.delete(self)
        db.session.commit()