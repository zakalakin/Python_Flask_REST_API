from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    qty = db.Column(db.Integer)

    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    store = db.relationship("StoreModel")

    def __init__(self, name, qty, store_id):
        self.name = name
        self.qty = qty
        self.store_id = store_id

    @classmethod
    def find_by_name(cls, name):
        return ItemModel.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {"name": self.name, "qty": self.qty}

    # store find name by id
