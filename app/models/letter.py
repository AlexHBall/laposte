import datetime

from sqlalchemy.orm import relationship

from app import db
from app.models.history import History


class Letter(db.Model):
    __tablename__ = "letter"

    id = db.Column(db.Integer, primary_key=True)
    tracking_number = db.Column(db.String(256))
    status = db.Column(db.String(191))
    children = relationship("History")

    priority = {'DR1': 1,
                'PC1': 2,
                'PC2': 2,
                'ET1': 3,
                'ET2': 3,
                'ET3': 3,
                'ET4': 3,
                'EP1': 3,
                'DO1': 3,
                'DO2': 3,
                'DO3': 3,
                'PB1': 3,
                'PB2': 3,
                'MD2': 4,
                'ND1': 4,
                'AG1': 4,
                'RE1': 4,
                'DI1': 5,
                'PC1': 5,
                }

    def __repr__(self):
        return f"Letter id {self.id} tracking number {self.tracking_number} status {self.status}"

    def add(self):
        db.session.add(self)
        db.session.commit()
        history = History(letter_id=self.id, status=self.status,
                          time=datetime.datetime.now())
        history.add()

    def update_status(self, status):
        self.status = status

    def update(self):
        history = History(letter_id=self.id, status=self.status,
                          time=datetime.datetime.now())
        history.add()
        db.session.update(self)
        db.session.commit()

    def get_all(self):
        return Letter.query.all()

    def current_status_outdated(self, code):
        current_priority = 0
        new_priority = Letter.priority[code]
        try:
            current_priority = Letter.priority[self.status]
        except KeyError:
            current_priority = 0
        return True if new_priority > current_priority else False

    @staticmethod
    def tracking_number_is_valid(n):
        return True
        if not isinstance(n, str):
            return False
        if not n.isalnum():
            return False
        if 11 <= len(n) <= 15:
            return False
        return True
