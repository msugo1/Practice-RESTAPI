from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # back_reference
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    # lazy dynamic turns self.items (a list of items) into a query builder)
    # till json method is called the data in the table is not going to be looked into
    # a trade-off between speed of creating stores and speed of calling json method
    # which one is more important determines it

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()  # because it's a class method

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

