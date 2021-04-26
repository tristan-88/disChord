from .db import db
from sqlalchemy import Date


class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        "products.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    created_at = db.Column(Date)

    review_user = db.relationship("User", back_populates="user_review")
    review_product = db.relationship(
        "Product", back_populates="product_review")