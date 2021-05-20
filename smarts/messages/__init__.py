from flask import Blueprint

messages_bp = Blueprint('messages', __name__)

from smarts.messages import messages
