from sqlalchemy.orm import relationship
from models.bill import Factura
from models.product import Product
from models.review import Review


def setup_relationships():
    Product.factura = relationship("Factura", back_populates="products")
    Product.reviews = relationship("Review", back_populates="product")
    Review.product = relationship("Product", back_populates="reviews")
    Factura.products = relationship("Product", back_populates="factura")
