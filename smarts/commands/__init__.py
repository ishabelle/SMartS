from flask import Blueprint

db_manage_bp = Blueprint('db_manage_cm', __name__, cli_group=None)

from smarts.commands import db_manage_commands
