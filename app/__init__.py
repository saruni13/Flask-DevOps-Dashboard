from Flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import dashboard_bp
    app.register_blueprint(dashboard_bp)

    return app
