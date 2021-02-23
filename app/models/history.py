from app import db
class History(db.Model):
    __tablename__ = "history"

    id = db.Column(db.Integer, primary_key=True)
    letter_id = db.Column(db.Integer, db.ForeignKey('letter.id'))
    weather = db.Column(db.String(191))
    time = db.Column(db.DateTime())

    def __repr__(self):
        return f"History {self.id} letter {self.letter_id} status {self.status} at time {self.time}"

    def add(self):
        db.session.add(self)
        db.session.commit()
