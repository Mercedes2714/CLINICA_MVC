from flask import Flask, redirect, url_for, render_template
from config import Config
from extensions import db  # ← Importar desde extensions

def create_app():
    """Función factory para crear la aplicación Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializar SQLAlchemy con la app
    db.init_app(app)  # ← Usar init_app
    
    # Registrar Blueprints
    from controllers.medico_controller import medico_bp
    from controllers.paciente_controller import paciente_bp
    from controllers.consulta_controller import consulta_bp
    
    app.register_blueprint(medico_bp)
    app.register_blueprint(paciente_bp)
    app.register_blueprint(consulta_bp)
    
    # Ruta principal
    @app.route('/')
    def index():
        return render_template('index.html')
    
    # Crear tablas de la base de datos
    with app.app_context():
        db.create_all()
        print("✅ Base de datos creada exitosamente")
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)


app = create_app()