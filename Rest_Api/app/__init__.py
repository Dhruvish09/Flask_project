from flask import Flask
from .Controller import  user_controller,product_controller


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(user_controller.user_api)
    app.register_blueprint(product_controller.product_api)

    return app
