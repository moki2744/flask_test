from flask import Flask
from project_app.views.main_views import main_bp


def create_app():
    app = Flask(__name__)

    from project_app.views.main_views import main_bp

    app.register_blueprint(main_bp)

    return app

if __name__ == "__main__":
  app = create_app()
  app.run()
  
