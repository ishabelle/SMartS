from smarts.auth import auth_bp
from smarts.utils import validate_json_content_type
from webargs.flaskparser import use_args
from smarts.models import User, user_schema, UserSchema
from flask import abort, jsonify
from smarts import db


@auth_bp.route('/register', methods=['POST'])
@validate_json_content_type
@use_args(user_schema, error_status_code=400)
def register(args: dict):
    if User.query.filter(User.username == args['username']).first():
        abort(409, description=f'User with username {args["username"]} already exists')
    if User.query.filter(User.email == args['email']).first():
        abort(409, description=f'User with email {args["email"]} already exists')

    args['password'] = User.generate_hashed_password(args['password'])
    user = User(**args)

    db.session.add(user)
    db.session.commit()

    token = user.generate_jwt()

    return jsonify({
        'success': True,
        'token': token.decode()
    })


@auth_bp.route('/login', methods=['POST'])
@validate_json_content_type
@use_args(UserSchema(only=['username', 'password']), error_status_code=400)
def login(args: dict):
    user = User.query.filter(User.username == args['username']).first()
    if not user:
        abort(401, description='Invalid credentials')

    if not user.is_password_valid(args['password']):
        abort(401, description='Invalid credentials')

    token = user.generate_jwt()

    return jsonify({
        'success': True,
        'token': token.decode()
    })
