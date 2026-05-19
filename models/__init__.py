# models/__init__.py

# Este archivo permite importar los modelos como paquete
from models.medicos import Medico
from models.pacientes import Paciente
from models.consultas import Consulta

__all__ = ['Medico', 'Paciente', 'Consulta']