from smarts import db
from flask import jsonify, request
from smarts.models import Message, MessageSchema, message_schema
from webargs.flaskparser import use_args
from smarts.utils import validate_json_content_type, token_required
from smarts.messages import messages_bp


@messages_bp.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    message_schema = MessageSchema(many=True)

    return jsonify({
        'success': True,
        'data': message_schema.dump(messages),
        'number_of_records': len(messages)
    })


@messages_bp.route('/messages/<int:message_id>', methods=['GET'])
def get_message(message_id: int):
    message = Message.query.get_or_404(message_id, description=f'Message with id {message_id} not found')

    return jsonify({
        'success': True,
        'data': message_schema.dump(message)
    })


@messages_bp.route('/messages', methods=['POST'])
@token_required
@validate_json_content_type
@use_args(message_schema, error_status_code=400)
def create_message(user_id: str, args: dict):
    message = Message(**args)
    db.session.add(message)
    db.session.commit()

    return jsonify({
        'success': True,
        'data': message_schema.dump(message)
    }), 201


@messages_bp.route('/messages/<int:message_id>', methods=['PUT'])
@token_required
@validate_json_content_type
@use_args(message_schema, error_status_code=400)
def update_message(user_id: str, args: dict, message_id: int):
    message = Message.query.get_or_404(message_id, description=f'Message with id {message_id} not found')
    message.receiver = args['receiver']
    message.date = args['date']
    message.text = args['text']
    message.sender = args['sender']
    db.session.commit()

    return jsonify({
        'success': True,
        'data': message_schema.dump(message)
    })


@messages_bp.route('/messages/<int:message_id>', methods=['DELETE'])
@token_required
def delete_message(user_id: str, message_id: int):
    message = Message.query.get_or_404(message_id, description=f'Message with id {message_id} not found')
    db.session.delete(message)
    db.session.commit()

    return jsonify({
        'success': True,
        'data': f'Message with ID {message_id} has been deleted'
    })
