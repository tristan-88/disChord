from flask import Blueprint, jsonify
from flask_login import current_user
from app.models import db, Product, Store, Review

product_routes = Blueprint('products', __name__)

# for route testing
tests = {'Message': 'Hello'}

# ---GET--- http://localhost:5000/api/products/ ---UNTESTED---


@product_routes.route('/')
def all_products():
    return jsonify(tests)

# ---POST--- http://localhost:5000/api/products ---UNTESTED---


@product_routes.route('/', methods=['POST'])
def create_product():
    return jsonify(tests)

# ---GET--- http://localhost:5000/api/products/id ---UNTESTED---


@product_routes.route('/<int:id>')
def single_product(id):
    product = Product.get(id)
    return product.to_dict()


# ---PATCH--- http://localhost:5000/api/products/id ---UNTESTED---


# @product_routes.route('/<int:id>', methods=['PATCH'])
# def edit_product(id):
#     product = Product.query.get(id)

#     new_product = Product()
#     form_data = ProductForm()
#     if form_data.validate_on_submit():
#         form_data.populate_obj(new_product)
#         product = new_product
#         db.session.commit()

# ---DELETE --- http://localhost:5000/api/products/id ---untested---
@product_routes.route('/<int:id>', methods=["Delete"])
def delete_product(id):
    remove_product = Product.query.filter(Product.id == id).delete()
    db.session.commit()
    return jsonify('Product was successfully deleted!' if remove_product else "Could not delete product")

# ---GET --- http://localhost:5000/api/products/:id/reviews #! ??