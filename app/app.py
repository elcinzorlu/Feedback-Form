from flask import Flask
from .views import form, detail, list


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder='static')

    app.config.from_pyfile("config.py")
    app.secret_key = b"?039eruif3__"
    if app.config["VERSION"] == "1.0.1":
        pass
    if app.config["VERSION"] == "1.0.2":
        pass

    app.register_blueprint(form.bp)
    app.register_blueprint(list.bp)
    app.register_blueprint(detail.bp)

    return app

app = create_app()
