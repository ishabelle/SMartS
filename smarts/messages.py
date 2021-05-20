from smarts import app
from flask import jsonify
from smarts.models import Message, MessageSchema


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
    return jsonify({
        'success': True,
        'data': f'Get message with ID {message_id}'
    })


@app.route('/api/v1/messages', methods=['POST'])
def create_message():
    return jsonify({
        'success': True,
        'data': 'New message has been created'
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
