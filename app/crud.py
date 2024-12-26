from sqlalchemy.orm import Session
from app.models import Product



def get_products(session: Session):
    return session.query(Product).all()


def get_product_by_id(session: Session, product_id: int):
    return session.query(Product).filter(Product.id == product_id).first()


def create_product(session: Session, product: Product):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


def update_product(session: Session, product_id: int, product_data: Product):
    product = session.query(Product).filter(Product.id == product_id).first()
    if product:
        for key, value in product_data.dict(exclude_unset=True).items():
            setattr(product, key, value)
        session.commit()
        session.refresh(product)
        return product
    return None


def delete_product(session: Session, product_id: int):
    product = session.query(Product).filter(Product.id == product_id).first()
    if product:
        session.delete(product)
        session.commit()
        return product
    return None
