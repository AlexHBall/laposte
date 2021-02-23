import datetime

from sqlalchemy.orm import relationship

from app import db
#from app.models.history import History


class City(db.Model):
    __tablename__ = "city"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    weather_id = db.Column(db.Integer)
    weather = db.Column(db.String(256))
    sunrise = db.Column(db.Integer)
    sunset = db.Column(db.Integer)
    #children = relationship("History")


    def __repr__(self):
        return f"City {self.name} current weather {self.weather} sunrise at {self.sunrise} sunset at {self.sunset}"

    def add(self):
        db.session.add(self)
        db.session.commit()

    def get_all(self):
        return City.query.all()