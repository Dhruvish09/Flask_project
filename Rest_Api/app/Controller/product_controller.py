from flask import Blueprint

product_api = Blueprint('product_api', __name__)


@product_api.route("/product/add")
def proadd():
    return "This is Product Add page."
