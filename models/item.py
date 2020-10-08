from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))  # precision=? the number of numbers after the decimal point ? = 2, two decimal places

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')  # we have a store id so we can find a store in the database that matches the id


    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()  # because it's a class method

        # query - SQLAlchemy knows we are building a query on the database
        # filter_by = SELECT * FROM items WHERE name = name
        # saves us from connecting, creating a cursor and everything
        # continue to filter filter_by(name, id, ) like this rather than query.filter_by.filter_by.filter_by
        # first means SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

        # SQLAlchemy does directly translate from an object to a row in a database
        # so no need to tell where the data should be inserted
        # session - a collection of objects that we are going to write to the database
        # can write more than one at once and then add

        # retrieve data with a specific id, add/commit with a different name/price  update
        # so both insert and update can be carried out in one method=

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

# codes have been substantially simplified and no longer need import Sqlite3
