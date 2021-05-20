from smarts import db
from marshmallow import Schema, fields


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    receiver = db.Column(db.String(50), nullable=True)
    date = db.Column(db.Date, nullable=True)
    text = db.Column(db.String(160), nullable=True)
    sender = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'<{self.__class__.__name__}>: Message posted on {self.date} by {self.sender} '


class MessageSchema(Schema):
    id = fields.Integer()
    receiver = fields.String()
    date = fields.Date('%d-%m-%Y')
    text = fields.String()
    sender = fields.String()


message_schema = MessageSchema()
