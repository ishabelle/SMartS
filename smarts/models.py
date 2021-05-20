from smarts import db
from marshmallow import Schema, fields, validate, validates, ValidationError
from datetime import datetime


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    receiver = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    text = db.Column(db.String(160), nullable=False)
    sender = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<{self.__class__.__name__}>: Message posted on {self.date} by {self.sender} '


class MessageSchema(Schema):
    id = fields.Integer(dump_only=True)
    receiver = fields.String(required=True, validate=validate.Length(max=50))
    date = fields.Date('%d-%m-%Y', required=True)
    text = fields.String(required=True, validate=validate.Length(min=1, max=160))
    sender = fields.String(required=True, validate=validate.Length(max=50))

    @validates('date')
    def validate_date(self, value):
        if value > datetime.now().date():
            raise ValidationError(f'Date must be lower than {datetime.now().date()}')


message_schema = MessageSchema()
