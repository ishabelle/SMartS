from smarts import app, db
from flask import jsonify, request
from smarts.models import Message, MessageSchema, message_schema
from webargs.flaskparser import use_args


@app.route('/api/v1/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    message_schema = MessageSchema(many=True)

    return jsonify({
        'success': True,
        'data': message_schema.dump(messages),
        'number_of_records': len(messages)
    })


@app.route('/api/v1/messages/<int:message_id>', methods=['GET'])
def get_message(message_id: int):
    message = Message.query.get_or_404(message_id, description=f'Message with id {message_id} not found')

    return jsonify({
        'success': True,
        'data': message_schema.dump(message)
    })


@app.route('/api/v1/messages', methods=['POST'])
@use_args(message_schema)
def create_message(args: dict):
    message = Message(**args)
    db.session.add(message)
    db.session.commit()

    return jsonify({
        'success': True,
        'data': message_schema.dump(message)
    }), 201


@app.route('/api/v1/messages/<int:message_id>', methods=['PUT'])
def update_message(message_id: int):
    return jsonify({
        'success': True,
        'data': f'Message with ID {message_id} has been updated'
    })


@app.route('/api/v1/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id: int):
    return jsonify({
        'success': True,
        'data': f'Message with ID {message_id} has been deleted'
    })
